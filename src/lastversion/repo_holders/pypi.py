"""A module to represent a Pypi project holder."""

import logging

from dateutil import parser

from lastversion.repo_holders.base import BaseProjectHolder
from lastversion.version import Version

log = logging.getLogger(__name__)


class PypiRepoSession(BaseProjectHolder):
    """A class to represent a Pypi project holder."""

    DEFAULT_HOSTNAME = "pypi.org"
    REPO_URL_PROJECT_COMPONENTS = 1
    # For project URLs, e.g. https://pypi.org/project/lastversion/
    # a URI does not start with a repo name, skip '/project/'
    REPO_URL_PROJECT_OFFSET = 1
    CAN_BE_SELF_HOSTED = True

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
            self.hostname = PypiRepoSession.DEFAULT_HOSTNAME
        self.project = self.get_project()

    def release_download_url(self, release, shorter=False):
        """Get release download URL."""
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest project release."""
        pass

    @staticmethod
    def make_canonical_link(repo):
        """Make canonical link for a repo."""
        pass

    def get_canonical_link(self):
        """Get the canonical link for a repo."""
        pass
