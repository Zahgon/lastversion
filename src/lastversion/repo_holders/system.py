"""Version holder based on system package repositories."""

import datetime
import logging

from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)


class SystemRepoSession(BaseProjectHolder):
    """Version holder based on system package repositories."""

    # noinspection PyUnusedLocal
    def __init__(self, repo, hostname=None):
        super().__init__(repo, hostname)

    def dnf_get_available_version(self, pre_ok, major):
        """Get the latest release available via `dnf`."""
        pass

    def yum_get_available_version(self, pre_ok, major):
        """Get the latest release available via `yum`."""
        pass

    def apt_get_available_version(self, pre_ok, major):
        """Get the latest release available via `apt`."""
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass
