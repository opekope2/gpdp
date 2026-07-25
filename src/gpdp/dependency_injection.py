import os
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Header, Request
from httpx import AsyncClient

import gpdp.config
from gpdp.config import DEFAULT_CONF, ENV_CONF, Config
from gpdp.services.download import DownloadService
from gpdp.services.play_api import PlayApiService
from gpdp.services.play_auth import PlayAuthService
from gpdp.util import logging
from gpdp.util.device import DEFAULT_DEVICE_CONF, ENV_DEVICE_CONF, DeviceProperties


@asynccontextmanager
async def inject(app: FastAPI):
    logging.setup()
    conf = gpdp.config.load(os.getenv(ENV_CONF, DEFAULT_CONF), Config)
    dev = gpdp.config.load(
        os.getenv(ENV_DEVICE_CONF, DEFAULT_DEVICE_CONF), DeviceProperties
    )

    async with AsyncClient(follow_redirects=True) as client:
        app.state.config = conf
        app.state.http_client = client
        app.state.download = download = DownloadService(client)
        app.state.play_auth = play_auth = PlayAuthService(client, conf, dev)
        app.state.play_api = PlayApiService(download, play_auth, conf)

        await play_auth.auth_dispenser()  # TODO

        yield


def config(req: Request) -> Config:
    return req.app.state.config


def http_client(req: Request) -> AsyncClient:
    return req.app.state.http_client


def download(req: Request) -> DownloadService:
    return req.app.state.download


def play_auth(req: Request) -> PlayAuthService:
    return req.app.state.play_auth


def play_api(req: Request) -> PlayApiService:
    return req.app.state.play_api


def locale(
    config: Annotated[Config, Depends(config)],
    accept_language: Annotated[str, Header()] = "",
):
    accept_language = accept_language or config.play_default_locale
    return accept_language.split(",")[0].split(";")[0].strip()
