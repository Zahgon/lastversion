"""Provides class to represent a WordPress plugin/core project holder."""

import logging

from lastversion.repo_holders.base import BaseProjectHolder
from lastversion.version import Version

log = logging.getLogger(__name__)


class WordPressPluginRepoSession(BaseProjectHolder):
    """A class to represent a WordPress plugin or core project holder."""

    DEFAULT_HOSTNAME = "wordpress.org"
    REPO_URL_PROJECT_COMPONENTS = 1
    # For project URLs, e.g., https://wordpress.org/plugins/opcache-reset/
    # a URI does not start with a repo name, skip '/plugins/'
    REPO_URL_PROJECT_OFFSET = 1

    KNOWN_REPOS_BY_NAME = {
        "wordpress": {"repo": "wordpress"},
    }

    def _get_core_project(self):
        """Fetch WordPress core version info from the version-check API.

        Returns:
            dict: Project dict with name, version, and download_link,
                or None if the API call fails.
        """
        pass

    def get_project(self):
        """Get project JSON data."""
        pass

    def is_instance(self):
        pass

    def __init__(self, repo, hostname=None):
        super().__init__(repo, hostname)
        if hostname:
            self.hostname = hostname
        else:
            self.hostname = WordPressPluginRepoSession.DEFAULT_HOSTNAME
        self.is_core = repo and repo.lower() == "wordpress"
        self.project = self.get_project()

    def release_download_url(self, release, shorter=False):
        """Get release download URL."""
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release for this project."""
        pass

    @staticmethod
    def make_canonical_link(repo):
        """Make canonical link from repo."""
        pass

    def get_canonical_link(self):
        """Get canonical link from repo."""
        pass
