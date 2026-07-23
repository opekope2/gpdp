import functools
import time
from asyncio import Lock
from collections.abc import Awaitable, Callable
from typing import Any, Concatenate, ParamSpec, TypeVar

from fastapi import HTTPException, status
from httpx import AsyncClient, HTTPStatusError
from pydantic import BaseModel, Field, ValidationError

from gpdp.config import Config
from gpdp.http.content_types import CONTENT_TYPE_JSON
from gpdp.http.headers import (
    ACCEPT,
    ACCEPT_LANGUAGE,
    AUTHORIZATION,
    CONTENT_TYPE,
    USER_AGENT,
)
from gpdp.util import logging
from gpdp.util.device import DeviceProperties
from gpdp.util.logging import STATUS

P = ParamSpec("P")
R = TypeVar("R")


def dispenser_error_to_fastapi[**P, R](
    func: Callable[Concatenate[Any, P], Awaitable[R]],
):
    @functools.wraps(func)
    async def wrapper(self: Any, *args: P.args, **kwargs: P.kwargs):
        try:
            return await func(self, *args, **kwargs)
        except HTTPStatusError, ValidationError:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY, detail="Dispenser error"
            )

    return wrapper


def log_dispenser_error(func: Callable[[PlayAuthService], Awaitable[None]]):
    async def wrapper(self: PlayAuthService):
        try:
            await func(self)
        except HTTPStatusError as e:
            res = e.response
            err = res.json().get("error")
            self.logger.error(
                "Dispenser error: %s", err, extra={STATUS: res.status_code}
            )
            raise
        except ValidationError as e:
            self.logger.error("Dispenser error: %s", e)
            raise

    return wrapper


class DeviceInfo(BaseModel):
    mccMnc: str | None = Field(alias="mccMnc", default=None)


class AuthBundle(BaseModel):
    auth_token: str = Field(alias="authToken")
    user_agent: str = Field(alias="userAgentString", default="")
    gsf_id: str = Field(alias="gsfId", default="")
    dfe_cookie: str = Field(alias="dfeCookie", default="")
    device_consistency_token: str | None = Field(
        alias="deviceCheckInConsistencyToken", default=None
    )
    device_config_token: str | None = Field(alias="deviceConfigToken", default=None)
    device_info: DeviceInfo = Field(alias="deviceInfoProvider")


class PlayAuthService:
    def __init__(self, http: AsyncClient, config: Config, device: DeviceProperties):
        self.http = http
        self.logger = logging.get_logger(self)
        self.dispenser_url = config.dispenser_url
        self.refresh_cooldown = config.dispenser_refresh_cooldown
        self.device = device
        self.last_auth = 0
        self.auth_lock = Lock()

    @logging.log_info("Authenticating with dispenser")
    @log_dispenser_error
    async def _auth_dispenser(self):
        res = await self.http.post(
            self.dispenser_url,
            json=self.device.model_dump(by_alias=True),
            headers={ACCEPT: CONTENT_TYPE_JSON, CONTENT_TYPE: CONTENT_TYPE_JSON},
        )
        res.raise_for_status()

        self.auth_bundle = AuthBundle.model_validate(res.json())
        if not self.auth_bundle.user_agent:
            self.auth_bundle.user_agent = self.device.user_agent()

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
            "X-DFE-Device-Checkin-Consistency-Token": self.auth_bundle.device_consistency_token,  # noqa: E501
            "X-DFE-Device-Config-Token": self.auth_bundle.device_config_token,
            "X-DFE-MCCMNC": self.auth_bundle.device_info.mccMnc,
        }
        return {
            AUTHORIZATION: f"Bearer {self.auth_bundle.auth_token}",
            USER_AGENT: self.auth_bundle.user_agent,
            "X-DFE-Device-Id": self.auth_bundle.gsf_id,
            ACCEPT_LANGUAGE: accept_language,
            "X-DFE-Encoded-Targets": "CAESN/qigQYC2AMBFfUbyA7SM5Ij/CvfBoIDgxXrBPsDlQUdMfOLAfoFrwEHgAcBrQYhoA0cGt4MKK0Y2gI",  # noqa: E501
            "X-DFE-Phenotype": "H4sIAAAAAAAAAB3OO3KjMAAA0KRNuWXukBkBQkAJ2MhgAZb5u2GCwQZbCH_EJ77QHmgvtDtbv-Z9_H63zXXU0NVPB1odlyGy7751Q3CitlPDvFd8lxhz3tpNmz7P92CFw73zdHU2Ie0Ad2kmR8lxhiErTFLt3RPGfJQHSDy7Clw10bg8kqf2owLokN4SecJTLoSwBnzQSd652_MOf2d1vKBNVedzg4ciPoLz2mQ8efGAgYeLou-l-PXn_7Sna1MfhHuySxt-4esulEDp8Sbq54CPPKjpANW-lkU2IZ0F92LBI-ukCKSptqeq1eXU96LD9nZfhKHdtjSWwJqUm_2r6pMHOxk01saVanmNopjX3YxQafC4iC6T55aRbC8nTI98AF_kItIQAJb5EQxnKTO7TZDWnr01HVPxelb9A2OWX6poidMWl16K54kcu_jhXw-JSBQkVcD_fPsLSZu6joIBAAA",  # noqa: E501
            "X-DFE-Client-Id": "am-android-google",
            "X-DFE-Network-Type": "4",
            "X-DFE-Content-Filters": "",
            "X-Limit-Ad-Tracking-Enabled": "false",
            "X-Ad-Id": "",
            "X-DFE-UserLanguages": accept_language.replace("-", "_"),
            "X-DFE-Request-Params": "timeoutMs=4000",
            "X-DFE-Cookie": self.auth_bundle.dfe_cookie,
            "X-DFE-No-Prefetch": "true",
            **{k: v for k, v in optional_headers.items() if v is not None},
        }
