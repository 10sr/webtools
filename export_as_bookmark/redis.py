"""Redis."""

from __future__ import annotations

from typing import Any, ClassVar, Optional, Union, cast
from urllib.parse import urlparse

import redis


# TODO: Use costum storage system?
# https://docs.djangoproject.com/en/2.2/howto/custom-file-storage/
class Redis:
    """Communicate with redis server."""

    __singleton_instance: ClassVar[Optional[Redis]] = None

    def __init__(self) -> None:
        """
        Raise error because this is singleton.

        Use get_instance() instead.

        :raises RuntimeError: Instanciation is not allowed
        """
        raise RuntimeError("Cannot initialize via Constructor")

    @classmethod
    def get_instance(cls) -> Redis:
        """
        Get Redis instance.

        :returns: Instance
        """
        if cls.__singleton_instance is None:
            cls.__singleton_instance = cls.__new__(cls)

        return cls.__singleton_instance

    __client: Optional[redis.Redis] = None
    url: str

    def ready(self, url: str) -> None:
        """
        Set configs for redis connection.

        :param url: str:

        """
        self.url = url
        return

    def _client(self) -> redis.Redis:
        """
        Return Redis client instance.

        :returns: Redis client instance
        """
        if self.__client is None:
            self.__client = cast(
                # Call to untyped function "from_url" of "Redis" in typed context
                redis.Redis,
                redis.Redis.from_url(self.url),  # type: ignore
            )
        return self.__client

    def set(self, k: str, v: bytes, **kargs: Any) -> Any:
        """
        Set key-value pair.

        :param k: Key
        :param v: Value
        :param **kargs: Additional parameters passed to Redis.set method
        :returns: Return from Redis.set
        """
        return self._client().set(k, v, **kargs)

    def get(self, k: str) -> Optional[bytes]:
        """
        Get value of key.

        If key does not eixst or expired, return None.

        :param k: Key
        :returns: Value of k
        """
        ret = self._client().get(k)
        assert isinstance(ret, bytes) or ret is None
        return ret
