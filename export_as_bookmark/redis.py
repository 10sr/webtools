from urllib.parse import urlparse

import redis

# def _parse_url(url):
#     parsed = urlparse(url)
#     assert parsed.scheme == "redis"
#     host_port = parsed.netloc.split(":")
#     assert len(host_port) == 2
#     host, port = host_port
#     database = parsed.ltrim("/")
#     return (host, port, database)


class Redis:
    __client = None

    def __init__(self, settings):
        self.url = settings.EXPORT_AS_BOOKMARK_REDIS_URL
        return


    @property
    def _client(self):
        if self.__client is None:
            # parsed = _parse_url(self.url)
            # TODO: How to reuse redis client???
            self.__client = redis.Redis.from_url(self.url)
        return self.__client

    def set(self, k, v):
        return self._client.set(k, v)

    def get(self, k):
        return self._client.get(k)
