"""View test."""

from unittest import mock

from django.test import TestCase
from django.urls import reverse
from export_as_bookmark.redis import Redis


class ViewTests(TestCase):
    """View test."""

    def _request_get(self, name, reverse_args=None, *args, **kargs):
        return self.client.get(
            reverse(f"export_as_bookmark:{name}", args=reverse_args), *args, **kargs
        )

    def _request_post(self, name, reverse_args=None, *args, **kargs):
        return self.client.post(
            reverse(f"export_as_bookmark:{name}", args=reverse_args), *args, **kargs
        )

    def test_index(self):
        response = self._request_get("index")
        self.assertEqual(response.status_code, 200)
        return

    @mock.patch.object(Redis, "get_instance")
    def test_post(self, redis_mock):
        body = """http://google.com
http://yahoo.co.jp
"""
        response = self._request_post("post", None, {"body": body})
        self.assertEqual(response.status_code, 302)
        redis_mock.return_value.set.assert_called_once()
        return

    @mock.patch.object(Redis, "get_instance")
    def test_done(self, redis_mock):
        redis_mock.return_value.pttl.return_value = 1

        response = self._request_get("done", ("12345", "export-name"))
        self.assertEqual(response.status_code, 200)
        redis_mock.return_value.pttl.assert_called_once_with("12345")
        return

    @mock.patch.object(Redis, "get_instance")
    def test_download(self, redis_mock):
        redis_mock.return_value.get.return_value = b"hoehoe"

        response = self._request_get("download", ("12345", "export-name"))
        self.assertEqual(response.status_code, 200)
        redis_mock.return_value.get.assert_called_once_with("12345")
        return

    @mock.patch.object(Redis, "get_instance")
    def test_download_404(self, redis_mock):
        redis_mock.return_value.get.return_value = None

        # TODO: Supress WARNING:django.request:Not Found: warning
        response = self._request_get("download", ("12345", "export-name"))
        self.assertEqual(response.status_code, 404)
        redis_mock.return_value.get.assert_called_once_with("12345")
        return
