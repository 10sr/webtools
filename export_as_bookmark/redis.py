from typing import Optional, Any, Union
from urllib.parse import urlparse

import redis


# TODO: Use costum storage system?
# https://docs.djangoproject.com/en/2.2/howto/custom-file-storage/
class Redis:
    __client: Optional[redis.Redis] = None
    url: str

    def __init__(self) -> None:
        raise RuntimeError("Cannot instanciate")

    @classmethod
    def ready(cls, url: str) -> None:
        cls.url = url
        return

    @classmethod
    def _client(cls) -> redis.Redis:
        if cls.__client is None:
            cls.__client = redis.Redis.from_url(cls.url)
        return cls.__client

    @classmethod
    # Should use Any for kargs?
    def set(cls, k: str, v: bytes, **kargs: Union[int, str]) -> Any:
        return cls._client().set(k, v, **kargs)

    @classmethod
    def get(cls, k: str) -> Optional[bytes]:
        ret = cls._client().get(k)
        assert isinstance(ret, bytes) or ret is None
        return ret
