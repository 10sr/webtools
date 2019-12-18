"""View test."""

from django.test import TestCase
from django.urls import reverse


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
        response = self.client.get("")
        self.assertEqual(response.status_code, 302)
        return
