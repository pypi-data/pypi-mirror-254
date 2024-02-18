import logging
import dataclasses
import enum
from typing import Any
import yaml
from home_link.models import Device


class ConfigKey(enum.Enum):
    LOG_LEVEL = "log_level"
    HTTP_SERVER = "http_server"
    FIREBASE = "firebase"
    DEVICES = "devices"


@dataclasses.dataclass
class HttpServerConfig:
    host: str = "127.0.0.1"
    port: int = "80"
    username: str = None
    password: str = None


@dataclasses.dataclass
class FirebaseConfig:
    cert_json: str = "home-link_firebase.json"


class Config:
    CONFIG_FILENAME = "config.yaml"
    DEVICE_FILENAME = "device_{}.toml"

    _instance = None

    log_level = "INFO"
    http_server: HttpServerConfig = None
    firebase: FirebaseConfig = None
    devices: dict[str, Device] = {}

    def __init__(self) -> None:
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._read_toml(cls._instance)
        return cls._instance

    def _read_toml(self):
        logging.info("load configuration")
        try:
            with open(self.CONFIG_FILENAME, "r") as file_config:
                config_obj: dict[str, Any] = yaml.safe_load(file_config)
                if ConfigKey.LOG_LEVEL.value in config_obj:
                    self.log_level = config_obj.get(ConfigKey.LOG_LEVEL.value).upper()
                if ConfigKey.HTTP_SERVER.value in config_obj:
                    try:
                        self.http_server = HttpServerConfig(**config_obj.get(ConfigKey.HTTP_SERVER.value))
                    except TypeError:
                        self.http_server = HttpServerConfig()
                if ConfigKey.FIREBASE.value in config_obj:
                    try:
                        self.firebase = FirebaseConfig(**config_obj.get(ConfigKey.FIREBASE.value))
                    except TypeError:
                        self.firebase = FirebaseConfig()
                if ConfigKey.DEVICES.value in config_obj:
                    try:
                        self.devices = {
                            str(device.get("name")): Device(**device)
                            for device in config_obj.get(ConfigKey.DEVICES.value)
                        }
                    except:
                        raise Exception("error configuration, illegal arguments in section devices!")
                else:
                    logging.info("no devices found!")
        except FileNotFoundError:
            pass
