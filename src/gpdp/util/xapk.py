from typing import Annotated

from pydantic import BaseModel, Field, PlainSerializer

from gpdp.proto.GooglePlay_pb2 import (
    AndroidAppDeliveryData,
    AppFileMetadata,
    Item,
    SplitDeliveryData,
)

BASE_ID = "base"
BASE_NAME = f"{BASE_ID}.apk"
ICON_NAME = "icon.png"
ICON_NONE = ""
MANIFEST_NAME = "manifest.json"
OBB_TYPE = ["main", "patch"]
OBB_PATH = "Android/obb"
XAPK_VERSION_2 = 2
INSTALL_LOCATION_EXTERNAL_STORAGE = "EXTERNAL_STORAGE"


def split_name(split: SplitDeliveryData):
    return f"split_{split.name}.apk"


def obb_name(package: str, obb: AppFileMetadata):
    return f"{OBB_TYPE[obb.fileType]}.{obb.versionCode}.{package}.obb"


def obb_path(package: str, obb: AppFileMetadata):
    return f"{OBB_PATH}/{package}/{obb_name(package, obb)}"


def create_manifest(app: Item, delivery: AndroidAppDeliveryData, has_icon: bool):
    package = app.id
    details = app.details.appDetails
    splits = [Split(file=split_name(s), id=s.name) for s in delivery.splitDeliveryData]

    return Manifest(
        name=app.title,
        package_name=package,
        version_code=details.versionCode,
        version_name=details.versionString,
        icon=ICON_NAME if has_icon else ICON_NONE,
        total_size=details.infoDownloadSize,
        # min_sdk_version="",  # TODO
        # max_sdk_version="",  # TODO
        # target_sdk_version="",  # TODO
        permissions=list(details.permission),
        split_configs=[s.name for s in delivery.splitDeliveryData],
        split_apks=[Split(file=BASE_NAME, id=BASE_ID), *splits],
        expansions=[
            Expansion(
                file=obb_path(package, f),
                install_location=INSTALL_LOCATION_EXTERNAL_STORAGE,
                install_path=obb_path(package, f),
            )
            for f in delivery.additionalFile
        ],
    )


STRING_SERIALIZER = PlainSerializer(str, return_type=str)


class Expansion(BaseModel):
    file: str
    install_location: str
    install_path: str


class Split(BaseModel):
    file: str
    id: str


# Extracting SDK versions require
# 1. Intercepting the download of base.apk
# 2. Finding the local header for AndroidManifest.xml
# 3. Reading, decompressing, and decoding AndroidManifest.xml
# 4. Padding the manifest bytes for small or missing numbers
class Manifest(BaseModel):
    xapk_version: int = Field(default=XAPK_VERSION_2)
    name: str
    package_name: str
    version_code: Annotated[int, STRING_SERIALIZER]
    version_name: str
    icon: str = Field(default=ICON_NONE)
    total_size: int
    # min_sdk_version: Annotated[int, STRING_SERIALIZER]  # TODO
    # max_sdk_version: Annotated[int, STRING_SERIALIZER]  # TODO
    # target_sdk_version: Annotated[int, STRING_SERIALIZER]  # TODO
    permissions: list[str] = Field(default_factory=list)
    split_configs: list[str] = Field(default_factory=list)
    split_apks: list[Split] = Field(default_factory=list)
    expansions: list[Expansion] = Field(default_factory=list)
