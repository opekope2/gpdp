from typing import Annotated

from fastapi import FastAPI, Path, Response
from fastapi.responses import PlainTextResponse

from gpdp.util.di import inject
from gpdp.util.streamed_zip import (
    FileHeader,
    end_of_central_directory,
    zip_file_size,
)

MEDIA_TYPE_APK = "application/vnd.android.package-archive"
MEDIA_TYPE_ZIP = "application/zip"


def get_download_headers(entries: list[FileHeader]):
    return {
        "Content-Size": str(zip_file_size(entries)),
        "Content-Disposition": "attachment",
    }


app = FastAPI(lifespan=inject)


@app.get("/favicon.ico")
def favicon():
    return Response(status_code=404)  # TODO


@app.get("/{package_id}")
async def app_info(package_id: Annotated[str, Path()]):
    return PlainTextResponse(f"Package {package_id}")


@app.get("/download/{package_id}-{version}.apk")
async def download_apk(package_id: Annotated[str, Path()]):
    return Response(
        content=end_of_central_directory([]),
        media_type=MEDIA_TYPE_APK,
        headers=get_download_headers([]),
    )


@app.get("/download/{package_id}-{version}.apks")
async def download_apks(package_id: Annotated[str, Path()]):
    return Response(
        content=end_of_central_directory([]),
        media_type=MEDIA_TYPE_ZIP,
        headers=get_download_headers([]),
    )


@app.get("/download/{package_id}-{version}.xapk")
async def download_xapk(package_id: Annotated[str, Path()]):
    return Response(
        content=end_of_central_directory([]),
        media_type=MEDIA_TYPE_ZIP,
        headers=get_download_headers([]),
    )
