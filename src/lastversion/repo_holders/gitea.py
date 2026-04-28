"""Gitea repository session class."""

import json
import logging
import math
import os
import re
import time

from bs4 import BeautifulSoup
from dateutil import parser

from lastversion.exceptions import ApiCredentialsError, BadProjectError
from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)

TOKEN_PRO_TIP = "ProTip: set GITHUB_API_TOKEN env var as per " "https://github.com/dvershinin/lastversion#tips"


def asset_matches(asset, search, regex_matching):
    """Check if the asset equals to string or satisfies a regular expression
    Args:
        asset (dict): asset dict as returned by the API
        search (str): string or regexp to match asset's name or label with
        regex_matching (bool): whether search argument is a regexp
    Returns:
        bool: Whether match is satisfied
    """
    pass


class GiteaRepoSession(BaseProjectHolder):
    """A class to represent a Gitea-based project holder (Gitea, Codeberg, etc.)."""

    DEFAULT_HOSTNAME = "gitea.com"
    # Additional known Gitea-based forges
    KNOWN_HOSTNAMES = ["gitea.com", "codeberg.org"]
    CAN_BE_SELF_HOSTED = True
    """ The following format will benefit from:
    1) not using API, so is not subject to its rate limits
    2) likely has been accessed by someone in CDN and thus faster
    3) provides more or less unique filenames once the stuff is downloaded
    See https://fedoraproject.org/wiki/Packaging:SourceURL#Git_Tags
    We use variation of this: it does not need a parsed version (works for
    --pre better) and it is not broken on fancy release tags like v1.2.3-stable
    https://github.com/OWNER/PROJECT/archive/%{git_tag}/%{git_tag}-%{version}.tar.gz
    """
    RELEASE_URL_FORMAT = "https://{hostname}/{repo}/archive/{tag}.{ext}"
    SHORT_RELEASE_URL_FORMAT = RELEASE_URL_FORMAT

    def find_repo_by_name_only(self, repo):
        """Find repo by name only using Gitea API."""
        pass

    @classmethod
    def is_matching_hostname(cls, hostname):
        """Check if given hostname matches known Gitea-based forges."""
        pass

    def is_instance(self):
        """
        Check if this is a Gitea repo page.
        Navigate to the homepage of project by URL
        Gitea project page will have
        """
        pass

    def __init__(self, repo, hostname):
        pass

    @property
    def rate_limit_url(self):
        """Get the rate limit URL."""
        pass

    def get(self, url, **kwargs):
        """Send GET request and account for GitHub rate limits and such."""
        pass

    def rate_limit(self):
        """Get rate limit info."""
        pass

    def repo_query(self, uri):
        """Query the repo API."""
        pass

    def repo_license(self, tag):
        """Get the license file for a tag."""
        pass

    def repo_readme(self, tag):
        """Get the readme file for a tag."""
        pass

    def get_formal_release_for_tag(self, tag):
        """Get the formal release for a tag, if it exists."""
        pass

    # finding in tags requires paging through ALL of them, because the API does not list them
    # in order of recency, thus this is very slow
    # in: current release to be returned, output: newer release to be returned
    def find_in_tags(self, pre_ok, major):
        """Find the latest release in tags."""
        pass

    def get_latest(self, pre_ok=False, major=None):
        """
        Gets the latest release satisfying "pre-releases are OK" or major/branch constraints
        Strive to fetch formal API release if it exists, because it has useful information
        like assets.
        """
        pass

    def set_matching_formal_release(self, ret, formal_release, version, pre_ok, data_type="release"):
        """Set the current release selection to this formal release if matching conditions."""
        pass

    def try_get_official(self, repo):
        """Check the existence of repo/repo

        Returns:
            str: updated repo
        """
        pass
