"""GitLab repo session."""

import logging
import os
import platform
import re
from datetime import timedelta

from dateutil import parser

from lastversion.exceptions import BadProjectError
from lastversion.repo_holders.base import BaseProjectHolder
from lastversion.utils import asset_does_not_belong_to_machine

log = logging.getLogger(__name__)


class GitLabRepoSession(BaseProjectHolder):
    """GitLab repo session."""

    DEFAULT_HOSTNAME = "gitlab.com"
    CAN_BE_SELF_HOSTED = True
    # Domains gitlab.example.com
    SUBDOMAIN_INDICATOR = "gitlab"

    # GitLab has unlimited nesting in subgroups
    REPO_URL_PROJECT_COMPONENTS = True

    def __init__(self, repo, hostname):
        pass

    def repo_query(self, uri, params=None):
        """Query the repo API."""
        pass

    def ensure_formal_releases_fetched(self):
        """
        Prime cache for dict of recent formal releases
        this fetches /releases and allow quickly look up if a tag is marked as pre-release
        """
        pass

    def get_formal_release_for_tag(self, tag):
        """Get formal release for a given GitLab tag"""
        pass

    def find_gitlab_project_path(self, uri):
        """
        Finds the GitLab project path from a given URL.

        Args:
            uri (str): The GitLab URI.

        Returns:
            str: The path of the project if found, otherwise None.
        """
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass

    def _filter_assets(self, release, assets_filter):
        """Filter and return assets from release."""
        pass

    def get_assets(self, release, short_urls, assets_filter=None):
        """Get assets for a given release."""
        pass

    def get_assets_with_digests(self, release, short_urls, assets_filter=None):
        """Get assets with detailed information for GitLab releases.

        GitLab doesn't provide digests via API, but we include url, name, and size.
        """
        pass

    def release_download_url(self, release, shorter=False):
        """Get release download URL."""
        pass

    def repo_license(self, tag):
        """Get repo license."""
        pass

    def repo_changelog(self, tag):
        """Try to fetch a conventional CHANGELOG/CHANGES/NEWS file at a tag."""
        pass

    def fetch_text_file_at_tag(self, tag: str, path: str) -> str:
        """Fetch text file via GitLab raw endpoint; set Accept for plain text."""
        pass

    def repo_changelog_path(self, tag):
        pass
