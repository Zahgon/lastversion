# -*- coding: utf-8 -*-
# License: BSD, see LICENSE for more details.
"""
This is the main module of lastversion package.
To use it, import it and invoke any function documented here. For example:

```python
from lastversion import lastversion
lastversion.has_update(repo='mautic/mautic', current_version='1.2.3')
```
"""

import argparse
import logging
import os
import re
import shlex
import sys
from os.path import expanduser
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml
from packaging.version import InvalidVersion

from lastversion.ai import generate_changelog
from lastversion.cache import get_release_cache
from lastversion.exceptions import ApiCredentialsError
from lastversion.holder_factory import HolderFactory
from lastversion.repo_holders.test import TestProjectHolder
from lastversion.spdx_id_to_rpmspec import rpmspec_licenses
from lastversion.utils import download_file, extract_appimage_desktop_file, rpm_installed_version
from lastversion.version import Version

log = logging.getLogger(__name__)
FAILS_SEM_ERR_FMT = "Latest version %s fails semantic %s constraint against current version %s"


# noinspection GrazieInspection
def find_preferred_url(spec_urls):
    """
    Given a list of URLs of a project, return preferred one that might lead to version info.
    Basically returns the first URL that matches a handler by matching its primary domain.
    """
    pass


def get_repo_data_from_spec(rpmspec_filename):
    """
    Extracts repo data and CLI args from .spec file

    The project (repo) is specified inside the .spec file
    GitHub repo is resolved via %{upstream_github} + %{name}/%{upstream_name}
    No upstream_github global means that the spec was not prepared for lastversion
    Optional: use of spec_tag macros if the source is from GitHub. In edge cases we check
    new version via GitHub, but prepared sources are elsewhere

    Args:
        rpmspec_filename:

    Returns:

    """
    pass


def get_repo_data_from_yml(repo):
    """Get repo data from YAML file."""
    pass


def latest(
    repo,
    output_format="version",
    pre_ok=False,
    assets_filter=None,
    short_urls=False,
    major=None,
    only=None,
    at=None,
    having_asset=None,
    exclude=None,
    even=False,
    formal=False,
    changelog=False,
    cache_ttl=None,
    skip_release_cache=False,
):
    r"""Find the latest release version for a project.

    Args:
        major (str): Only consider versions which are "descendants" of this
          major version string
        short_urls (bool): Whether we should try to return shorter URLs for
          release data
        assets_filter (Union[str, Pattern]): Regular expression for filtering
          assets for the latest release
        only (str): Only consider tags with this text. Useful for repos with multiple projects.
                    The argument supports negation and regular expressions. To indicate a regex,
                    start it with tilde sign, to negate the expression, start it with exclamation
                    point. See `Examples`.
        repo (str): Repository specifier in any form.
        output_format (str): Affects the return format. Possible values `version`, `json`, `dict`,
                             `assets`, `source`, `tag`.
        pre_ok (bool): Specifies whether pre-releases can be accepted as a newer version.
        at (str): Specifies repo hosting more precisely, only useful if repo argument was
                  specified as one word.
        having_asset (Union[str, bool]): Only consider releases with the given asset.
                                         Pass `True` for any asset
        exclude (str): Only consider releases NOT containing this text/regular expression.
        even (bool): Consider as stable only releases with even minor component, e.g. 1.2.3
        formal (bool): Consider as stable only releases with formal tags set up in Web UI
        changelog (bool): Populate release["changelog"] using upstream notes (if True)
        cache_ttl (int): Optional TTL override for release data cache (seconds).
                         Only used when release cache is enabled in config.
        skip_release_cache (bool): Skip the release data cache entirely (both read and write).
                                   Useful when you need fresh data from the source.

    Examples:
        Find the latest version of Mautic, it is OK to consider betas.

        >>> latest("mautic/mautic", output_format='version', pre_ok=True)
        <Version('4.4.4')>

        Consider only tags without letters:

        >>> latest("openssl/openssl", output_format='version', only=r'!~\w')
        <Version('3.0.7')>

    Returns:
        Union[Version, dict]: Newer version object, if found and `output_format` is `version`.
    Returns:
        str: Single string containing tag, if found and `output_format` is `tag`

    """
    pass


def clear_cache(repo=None):
    """Clear the HTTP cache for lastversion.

    This function is useful for webhook handlers that need to invalidate
    cache when a new release is published.

    Args:
        repo (str): Optional repository identifier (e.g., "owner/repo").
                    If provided, attempts to clear cache for that repo only.
                    If None, clears the entire cache.

    Returns:
        int: Number of cache entries cleared (or 1 for full cache clear)

    Example:
        # In a webhook handler for GitHub release events:
        from lastversion import clear_cache, latest

        def handle_github_webhook(payload):
            repo = payload['repository']['full_name']
            clear_cache(repo)
            # Optionally fetch fresh version
            version = latest(repo, output_format='json')
            return version
    """
    pass


def has_update(repo, current_version, pre_ok=False, at=None):
    """Given an existing version for a repo, checks if there is an update.

    Args:
        repo (str): Repository specifier in any form.
        current_version (str): A version you want to check update for.
        pre_ok (bool): Specifies whether pre-releases can be accepted as a newer version.
        at (str): Specifies repo hosting more precisely, only useful if repo argument was
                  specified as one word.

    Returns:
        Version: Newer version as an object, if found. Otherwise, False

    """
    pass


def check_version(value):
    """Given a version string, raises argparse.ArgumentTypeError if it does not contain any version.
    In lastversion CLI app, this is used as argument parser helper for --newer-than (-gt) option.

    Args:
        value (str): Free-format string which is meant to contain a user-supplied version

    Raises:
        argparse.ArgumentTypeError: Exception in a case version was not found in the input string

    Returns:
        Version: Parsed version object

    """
    pass


def parse_version(tag):
    """
    Parse version to a Version object.
    Argument may not be a version but a URL or a repo name, in which case return False
    E.g., used in lastversion repo-name -gt 1.2.3 (and repo-name is passed here as tag)
    """
    pass


def get_rpm_packager():
    """Get RPM packager name from ~/.rpmmacros"""
    pass


def build_changelog_bullets(res, repo_arg):
    """Build changelog bullets for a release dict using upstream notes and OpenAI.

    Returns:
        list[str] or None
    """
    pass


def update_spec(repo, res, sem="minor", changelog: bool = False):
    pass


def update_spec_commit(spec_file, commit_info, repo_data):
    """Update spec file for commit-based (snapshot) releases.

    Args:
        spec_file: Path to the spec file
        commit_info: Dict with 'sha', 'short_sha', 'date', 'message'
        repo_data: Dict with repo data from spec parsing

    Updates:
        - %global commit <sha>
        - %global commit_date <YYYYMMDD>
        - Release: 0.%{snapinfo}%{?dist} (if no releases) or 1.%{snapinfo}%{?dist}
    """
    pass


def install_app_image(url, install_name):
    """Install an AppImage from a URL to `~/Applications/<install_name>`

    Args:
        url (str): URL where AppImage file is hosted
        install_name (str): Short name that the AppImage will be renamed to
    """
    pass


def install_rpms(res, rpms, args):
    """Install RPMs using package manager"""
    pass
    # if the system has yum, then lastversion has to be installed from yum and
    # has access to system packages like yum python or dnf python API
    # if install_with_dnf(rpms) is False or install_with_yum(rpms) is False:
    #     log.error('Failed talking to either DNF or YUM for package install')
    #     sys.exit(1)


def install_debs(_res, debs, args):
    """Install deb packages using apt.

    Args:
        _res: Release dict (unused, kept for API consistency with install_rpms)
        debs: List of deb package URLs
        args: CLI arguments
    """
    pass


def install_standalone_binary(url, install_name):
    """Install a standalone binary from a URL to `~/Applications/<install_name>`

    Args:
        url (str): URL where the binary file is hosted
        install_name (str): Filename that the binary will be renamed to
    """
    pass


def install_release(res, args):
    """Install latest release.

    Prefers native package formats (RPM/deb) over AppImages for better
    integration with package managers and architecture compatibility.
    """
    pass
