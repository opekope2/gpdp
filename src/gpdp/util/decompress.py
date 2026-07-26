import zlib
from collections.abc import AsyncIterator


async def gzip_stream_decompress(iter: AsyncIterator[bytes]) -> AsyncIterator[bytes]:
    decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)

    async for chunk in iter:
        chunk = decompressor.decompress(chunk)
        if chunk:
            yield chunk

    remaining = decompressor.flush()
    if remaining:
        yield remaining
