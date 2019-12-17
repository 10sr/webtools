"""Redis test."""

from unittest import mock

from django.test import TestCase
from export_as_bookmark.redis import Redis


class RedisTests(TestCase):
    """Redis test."""

    def test_init(self):
        with self.assertRaises(RuntimeError):
            Redis()
        return
