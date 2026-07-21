from jproperties import Properties

ENV_DEVICE_CONF = "GPDP_DEVICE_CONF"
DEFAULT_DEVICE_CONF = "device.properties"


def load(file: str):
    with open(file, "rb") as f:
        props = Properties()
        props.load(f)
        return {key: value.data for key, value in props.items()}
