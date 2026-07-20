from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from httpx import AsyncClient


@asynccontextmanager
async def inject(app: FastAPI):
    async with AsyncClient() as client:
        app.state.http_client = client
        yield


def http_client(req: Request) -> AsyncClient:
    return req.app.state.http_client
