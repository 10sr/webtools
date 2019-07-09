# import unittest

from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def _request_get(self, name, *args, **kargs):
        return self.client.get(reverse(f"lggr:{name}"), *args, **kargs)

    def _request_post(self, name, *args, **kargs):
        return self.client.post(reverse(f"lggr:{name}"), *args, **kargs)

    def test_index(self):
        response = self._request_get("index")
        self.assertEqual(response.status_code, 200)
        return

    def test_get(self):
        response = self._request_get("get", {"key1": "v1", "key2": "value2"})
        self.assertEqual(response.status_code, 200)
        return

    def test_post(self):
        response = self._request_post("post", {"key1": "v1", "key2": "value2"})
        self.assertEqual(response.status_code, 200)
        return
