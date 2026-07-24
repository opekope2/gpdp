import pydantic
from pydantic import BaseModel

from gpdp.proto.GooglePlay_pb2 import Item

LINK_PREFIX = "obtainium://app/"


def create_app(url: str, app: Item):
    details = app.details.appDetails
    return App(
        id=app.id,
        url=url,
        author=details.developerName,
        name=app.title,
        preferredApkIndex=0,
        additionalSettings=AdditionalSettings(
            intermediateLink=[],
            customLinkFilterRegex="",
            filterByLinkText=False,
            matchLinksOutsideATags=False,
            skipSort=False,
            reverseSort=False,
            sortByLastLinkSegment=False,
            versionExtractWholePage=True,
            requestHeader=[],  # TODO
            defaultPseudoVersioningMethod="ETag",
            trackOnly=False,
            versionExtractionRegEx=r'<span class="version">(.+?)</span>',
            matchGroupToUse="$1",
            versionDetection=True,
            useVersionCodeAsOSVersion=False,
            apkFilterRegEx="",
            invertAPKFilter=False,
            autoApkFilterByArch=True,
            appName=app.title,
            appAuthor=details.developerName,
            shizukuPretendToBeGooglePlay=False,
            allowInsecure=False,
            exemptFromBackgroundUpdates=False,
            skipUpdateNotifications=False,
            about=app.promotionalDescription,
            refreshBeforeDownload=False,
        ),
    )


class AdditionalSettings(BaseModel):
    intermediateLink: list[str]
    customLinkFilterRegex: str
    filterByLinkText: bool
    matchLinksOutsideATags: bool
    skipSort: bool
    reverseSort: bool
    sortByLastLinkSegment: bool
    versionExtractWholePage: bool
    requestHeader: list[str]
    defaultPseudoVersioningMethod: str
    trackOnly: bool
    versionExtractionRegEx: str
    matchGroupToUse: str
    versionDetection: bool
    useVersionCodeAsOSVersion: bool
    apkFilterRegEx: str
    invertAPKFilter: bool
    autoApkFilterByArch: bool
    appName: str
    appAuthor: str
    shizukuPretendToBeGooglePlay: bool
    allowInsecure: bool
    exemptFromBackgroundUpdates: bool
    skipUpdateNotifications: bool
    about: str
    refreshBeforeDownload: bool


class App(BaseModel):
    id: str
    url: str
    author: str
    name: str
    preferredApkIndex: int
    additionalSettings: AdditionalSettings

    @pydantic.field_serializer("additionalSettings")
    def serialize_additional_settings(self, value: AdditionalSettings):
        return value.model_dump_json()
