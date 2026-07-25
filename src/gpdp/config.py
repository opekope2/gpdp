from pathlib import Path
from typing import TypeVar

from jproperties import Properties
from pydantic import BaseModel, Field

ENV_CONF = "GPDP_CONF"
DEFAULT_CONF = "gpdp.properties"

T = TypeVar("T")


def load[T: BaseModel](file: str, config_class: type[T]):
    props = Properties()
    props.load(Path(file).read_text())
    return config_class.model_validate(
        {key: value.data for key, value in props.items()}
    )


class Config(BaseModel):
    dispenser_refresh_cooldown: int = Field(alias="dispenser.refresh_cooldown")
    dispenser_url: str = Field(alias="dispenser.url")
    add_to_obtainium: bool = Field(alias="obtainium.auto_add")
    play_download_compressed: bool = Field(alias="play.download.compressed")
    play_default_locale: str = Field(alias="play.locale.default")
