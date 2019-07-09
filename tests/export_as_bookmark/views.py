# import unittest

from django.test import TestCase

from django.urls import reverse


class ViewTests(TestCase):
    def _request_get(self, name, *args, **kargs):
        return self.client.get(reverse(f"export_as_bookmark:{name}"), *args, **kargs)

    def _request_post(self, name, *args, **kargs):
        return self.client.post(reverse(f"export_as_bookmark:{name}"), *args, **kargs)

    def test_index(self):
        response = self._request_get("index")
        self.assertEqual(response.status_code, 200)
        return

    def test_post(self):
        body = """http://google.com
http://yahoo.co.jp
"""
        # TODO: Mock redis client
        response = self._request_post("post", {"body": body})
        self.assertEqual(response.status_code, 302)
        return
