#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess

import click
import semver


class Release:
    """Release."""

    __semver: semver.VersionInfo

    def __init__(self, version: str):
        self.__semver = semver.parse_version_info(re.sub("^v", "", version))
        return

    def __str__(self) -> str:
        return "v" + str(self.__semver)

    def __repr__(self) -> str:
        return f"Release(version=\"v{str(self.__semver)}\")"

    def next(self, target: str) -> Release:
        next_semver: semver.VersionInfo
        if target == "major":
            next_semver = self.__semver.bump_major()
        elif target == "minor":
            next_semver = self.__semver.bump_minor()
        elif target == "patch":
            next_semver = self.__semver.bump_patch()
        else:
            raise Exception(f"Unknown target {target}")
        return Release("v" + str(next_semver))


def get_latest_release() -> Release:
    """Return latest release object."""
    proc = subprocess.run(
        ["git", "describe", "--tags", "--abbrev=0"], check=True, capture_output=True
    )
    tag = proc.stdout.decode("ascii").strip()
    return Release(tag)


def tag_release(release: Release):
    cmd = ["git", "tag", "--sign", str(release)]
    subprocess.run(cmd, check=True)
    return


@click.command()
@click.option("--dryrun", is_flag=True)
@click.option("--major", "target", flag_value="major")
@click.option("--minor", "target", flag_value="minor")
@click.option("--patch", "target", flag_value="patch", default=True)
def main(dryrun: bool, target: str):
    """tag_next_release entrypoint."""
    latest = get_latest_release()
    next = latest.next(target)
    print(f"Latest release: {latest}")
    print(f"Next release:   {next}")
    if not dryrun:
        tag_release(next)
    return


main()
