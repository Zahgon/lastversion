"""BitBucket repository session."""

import logging

from dateutil import parser

from lastversion.exceptions import BadProjectError
from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)


class BitBucketRepoSession(BaseProjectHolder):
    """BitBucket repository session."""

    DEFAULT_HOSTNAME = "bitbucket.org"
    CAN_BE_SELF_HOSTED = True
    KNOWN_REPO_URLS = {
        "mmonit.com": {
            "repo": "tildeslash/monit",
            # get URL from the official website because it is a "prepared"
            # source that has the `./configure` script available
            "release_url_format": "https://mmonit.com/{name}/dist/{name}-" "{version}.tar.gz",
        }
    }

    KNOWN_REPOS_BY_NAME = {"monit": KNOWN_REPO_URLS["mmonit.com"]}

    def __init__(self, repo, hostname):
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass

    def _get_latest_from_tags(self, pre_ok=False, major=None):
        """Get the latest release from tags API."""
        pass
