from pydantic import BaseModel, Field

ENV_DEVICE_CONF = "GPDP_DEVICE_CONF"
DEFAULT_DEVICE_CONF = "device.properties"


class DeviceProperties(BaseModel):
    userreadablename: str = Field(alias="UserReadableName")
    build_bootloader: str = Field(alias="Build.BOOTLOADER")
    build_brand: str = Field(alias="Build.BRAND")
    build_device: str = Field(alias="Build.DEVICE")
    build_fingerprint: str = Field(alias="Build.FINGERPRINT")
    build_hardware: str = Field(alias="Build.HARDWARE")
    build_id: str = Field(alias="Build.ID")
    build_manufacturer: str = Field(alias="Build.MANUFACTURER")
    build_model: str = Field(alias="Build.MODEL")
    build_product: str = Field(alias="Build.PRODUCT")
    build_radio: str = Field(alias="Build.RADIO")
    build_version_release: str = Field(alias="Build.VERSION.RELEASE")
    build_version_sdk_int: str = Field(alias="Build.VERSION.SDK_INT")
    celloperator: str = Field(alias="CellOperator")
    client: str = Field(alias="Client")
    features: str = Field(alias="Features")
    gl_version: str = Field(alias="GL.Version")
    gsf_version: str = Field(alias="GSF.version")
    locales: str = Field(alias="Locales")
    platforms: str = Field(alias="Platforms")
    roaming: str = Field(alias="Roaming")
    screen_density: str = Field(alias="Screen.Density")
    screen_height: str = Field(alias="Screen.Height")
    screen_width: str = Field(alias="Screen.Width")
    sharedlibraries: str = Field(alias="SharedLibraries")
    simoperator: str = Field(alias="SimOperator")
    timezone: str = Field(alias="TimeZone")
    vending_version: str = Field(alias="Vending.version")
    vending_versionstring: str = Field(alias="Vending.versionString")
    gl_extensions: str = Field(alias="GL.Extensions")

    def user_agent(self):
        return (
            f"Android-Finsky/{self.vending_versionstring} ("
            f"api={3},"
            f"versionCode={self.vending_version},"
            f"sdk={self.build_version_sdk_int},"
            f"device={self.build_device},"
            f"hardware={self.build_hardware},"
            f"product={self.build_product},"
            f"platformVersionRelease={self.build_version_release},"
            f"model={self.build_model},"
            f"buildId={self.build_id},"
            f"isWideScreen={0},"
            f"supportedAbis={self.platforms}"
            f")"
        )
