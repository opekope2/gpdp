from gpapi.googleplay_pb2 import AppFileMetadata, Split

BASE_NAME = "base.apk"
OBB_TYPE = ["main", "patch"]


def split_name(split: Split):
    return f"split_{split.name}.apk"


def obb_name(package: str, obb: AppFileMetadata):
    return f"{OBB_TYPE[obb.fileType]}.{obb.versionCode}.{package}.obb"


def obb_path(package: str, obb: AppFileMetadata):
    return f"Android/obb/{package}/{obb_name(package, obb)}"
