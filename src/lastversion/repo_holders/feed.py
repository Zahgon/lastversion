"""FeedRepoSession class."""

import datetime
import logging
from urllib.parse import urljoin

import feedparser

from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)


class FeedRepoSession(BaseProjectHolder):
    """Feed repo session."""

    KNOWN_REPOS_BY_NAME = {
        "filezilla": {
            "repo": "filezilla",
            "hostname": "filezilla-project.org",
            "only": "FileZilla Client",
        }
    }
    CAN_BE_SELF_HOSTED = True
    # Unlimited number of components (URI as is)
    REPO_IS_URI = True

    # https://alex.miller.im/posts/python-3-feedfinder-rss-detection-from-url/
    def find_feed(self, site):
        """Find the feed for a given site"""
        pass

    def __init__(self, repo, hostname):
        super().__init__(repo, hostname)
        self.home_soup = None
        feeds = self.find_feed("https://" + hostname + "/")
        if not feeds:
            return
        self.hostname = hostname
        log.info("Using feed URL: %s", feeds[0])
        self.feed_url = feeds[0]

    def is_instance(self):
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass
