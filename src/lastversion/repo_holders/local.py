# special case, private use now
# nginx version is taken as version of stable (written by rpm check script)
# to /usr/local/share/builder/nginx-stable.ver
import logging

from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)


class LocalVersionSession(BaseProjectHolder):
    DEFAULT_HOSTNAME = None

    def __init__(self, repo, hostname):
        pass

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass
