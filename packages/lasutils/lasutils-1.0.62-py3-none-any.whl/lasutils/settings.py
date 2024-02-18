import json
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import yaml

load_dotenv(find_dotenv())


class ConnectorSettings:
    def __init__(self, yaml_file: str):
        self._yaml_file = yaml_file
        self._config = None
        self._secrets = None
        self._settings = self._load_settings(yaml_file)

    def _load_settings(self, yaml_file: str):
        settings = yaml.safe_load(open(Path(yaml_file)).read())
        os.environ["POLLER_CLASS"] = settings["spec"]["class"]
        if settings["spec"].get("config"):
            self._config = settings["spec"]["config"]
            os.environ["CONFIG"] = json.dumps(settings["spec"]["config"])
        if settings["spec"].get("secrets"):
            self._secrets = settings["spec"]["secrets"]
            os.environ["SECRETS"] = json.dumps(settings["spec"]["secrets"])
        return settings

    @property
    def las_user(self):
        return os.getenv("LAS_USER")

    @property
    def las_pwd(self):
        return os.getenv("LAS_PWD")

    @property
    def poller_class(self):
        return self._settings["spec"]["class"]

    @property
    def config(self):
        return self._config

    @property
    def secrets(self):
        return self._secrets


# # LAS Auth
# LAS_USER = os.getenv("LAS_USER")
# LAS_PWD = os.getenv("LAS_PWD")

# # External Auth
# EXT_USER = os.getenv("EXT_USER")
# EXT_PWD = os.getenv("EXT_PWD")

# POLLER_CLASS = os.getenv("POLLER_CLASS")
# CONFIG = json.loads(os.getenv("CONFIG")) if os.getenv("CONFIG") else None
# SECRETS = json.loads(os.getenv("SECRETS")) if os.getenv("SECRETS") else None
