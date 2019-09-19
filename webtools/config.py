"""Config object."""

from __future__ import annotations

import dataclasses

from typing import Any, Dict, Optional, get_type_hints

import toml
import typeguard


@dataclasses.dataclass(frozen=True)
class Config:
    """Definitions for configurations that will be loaded at runtime."""

    SECRET_KEY: str
    ALLOWED_HOST: str
    DATABASE_URL: str
    EXPORT_AS_BOOKMARK_REDIS_URL: str

    DEBUG: bool = False
    USE_X_FORWARDED_HOST: bool = False
    SEMANTICUI_BASE_DIR: str = ".smanticui_static/"

    # Static Configurations
    STATIC_URL: str = "/webtools/static/"
    USE_S3: bool = False
    # S3
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_STORAGE_BUCKET_NAME: Optional[str] = None
    AWS_DEFAULT_ACL: Optional[str] = "public-read"
    AWS_BUCKET_ACL: Optional[str] = "public-read"
    AWS_AUTO_CREATE_BUCKET: bool = True
    AWS_S3_ENDPOINT_URL: Optional[str] = None
    # AWS_S3_CUSTOM_DOMAIN: Optional[str] = None
    # Local Filesystem
    STATIC_ROOT: str = "static_deploy/webtools/static/"

    # Non default but required to pass
    # manage.py check --deploy --fail-level WARINING
    SECURE_HSTS_SECONDS: int = 3600  # 1 hour
    SECURE_HSTS_INCLUDE_SUBDOMAINS: bool = True
    SECURE_HSTS_PRELOAD: bool = True

    SECURE_CONTENT_TYPE_NOSNIFF: bool = True
    SECURE_BROWSER_XSS_FILTER: bool = True
    SECURE_SSL_REDIRECT: bool = True
    SESSION_COOKIE_SECURE: bool = True
    CSRF_COOKIE_SECURE: bool = True
    X_FRAME_OPTIONS: str = "DENY"
    SECURE_REFERRER_POLICY: str = "no-referrer-when-downgrade"

    WEBTOOLS_REVISION_FILEPATH: Optional[str] = "HEAD.txt"

    def __post_init__(self) -> None:
        """Conduct explicit type check."""
        # When importing `annotations' filed.type is a str of
        # name of type, not the object
        # This get_type_hints call fails to type-check, but actually
        # it is acceptable.
        # > error: Argument 1 to "get_type_hints" has incompatible type "Config"; expected "Callable[..., Any]"
        types = get_type_hints(self, globals())  # type: ignore
        for field in dataclasses.fields(self):
            typeguard.check_type(
                field.name, getattr(self, field.name), types[field.name]
            )
        return

    @classmethod
    def from_dict(cls, args: Dict[str, Any]) -> Config:
        """
        Set up config from dict object.

        :param args: Dict of configuration names and values
        :returns: Config instance
        """
        return cls(**args)

    @classmethod
    def from_toml(cls, filepath: str, section: str) -> Config:
        """
        Set up config from TOML file.

        :param filepath: Input TOML file path
        :param section: Section name in TOML file
        :returns: Config instance
        """
        with open(filepath) as f:
            obj = toml.load(f)
        return cls.from_dict(obj[section])
