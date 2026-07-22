import dataclasses
import functools
import time
from asyncio import Lock
from collections.abc import Callable, Coroutine
from logging import Logger
from typing import Any, Concatenate, ParamSpec, TypeVar

from fastapi import HTTPException, status
from httpx import AsyncClient, HTTPStatusError

import gpdp.util.logging as gpdp_logging
from gpdp.config import Config
from gpdp.http.content_types import CONTENT_TYPE_JSON
from gpdp.http.headers import (
    ACCEPT,
    ACCEPT_LANGUAGE,
    AUTHORIZATION,
    CONTENT_TYPE,
    USER_AGENT,
)
from gpdp.util.logging import STATUS

P = ParamSpec("P")
R = TypeVar("R")


def httpx_error_to_fastapi(logger_getter: Callable[[Any], Logger]):
    def decorator(func: Callable[Concatenate[Any, P], Coroutine[Any, Any, R]]):
        @functools.wraps(func)
        async def wrapper(self: Any, *args: P.args, **kwargs: P.kwargs):
            try:
                return await func(self, *args, **kwargs)
            except HTTPStatusError as e:
                res = e.response
                logger_getter(self).error(
                    "Dispenser error: %s",
                    res.json().get("error"),
                    extra={STATUS: res.status_code},
                )
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY, detail="Dispenser error"
                )

        return wrapper

    return decorator


@dataclasses.dataclass
class AuthBundle:
    authToken: str
    userAgent: str
    gsfId: str
    dfeCookie: str
    deviceCheckInConsistencyToken: str | None
    deviceConfigToken: str | None
    mccMnc: str | None


class PlayAuthService:
    def __init__(self, http: AsyncClient, config: Config, device: dict[Any, Any]):
        self.http = http
        self.logger = gpdp_logging.get_logger(self)
        self.dispenser_url = config.dispenser_url
        self.refresh_cooldown = config.dispenser_refresh_cooldown
        self.device = device
        self.last_auth = 0
        self.auth_lock = Lock()

    def build_user_agent(self):
        def prop(name: str):
            return self.device.get(name, "")

        return (
            f"Android-Finsky/{prop('Vending.versionString')} ("
            f"api={3},"
            f"versionCode={prop('Vending.version')},"
            f"sdk={prop('Build.VERSION.SDK_INT')},"
            f"device={prop('Build.DEVICE')},"
            f"hardware={prop('Build.HARDWARE')},"
            f"product={prop('Build.PRODUCT')},"
            f"platformVersionRelease={prop('Build.VERSION.RELEASE')},"
            f"model={prop('Build.MODEL')},"
            f"buildId={prop('Build.ID')},"
            f"isWideScreen={0},"
            f"supportedAbis={prop('Platforms')}"
            f")"
        )

    @gpdp_logging.log_info(gpdp_logging.SELF_LOGGER, "Authenticating with dispenser")
    async def _auth_dispenser(self):
        res = await self.http.post(
            self.dispenser_url,
            json=self.device,
            headers={ACCEPT: CONTENT_TYPE_JSON, CONTENT_TYPE: CONTENT_TYPE_JSON},
        )
        res.raise_for_status()

        auth: dict[str, Any] = res.json()
        auth_token = auth.get("authToken")
        if not auth_token:
            raise HTTPStatusError("No authToken", request=res.request, response=res)

        self.auth_bundle = AuthBundle(
            auth_token,
            auth.get("userAgentString", self.build_user_agent()),
            auth.get("gsfId", ""),
            auth.get("dfeCookie", ""),
            auth.get("deviceCheckInConsistencyToken"),
            auth.get("deviceConfigToken"),
            auth.get("deviceInfoProvider", {}).get("mccMnc"),
        )

    async def auth_dispenser(self):
        if time.time() < self.last_auth + self.refresh_cooldown:
            return

        async with self.auth_lock:
            if time.time() < self.last_auth + self.refresh_cooldown:
                return

            self.last_auth = int(time.time())
            await self._auth_dispenser()

    def headers(self, accept_language: str = "en-US"):
        optional_headers = {
            "X-DFE-Device-Checkin-Consistency-Token": self.auth_bundle.deviceCheckInConsistencyToken,
            "X-DFE-Device-Config-Token": self.auth_bundle.deviceConfigToken,
            "X-DFE-MCCMNC": self.auth_bundle.mccMnc,
        }
        return {
            AUTHORIZATION: f"Bearer {self.auth_bundle.authToken}",
            USER_AGENT: self.auth_bundle.userAgent,
            "X-DFE-Device-Id": self.auth_bundle.gsfId,
            ACCEPT_LANGUAGE: accept_language,
            "X-DFE-Encoded-Targets": "CAESN/qigQYC2AMBFfUbyA7SM5Ij/CvfBoIDgxXrBPsDlQUdMfOLAfoFrwEHgAcBrQYhoA0cGt4MKK0Y2gI",
            "X-DFE-Phenotype": "H4sIAAAAAAAAAB3OO3KjMAAA0KRNuWXukBkBQkAJ2MhgAZb5u2GCwQZbCH_EJ77QHmgvtDtbv-Z9_H63zXXU0NVPB1odlyGy7751Q3CitlPDvFd8lxhz3tpNmz7P92CFw73zdHU2Ie0Ad2kmR8lxhiErTFLt3RPGfJQHSDy7Clw10bg8kqf2owLokN4SecJTLoSwBnzQSd652_MOf2d1vKBNVedzg4ciPoLz2mQ8efGAgYeLou-l-PXn_7Sna1MfhHuySxt-4esulEDp8Sbq54CPPKjpANW-lkU2IZ0F92LBI-ukCKSptqeq1eXU96LD9nZfhKHdtjSWwJqUm_2r6pMHOxk01saVanmNopjX3YxQafC4iC6T55aRbC8nTI98AF_kItIQAJb5EQxnKTO7TZDWnr01HVPxelb9A2OWX6poidMWl16K54kcu_jhXw-JSBQkVcD_fPsLSZu6joIBAAA",
            "X-DFE-Client-Id": "am-android-google",
            "X-DFE-Network-Type": "4",
            "X-DFE-Content-Filters": "",
            "X-Limit-Ad-Tracking-Enabled": "false",
            "X-Ad-Id": "",
            "X-DFE-UserLanguages": accept_language.replace("-", "_"),
            "X-DFE-Request-Params": "timeoutMs=4000",
            "X-DFE-Cookie": self.auth_bundle.dfeCookie,
            "X-DFE-No-Prefetch": "true",
            **{k: v for k, v in optional_headers.items() if v is not None},
        }
