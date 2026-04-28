"""Test SourceForge repository."""

from urllib.parse import urlparse, urlunparse

from lastversion.repo_holders.base import BaseProjectHolder


class SourceForgeRepoSession(BaseProjectHolder):
    """SourceForce project holder."""

    REPO_URL_PROJECT_COMPONENTS = 1
    DEFAULT_HOSTNAME = "sourceforge.net"
    # For project URLs, e.g. https://sourceforge.net/projects/keepass/
    # a URI does not start with a repo name, skip '/projects/'
    REPO_URL_PROJECT_OFFSET = 1

    def __init__(self, repo, hostname):
        super().__init__(repo, hostname)
        self.hostname = hostname

    @staticmethod
    def get_normalized_url(download_url):
        """Get normalized URL for a download URL, without /download suffix."""
        pass

    def get_latest(self, pre_ok=False, major=None):
        """
        Get the latest release.
        E.g. https://sourceforge.net/projects/keepass/rss?path=/
        """
        pass

    def release_download_url(self, release, shorter=False):
        """Get download URL for a release."""
        pass
