from urllib.parse import urlparse

import redis


class Redis:
    __client = None

    def __init__(self, settings):
        self.url = settings.EXPORT_AS_BOOKMARK_REDIS_URL
        return

    @property
    def _client(self):
        if self.__client is None:
            # TODO: How to reuse redis client???
            self.__client = redis.Redis.from_url(self.url)
        return self.__client

    def set(self, k, v):
        return self._client.set(k, v)

    def get(self, k):
        return self._client.get(k)
