import datetime
import operator
from collections import deque

from fastapi import HTTPException, status
from gpapi.googleplay import CONTENT_TYPE_PROTO, DELIVERY_URL, DETAILS_URL, PURCHASE_URL
from gpapi.googleplay_pb2 import AndroidAppDeliveryData, DocV2, ResponseWrapper
from httpx import AsyncClient

import gpdp.util.logging as gpdp_logging
import gpdp.util.xapk as xapk
import gpdp.util.zip as zip
from gpdp.http.headers import ACCEPT, CONTENT_TYPE, COOKIE
from gpdp.util.logging import PKG
from gpdp.util.zip import FileHeader

CONTENT_TYPE_X_WWW_FORM_URLENCODED = "application/x-www-form-urlencoded"


def get_auth_headers(accept_language: str = "en-US"):
    raise NotImplementedError()


class PlayApiService:
    def __init__(self, http: AsyncClient):
        self.http = http
        self.logger = gpdp_logging.get_logger(self)

    @gpdp_logging.package_request_info(operator.attrgetter("logger"), "Getting details")
    async def app_details(self, package: str):
        headers = get_auth_headers() | {
            ACCEPT: CONTENT_TYPE_PROTO,
            CONTENT_TYPE: CONTENT_TYPE_PROTO,
        }
        res = await self.http.get(f"{DETAILS_URL}?doc={package}", headers=headers)
        if res.is_error:
            self.logger.error("Not found (%s)", res.status_code, extra={PKG: package})
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="App not found"
            )

        response = ResponseWrapper()
        response.ParseFromString(res.content)

        app = response.payload.detailsResponse.docV2
        if not app.docid:
            self.logger.error("Not available", extra={PKG: package})
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="App not available"
            )

        return app

    @gpdp_logging.package_request_info(operator.attrgetter("logger"), "Purchasing")
    async def purchase(self, package: str, app: DocV2):
        for offer in app.offer:
            if offer.offerType == 1 and offer.micros > 0:
                price = offer.formattedAmount or "paid"
                self.logger.error(
                    "Purchase failed: paid app: %s", price, extra={PKG: package}
                )
                raise HTTPException(
                    status_code=status.HTTP_402_PAYMENT_REQUIRED,
                    detail=f"Paid app: {price}",
                )

        headers = get_auth_headers() | {
            ACCEPT: CONTENT_TYPE_PROTO,
            CONTENT_TYPE: CONTENT_TYPE_X_WWW_FORM_URLENCODED,
        }
        data = {"doc": package, "ot": 1, "vc": app.details.appDetails.versionCode}

        res = await self.http.post(PURCHASE_URL, headers=headers, data=data)
        if res.is_success:
            self.logger.info("Purchase successful", extra={PKG: package})
        else:
            self.logger.warning(
                "Purchase failed: %s", res.status_code, extra={PKG: package}
            )

    @gpdp_logging.package_request_info(operator.attrgetter("logger"), "Delivering")
    async def app_delivery(self, package: str, ver_code: int, purchased: bool = False):
        headers = get_auth_headers() | {
            ACCEPT: CONTENT_TYPE_PROTO,
            CONTENT_TYPE: CONTENT_TYPE_PROTO,
        }
        res = await self.http.get(
            f"{DELIVERY_URL}?doc={package}&ot=1&vc={ver_code}", headers=headers
        )
        if res.is_error:
            self.logger.error(
                "Delivery not available: %s", res.status_code, extra={PKG: package}
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Delivery not available"
            )

        response = ResponseWrapper()
        response.ParseFromString(res.content)
        delivery = response.payload.deliveryResponse.appDeliveryData

        if not delivery.downloadUrl:
            if not purchased:
                app = await self.app_details(package)
                await self.purchase(package, app)
                return await self.app_delivery(package, ver_code, purchased=True)

            self.logger.error(
                "Download not available: %s", res.status_code, extra={PKG: package}
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Download not available"
            )

        return delivery

    @gpdp_logging.package_request_info(operator.attrgetter("logger"), "Creating XAPK")
    def xapk_create_entries(self, package: str, delivery: AndroidAppDeliveryData):
        now = datetime.datetime.now()

        base_apk = FileHeader(now, delivery.downloadSize, xapk.BASE_NAME, b"", "")
        split_entries = [
            FileHeader(now, s.size, xapk.split_name(s), b"", "") for s in delivery.split
        ]
        additional_entries = [
            FileHeader(now, f.size, xapk.OBB_PATH + xapk.obb_name(package, f), b"", "")
            for f in delivery.additionalFile
        ]

        # TODO icon, manifest
        return [base_apk, *split_entries, *additional_entries]

    # TODO gzip
    async def stream_file(
        self, entry: zip.FileHeader, url: str, headers: dict[str, str]
    ):
        yield entry.local_header()

        async with self.http.stream("GET", url, headers=headers) as res:
            res.raise_for_status()  # TODO
            async for chunk in res.aiter_bytes():
                entry.update_crc32(chunk)
                yield chunk

        yield entry.data_descriptor()

    async def xapk_stream_download(
        self, delivery: AndroidAppDeliveryData, entries: list[zip.FileHeader]
    ):
        cookie = "; ".join(f"{c.name}={c.value}" for c in delivery.downloadAuthCookie)
        headers = get_auth_headers() | {
            ACCEPT: CONTENT_TYPE_PROTO,
            CONTENT_TYPE: CONTENT_TYPE_PROTO,
            COOKIE: cookie,
        }

        e = deque(entries)

        async for chunk in self.stream_file(e.popleft(), delivery.downloadUrl, headers):
            yield chunk

        for s in delivery.split:
            # TODO check download
            async for chunk in self.stream_file(e.popleft(), s.downloadUrl, headers):
                yield chunk

        for f in delivery.additionalFile:
            # TODO check download
            async for chunk in self.stream_file(e.popleft(), f.downloadUrl, headers):
                yield chunk

        # TODO icon, manifest

        for e in entries:
            yield e.central_directory_header(entries)

        yield zip.end_of_central_directory(entries)
