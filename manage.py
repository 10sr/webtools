#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main() -> None:
    os.environ["DJANGO_SETTINGS_MODULE"] = "webtools.settings"
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    return


if __name__ == "__main__":
    main()
