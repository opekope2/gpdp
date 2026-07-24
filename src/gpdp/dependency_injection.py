import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from httpx import AsyncClient

from gpdp import config
from gpdp.config import DEFAULT_CONF, ENV_CONF
from gpdp.services.play_api import PlayApiService
from gpdp.services.play_auth import PlayAuthService
from gpdp.util import device, logging
from gpdp.util.device import DEFAULT_DEVICE_CONF, ENV_DEVICE_CONF


@asynccontextmanager
async def inject(app: FastAPI):
    logging.setup()
    conf = config.load(os.getenv(ENV_CONF, DEFAULT_CONF))
    dev = device.load(os.getenv(ENV_DEVICE_CONF, DEFAULT_DEVICE_CONF))

    async with AsyncClient(follow_redirects=True) as client:
        app.state.http_client = client
        app.state.play_auth = play_auth = PlayAuthService(client, conf, dev)
        app.state.play_api = PlayApiService(client, play_auth)

        await play_auth.auth_dispenser()  # TODO

        yield


def http_client(req: Request) -> AsyncClient:
    return req.app.state.http_client


def play_auth(req: Request) -> PlayAuthService:
    return req.app.state.play_auth


def play_api(req: Request) -> PlayApiService:
    return req.app.state.play_api
