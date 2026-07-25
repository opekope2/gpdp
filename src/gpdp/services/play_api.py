import datetime
from collections import deque
from collections.abc import Awaitable, Callable
from http import HTTPMethod

from fastapi import HTTPException, status
from httpx import AsyncClient, Response

from gpdp.http.content_types import (
    CONTENT_TYPE_PROTOBUF,
    CONTENT_TYPE_X_WWW_FORM_URLENCODED,
)
from gpdp.http.headers import ACCEPT, CONTENT_TYPE, COOKIE
from gpdp.proto.GooglePlay_pb2 import AndroidAppDeliveryData, Item, ResponseWrapper
from gpdp.services import play_auth
from gpdp.services.play_auth import PlayAuthService
from gpdp.util import logging, xapk, zip
from gpdp.util.logging import PKG, STATUS
from gpdp.util.zip import FileHeader

FDFE_URL = "https://android.clients.google.com/fdfe"
DETAILS_URL = f"{FDFE_URL}/details"
DELIVERY_URL = f"{FDFE_URL}/delivery"
PURCHASE_URL = f"{FDFE_URL}/purchase"

IMAGE_TYPE_ICON = 4


def icon(app: Item):
    return next(img for img in app.image if img.imageType == IMAGE_TYPE_ICON)


class PlayApiService:
    def __init__(self, http: AsyncClient, auth: PlayAuthService):
        self.http = http
        self.auth = auth
        self.logger = logging.get_logger(self)

    @play_auth.dispenser_error_to_fastapi
    async def request(self, f: Callable[[], Awaitable[Response]]):
        res = await f()
        if res.status_code == status.HTTP_401_UNAUTHORIZED:
            await self.auth.auth_dispenser()
            res = await f()
        if res.status_code == status.HTTP_401_UNAUTHORIZED:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY, detail="Auth token expired"
            )
        return res

    @logging.package_request_info("Getting details")
    async def app_details(self, package: str, locale: str):
        headers = self.auth.headers(locale) | {
            ACCEPT: CONTENT_TYPE_PROTOBUF,
            CONTENT_TYPE: CONTENT_TYPE_PROTOBUF,
        }
        res = await self.request(
            lambda: self.http.get(f"{DETAILS_URL}?doc={package}", headers=headers)
        )
        if res.is_error:
            self.logger.error(
                "Not found", extra={PKG: package, STATUS: res.status_code}
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="App not found"
            )

        response = ResponseWrapper()
        response.ParseFromString(res.content)

        app = response.payload.detailsResponse.item
        if not app.id:
            self.logger.error(
                "Not available", extra={PKG: package, STATUS: res.status_code}
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="App not available"
            )

        return app

    @logging.app_request_info("Purchasing")
    async def purchase(self, app: Item, ver_code: int, locale: str):
        for offer in app.offer:
            if offer.offerType == 1 and offer.micros > 0:
                price = offer.formattedAmount or "paid"
                self.logger.error(
                    "Purchase failed: paid app: %s", price, extra={PKG: app.id}
                )
                raise HTTPException(
                    status_code=status.HTTP_402_PAYMENT_REQUIRED,
                    detail=f"Paid app: {price}",
                )

        headers = self.auth.headers(locale) | {
            ACCEPT: CONTENT_TYPE_PROTOBUF,
            CONTENT_TYPE: CONTENT_TYPE_X_WWW_FORM_URLENCODED,
        }
        data = {"doc": app.id, "ot": 1, "vc": ver_code}

        res = await self.request(
            lambda: self.http.post(PURCHASE_URL, headers=headers, data=data)
        )
        if res.is_success:
            self.logger.info(
                "Purchase successful", extra={PKG: app.id, STATUS: res.status_code}
            )
        else:
            self.logger.warning(
                "Purchase failed", extra={PKG: app.id, STATUS: res.status_code}
            )

    @logging.app_request_info("Delivering")
    async def app_delivery(
        self,
        app: Item,
        ver_code: int,
        locale: str,
        purchased: bool = False,
    ):
        headers = self.auth.headers(locale) | {
            ACCEPT: CONTENT_TYPE_PROTOBUF,
            CONTENT_TYPE: CONTENT_TYPE_PROTOBUF,
        }
        res = await self.request(
            lambda: self.http.get(
                f"{DELIVERY_URL}?doc={app.id}&ot=1&vc={ver_code}", headers=headers
            )
        )
        if res.is_error:
            self.logger.error(
                "Delivery not available", extra={PKG: app.id, STATUS: res.status_code}
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Delivery not available"
            )

        response = ResponseWrapper()
        response.ParseFromString(res.content)
        delivery = response.payload.deliveryResponse.appDeliveryData

        if not delivery.downloadUrl:
            if not purchased:
                await self.purchase(app, ver_code, locale)
                return await self.app_delivery(app, ver_code, locale, purchased=True)

            self.logger.error(
                "Download not available",
                extra={PKG: app.id, STATUS: res.status_code},
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Download not available"
            )

        return delivery

    async def download_icon(self, app: Item):
        # TODO headers
        res = await self.request(lambda: self.http.get(icon(app).imageUrl))
        if res.is_error:
            self.logger.warning(
                "Icon download failed", extra={PKG: app.id, STATUS: res.status_code}
            )
            return

        return res.content

    @logging.package_request_info("Creating XAPK")
    def xapk_create_entries(
        self, package: str, delivery: AndroidAppDeliveryData, now: datetime.datetime
    ):
        base_apk = FileHeader(now, delivery.downloadSize, xapk.BASE_NAME, b"", "")
        split_entries = [
            FileHeader(now, s.downloadSize, xapk.split_name(s), b"", "")
            for s in delivery.splitDeliveryData
        ]
        additional_entries = [
            FileHeader(now, f.size, xapk.obb_path(package, f), b"", "")
            for f in delivery.additionalFile
        ]

        return [base_apk, *split_entries, *additional_entries]

    # TODO gzip
    async def stream_file(
        self, entry: zip.FileHeader, url: str, headers: dict[str, str]
    ):
        yield entry.local_header()

        async with self.http.stream(HTTPMethod.GET, url, headers=headers) as res:
            res.raise_for_status()  # Response has already started so it won't reach the client  # noqa: E501
            async for chunk in res.aiter_bytes():
                entry.update_crc32(chunk)
                yield chunk

        yield entry.data_descriptor()

    async def xapk_stream_download(
        self,
        delivery: AndroidAppDeliveryData,
        entries: list[zip.FileHeader],
        extra_files: list[bytes],
    ):
        cookie = "; ".join(f"{c.name}={c.value}" for c in delivery.downloadAuthCookie)
        headers = {COOKIE: cookie} if cookie else {}

        e = deque(entries)

        async for chunk in self.stream_file(e.popleft(), delivery.downloadUrl, headers):
            yield chunk

        for s in delivery.splitDeliveryData:
            async for chunk in self.stream_file(e.popleft(), s.downloadUrl, headers):
                yield chunk

        for f in delivery.additionalFile:
            async for chunk in self.stream_file(e.popleft(), f.downloadUrl, headers):
                yield chunk

        for f in extra_files:
            entry = e.popleft()

            yield entry.local_header()
            entry.update_crc32(f)
            yield f
            yield entry.data_descriptor()

        for e in entries:
            yield e.central_directory_header(entries)

        yield zip.end_of_central_directory(entries)
