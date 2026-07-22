import dataclasses
import json
import os

ENV_CONF = "GPDP_CONF"
DEFAULT_CONF = "config.json"


def load():
    conf = os.getenv(ENV_CONF, DEFAULT_CONF)
    with open(conf, encoding="utf-8") as conf:
        return Config(**json.load(conf))


@dataclasses.dataclass
class Config:
    dispenser_url: str
    dispenser_refresh_cooldown: int
