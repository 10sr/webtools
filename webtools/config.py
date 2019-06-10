import os
# TODO: Use dynaconf?
import toml


class Config:
    filepath = None
    # TODO: Define what configs are available
    # TODO: Define default variables here
    def __init__(self):
        self.filepath = os.environ.get("WEBTOOLS_SETTINGS_TOML", "settings.toml")
        with open(self.filepath) as f:
            self.toml = toml.load(f)
        return

    def __getattr__(self, name):
        return self.toml["webtools"][name]

    def get(self, name, default=None):
        try:
            return getattr(self, name)
        except KeyError:
            return default
