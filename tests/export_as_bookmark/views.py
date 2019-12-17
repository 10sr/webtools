"""View test."""

from unittest import mock

from django.test import TestCase
from django.urls import reverse
from export_as_bookmark.redis import Redis


class ViewTests(TestCase):
    """View test."""
    def _request_get(self, name, *args, **kargs):
        return self.client.get(reverse(f"export_as_bookmark:{name}"), *args, **kargs)

    def _request_post(self, name, *args, **kargs):
        return self.client.post(reverse(f"export_as_bookmark:{name}"), *args, **kargs)

    def test_index(self):
        response = self._request_get("index")
        self.assertEqual(response.status_code, 200)
        return

    @mock.patch.object(Redis, "get_instance")
    def test_post(self, redis_mock):
        body = """http://google.com
http://yahoo.co.jp
"""
        response = self._request_post("post", {"body": body})
        self.assertEqual(response.status_code, 302)
        redis_mock.return_value.set.assert_called_once()
        return
