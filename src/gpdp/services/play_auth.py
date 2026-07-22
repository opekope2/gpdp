import dataclasses
from typing import Any

from httpx import AsyncClient

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

ENV_DISPENSER_URL = "GPDP_DISPENSER_URL"


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
        self.url = config.dispenser_url
        self.refresh_cooldown = config.dispenser_refresh_cooldown
        self.device = device

    async def auth_dispenser(self):
        res = await self.http.post(
            self.url,
            json=self.device,
            headers={ACCEPT: CONTENT_TYPE_JSON, CONTENT_TYPE: CONTENT_TYPE_JSON},
        )
        res.raise_for_status()

        auth: dict[str, Any] = res.json()
        device_info: dict[str, Any] = auth.get("deviceInfoProvider", {})
        authToken = auth.get("authToken")
        userAgent = device_info.get("userAgentString")

        if not authToken or not userAgent:
            raise RuntimeError()  # TODO

        self.auth_bundle = AuthBundle(
            authToken,
            userAgent,
            auth.get("gsfId", ""),
            auth.get("dfeCookie", ""),
            auth.get("deviceCheckInConsistencyToken"),
            auth.get("deviceConfigToken"),
            device_info.get("mccMnc"),
        )

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
            "X-DFE-UserLanguages": "",  # TODO
            "X-DFE-Request-Params": "timeoutMs=4000",
            "X-DFE-Cookie": self.auth_bundle.dfeCookie,
            "X-DFE-No-Prefetch": "true",
            **{k: v for k, v in optional_headers.items() if v is not None},
        }
