"""Helm Chart repo holder."""

import logging

import yaml

from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)


class HelmChartRepoSession(BaseProjectHolder):
    """Helm Chart repo session."""

    # Any URI identifies a project
    REPO_IS_URI = True

    # noinspection PyUnusedLocal
    def __init__(self, repo, hostname=None):
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass
