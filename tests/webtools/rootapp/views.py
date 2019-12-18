"""View test."""

from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    """View test."""

    def _request_get(self, name, reverse_args=None, *args, **kargs):
        return self.client.get(
            reverse(f"rootapp:{name}", args=reverse_args), *args, **kargs
        )

    def _request_post(self, name, reverse_args=None, *args, **kargs):
        return self.client.post(
            reverse(f"rootapp:{name}", args=reverse_args), *args, **kargs
        )

    def test_index(self):
        response = self._request_get("index")
        self.assertEqual(response.status_code, 200)
        return
