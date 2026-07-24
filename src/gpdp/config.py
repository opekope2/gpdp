from pathlib import Path

from jproperties import Properties
from pydantic import BaseModel, Field

ENV_CONF = "GPDP_CONF"
DEFAULT_CONF = "gpdp.properties"


def load(file: str):
    props = Properties()
    props.load(Path(file).read_text())
    return Config.model_validate({key: value.data for key, value in props.items()})


class Config(BaseModel):
    dispenser_url: str = Field(alias="dispenser.url")
    dispenser_refresh_cooldown: int = Field(alias="dispenser.refresh_cooldown")
