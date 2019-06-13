"""Redis."""


from typing import Any, Optional, Union
from urllib.parse import urlparse

import redis


# TODO: Use costum storage system?
# https://docs.djangoproject.com/en/2.2/howto/custom-file-storage/
class Redis:
    """
    Communicate with redis server.

    This class is not intended to be instanciated, instead, use class
    method directly.
    """

    __client: Optional[redis.Redis] = None
    url: str

    def __init__(self) -> None:
        """
        Initialize instance.

        This class cannot be instanciated so always raise error when called.

        :raises RuntimeError: Instanciation is not allowed
        """
        raise RuntimeError("Cannot instanciate")

    @classmethod
    def ready(cls, url: str) -> None:
        """
        Set configs for redis connection.

        :param url: str: 

        """
        cls.url = url
        return

    @classmethod
    def _client(cls) -> redis.Redis:
        """
        Return Redis client instance.

        :returns: Redis client instance
        """
        if cls.__client is None:
            cls.__client = redis.Redis.from_url(cls.url)
        return cls.__client

    @classmethod
    # Should use Any for kargs?
    def set(cls, k: str, v: bytes, **kargs: Union[int, str]) -> Any:
        """
        Set key-value pair.

        :param k: Key
        :param v: Value
        :param **kargs: Additional parameters passed to Redis.set method
        :returns: Return from Redis.set
        """
        return cls._client().set(k, v, **kargs)

    @classmethod
    def get(cls, k: str) -> Optional[bytes]:
        """
        Get value of key.

        If key does not eixst or expired, return None.

        :param k: Key
        :returns: Value of k
        """
        ret = cls._client().get(k)
        assert isinstance(ret, bytes) or ret is None
        return ret
