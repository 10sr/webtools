#!/usr/bin/env python3

"""Add next release tag."""

from __future__ import annotations

import enum
import re
import subprocess

import click
import semver


class ReleaseTarget(enum.Enum):
    """Release target type."""

    MAJOR = enum.auto()
    MINOR = enum.auto()
    PATCH = enum.auto()


class Release:
    """Release."""

    __semver: semver.VersionInfo

    def __init__(self, version: str):
        """
        Initialize Release.

        :param version: Version in format like "v1.2.3"
        """
        self.__semver = semver.parse_version_info(re.sub("^v", "", version))
        return

    def __str__(self) -> str:
        """
        Return string.

        :returns: str
        """
        return "v" + str(self.__semver)

    def __repr__(self) -> str:
        """
        Repr.

        :returns: repr
        """
        return f'Release(version="v{str(self.__semver)}")'

    def next(self, target: ReleaseTarget) -> Release:
        """
        Return next release.

        :param target: Target to bump
        :returns: Next Release object
        :raises Exception: Unknown target type
        """
        next_semver: semver.VersionInfo
        if target == ReleaseTarget.MAJOR:
            next_semver = self.__semver.bump_major()
        elif target == ReleaseTarget.MINOR:
            next_semver = self.__semver.bump_minor()
        elif target == ReleaseTarget.PATCH:
            next_semver = self.__semver.bump_patch()
        else:
            raise Exception(f"Unknown target {target}")
        return Release("v" + str(next_semver))


def get_latest_release() -> Release:
    """
    Return latest release object.

    :returns: Latest Release object
    """
    # S603 subprocess call - check for execution of untrusted input.
    # S607 Starting a process with a partial executable path
    proc = subprocess.run(  # noqa: S603,S607
        ["git", "describe", "--tags", "--abbrev=0"], check=True, capture_output=True
    )
    tag = proc.stdout.decode("ascii").strip()
    return Release(tag)


def tag_release(release: Release) -> None:
    """
    Add release tag.

    Currently add tag to HEAD revision.

    :param release: Release object
    """
    cmd = ["git", "tag", "--sign", str(release)]
    # S603 subprocess call - check for execution of untrusted input.
    subprocess.run(cmd, check=True)  # noqa: 603
    return


@click.command()
@click.option("--dryrun", is_flag=True)
@click.option("--major", "target", flag_value=ReleaseTarget.MAJOR)
@click.option("--minor", "target", flag_value=ReleaseTarget.MINOR)
@click.option("--patch", "target", flag_value=ReleaseTarget.PATCH, default=True)
def main(dryrun: bool, target: ReleaseTarget) -> None:
    """
    tag_next_release entrypoint.

    :param dryrun: Dryrun flag
    :param target: Target to bump
    """
    latest = get_latest_release()
    next = latest.next(target)
    print(f"Latest release: {latest}")
    print(f"Next release:   {next}")
    if not dryrun:
        tag_release(next)
    return


main()
