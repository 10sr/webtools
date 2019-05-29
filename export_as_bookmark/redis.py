from urllib.parse import urlparse
from typing import Optional

import redis


class Redis:
    __client = None
    url: str

    def __init__(self):
        raise RuntimeError("Cannot instanciate")

    @classmethod
    def ready(cls, settings):
        cls.url = settings.EXPORT_AS_BOOKMARK_REDIS_URL
        return

    @classmethod
    def _client(cls):
        if cls.__client is None:
            cls.__client = redis.Redis.from_url(cls.url)
        return cls.__client

    @classmethod
    def set(cls, k: str, v: bytes, **kargs):
        return cls._client().set(k, v, **kargs)

    @classmethod
    def get(cls, k: str) -> Optional[bytes]:
        return cls._client().get(k)
