"""WikiPedia Repo Session."""

import logging

from bs4 import BeautifulSoup
from dateutil import parser

from lastversion.repo_holders.base import BaseProjectHolder

log = logging.getLogger(__name__)


def remove_words(title):
    """Remove words from a title that are not part of the version."""
    pass


class WikipediaRepoSession(BaseProjectHolder):
    """Wikipedia repo session."""

    KNOWN_REPOS_BY_NAME = {
        "alpine": {
            "repo": "Alpine_Linux",
        },
        "rocky": {
            "repo": "Rocky_Linux",
        },
        "rockylinux": {
            "repo": "Rocky_Linux",
        },
        "fedora": {"repo": "Fedora_(operating_system)"},
        "rhel": {"repo": "Red_Hat_Enterprise_Linux"},
        "redhat": {"repo": "Red_Hat_Enterprise_Linux"},
        "almalinux": {"repo": "AlmaLinux"},
        "ios": {"repo": "IOS"},
        "ubuntu": {"repo": "Ubuntu"},
        "debian": {"repo": "Debian"},
        "android": {"repo": "Android_(operating_system)"},
        "windows": {"repo": "Microsoft_Windows"},
        "osx": {"repo": "MacOS"},
        "sles": {"repo": "SUSE_Linux_Enterprise"},
        "opensuse": {"repo": "OpenSUSE"},
    }

    REPO_URL_PROJECT_COMPONENTS = 1
    DEFAULT_HOSTNAME = "en.wikipedia.org"
    # For project URLs, e.g. https://en.wikipedia.org/wiki/Rocky_Linux
    # a URI does not start with a repo name, skip '/wiki/'
    REPO_URL_PROJECT_OFFSET = 1

    def __init__(self, repo, hostname):
        super().__init__(repo, hostname)
        self.hostname = hostname
        if not self.hostname:
            self.hostname = self.DEFAULT_HOSTNAME

    def get_latest(self, pre_ok=False, major=None):
        """Get the latest release."""
        pass
