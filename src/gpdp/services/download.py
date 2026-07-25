import zlib
from http import HTTPMethod

from httpx import AsyncClient


class DownloadService:
    def __init__(self, http: AsyncClient):
        self.http = http

    async def stream_bytes(self, url: str, headers: dict[str, str]):
        async with self.http.stream(HTTPMethod.GET, url, headers=headers) as res:
            res.raise_for_status()
            async for chunk in res.aiter_bytes():
                yield chunk

    async def stream_bytes_decompress(self, url: str, headers: dict[str, str]):
        decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)

        async for chunk in self.stream_bytes(url, headers):
            chunk = decompressor.decompress(chunk)
            if chunk:
                yield chunk

        tail = decompressor.flush()
        if tail:
            yield tail
