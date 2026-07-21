from typing import Annotated

from fastapi import Depends, FastAPI, Path, Response, status
from fastapi.responses import HTMLResponse, StreamingResponse

import gpdp.util.dependencies as deps
import gpdp.util.zip as zip
from gpdp.http.headers import CONTENT_DISPOSITION, CONTENT_LENGTH
from gpdp.services.play_api import PlayApiService

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
    version_code: Annotated[int, Path()],
):
    delivery = await play_api.app_delivery(package_id, version_code)
    entries = play_api.xapk_create_entries(package_id, delivery)

    return StreamingResponse(
        content=play_api.xapk_stream_download(delivery, entries),
        media_type=MEDIA_TYPE_ZIP,
        headers={
            CONTENT_LENGTH: str(zip.file_size(entries)),
            CONTENT_DISPOSITION: f'attachment; filename="{package_id}-{version_code}.xapk"',
        },
    )
