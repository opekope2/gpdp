from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from httpx import AsyncClient

import gpdp.util.logging as gpdp_logging
from gpdp.services.play_api import PlayApiService


@asynccontextmanager
async def inject(app: FastAPI):
    gpdp_logging.setup()

    async with AsyncClient() as client:
        app.state.http_client = client
        app.state.play_api = PlayApiService(client)
        yield


def http_client(req: Request) -> AsyncClient:
    return req.app.state.http_client


def play_api(req: Request) -> PlayApiService:
    return req.app.state.play_api
