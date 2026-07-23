from gpapi.googleplay_pb2 import AndroidAppDeliveryData, AppFileMetadata, DocV2
from gpapi.googleplay_pb2 import Split as SplitAPK
from pydantic import BaseModel

BASE_ID = "base"
BASE_NAME = f"{BASE_ID}.apk"
ICON_NAME = "icon.png"
MANIFEST_NAME = "manifest.json"
OBB_TYPE = ["main", "patch"]
OBB_PATH = "Android/obb"
INSTALL_LOCATION_EXTERNAL_STORAGE = "EXTERNAL_STORAGE"


def split_name(split: SplitAPK):
    return f"split_{split.name}.apk"


def obb_name(package: str, obb: AppFileMetadata):
    return f"{OBB_TYPE[obb.fileType]}.{obb.versionCode}.{package}.obb"


def obb_path(package: str, obb: AppFileMetadata):
    return f"{OBB_PATH}/{package}/{obb_name(package, obb)}"


def create_manifest(app: DocV2, delivery: AndroidAppDeliveryData, has_icon: bool):
    package = app.docid
    details = app.details.appDetails
    splits = [Split(file=split_name(s), id=s.name) for s in delivery.split]

    return Manifest(
        xapk_version=2,
        name=app.title,
        package_name=package,
        version_code=str(details.versionCode),
        version_name=details.versionString,
        icon=ICON_NAME if has_icon else None,
        total_size=details.installationSize,
        # min_sdk_version="",  # TODO
        # max_sdk_version="",  # TODO
        # target_sdk_version="",  # TODO
        permissions=list(details.permission),
        split_configs=[s.name for s in delivery.split],
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


class Expansion(BaseModel):
    file: str
    install_location: str
    install_path: str


class Split(BaseModel):
    file: str
    id: str


class Manifest(BaseModel):
    xapk_version: int
    name: str
    package_name: str
    version_code: str
    version_name: str
    icon: str | None
    total_size: int
    # min_sdk_version: str  # TODO
    # max_sdk_version: str  # TODO
    # target_sdk_version: str  # TODO
    permissions: list[str]
    split_configs: list[str]
    split_apks: list[Split]
    expansions: list[Expansion]
