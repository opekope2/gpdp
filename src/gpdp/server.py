import asyncio
import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, Path, Response, status
from fastapi.responses import HTMLResponse, StreamingResponse

import gpdp.dependency_injection as deps
from gpdp.http.headers import CONTENT_DISPOSITION, CONTENT_LENGTH, ETAG
from gpdp.services.play_api import PlayApiService
from gpdp.util import xapk, zip
from gpdp.util.zip import FileHeader

MEDIA_TYPE_ZIP = "application/zip"
PACKAGE_ID_PATTERN = r"^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)+$"


app = FastAPI(lifespan=deps.inject)


@app.get("/favicon.ico")
def favicon():
    return Response(status_code=status.HTTP_204_NO_CONTENT)  # TODO


@app.get("/{package_id}")
async def app_info(
    play_api: Annotated[PlayApiService, Depends(deps.play_api)],
    package_id: Annotated[str, Path(pattern=PACKAGE_ID_PATTERN)],
):
    app = await play_api.app_details(package_id)

    version = app.details.appDetails.versionString
    version_code = app.details.appDetails.versionCode

    return HTMLResponse(
        content=f"""
            <span class="version">{version}</span><br>
            <a href="{app.docid}/{version_code}.xapk">Download XAPK</a>
        """
    )


@app.get("/{package_id}/{version_code:int}.xapk")
async def download_xapk(
    play_api: Annotated[PlayApiService, Depends(deps.play_api)],
    package_id: Annotated[str, Path(pattern=PACKAGE_ID_PATTERN)],
    version_code: Annotated[int, Path(gt=0)],
):
    now = datetime.datetime.now()
    app = await play_api.app_details(package_id)
    delivery, icon = await asyncio.gather(
        play_api.app_delivery(package_id, version_code, app),
        play_api.download_icon(app),
    )
    entries = play_api.xapk_create_entries(package_id, delivery, now)
    extra_files: list[bytes] = []

    if icon is not None:
        icon_entry = FileHeader(now, len(icon), xapk.ICON_NAME, b"", "")
        entries.append(icon_entry)
        extra_files.append(icon)

    manifest = (
        xapk.create_manifest(app, delivery, icon is not None)
        .model_dump_json(exclude_defaults=True)
        .encode()
    )
    manifest_entry = FileHeader(now, len(manifest), xapk.MANIFEST_NAME, b"", "")
    entries.append(manifest_entry)
    extra_files.append(manifest)

    return StreamingResponse(
        content=play_api.xapk_stream_download(app, delivery, entries, extra_files),
        media_type=MEDIA_TYPE_ZIP,
        headers={
            CONTENT_LENGTH: str(zip.file_size(entries)),
            CONTENT_DISPOSITION: f'attachment; filename="{package_id}-{version_code}.xapk"',  # noqa: E501
            ETAG: f'"{version_code}"',
        },
    )
