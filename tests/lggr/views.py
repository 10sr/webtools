# import unittest

from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def _get_client(self, name, *args, **kargs):
        return self.client.get(reverse(f"lggr:{name}"), *args, **kargs)

    def test_index(self):
        response = self._get_client("index")
        self.assertEqual(response.status_code, 200)
        return

    def test_get(self):
        response = self._get_client("get", {"key1": "v1", "key2": "value2"})
        self.assertEqual(response.status_code, 200)
        return
