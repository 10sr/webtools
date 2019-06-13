"""Config object."""

# from __future__ import annotations

import dataclasses

from typing import Any, Dict

import toml


@dataclasses.dataclass(frozen=True)
class Config:
    """Definitions for configurations that loaded from external at runtime."""

    ENV: str
    SECRET_KEY: str
    ALLOWED_HOST: str
    DATABASE_URL: str
    EXPORT_AS_BOOKMARK_REDIS_URL: str
    USE_X_FORWARDED_HOST: bool = False

    @classmethod
    def from_dict(cls, args: Dict[str, Any]) -> "Config":
        """
        Set up config from dict object.

        :param args: Dict of configuration names and values
        :returns: Config instance
        """
        # Check type explicitly
        for field in dataclasses.fields(cls):
            if field.name in args:
                # print(f"{repr(args[field.name])} -- {repr(field.type)}")
                # When importing `annotations' filed.type is a str of
                # name of type, not the object
                assert isinstance(args[field.name], field.type)
        return cls(**args)

    @classmethod
    def from_toml(cls, filepath: str) -> "Config":
        """
        Set up config from TOML file.

        :param filepath: Input TOML file path
        :returns: Config instance
        """
        with open(filepath) as f:
            obj = toml.load(f)
        return cls.from_dict(obj["webtools"])
