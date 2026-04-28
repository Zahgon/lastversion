"""Factory for holders."""

import logging
from collections import OrderedDict
from urllib.parse import urlparse

from lastversion.exceptions import BadProjectError
from lastversion.repo_holders.alpine import AlpineRepoSession
from lastversion.repo_holders.bibucket import BitBucketRepoSession
from lastversion.repo_holders.feed import FeedRepoSession
from lastversion.repo_holders.gitea import GiteaRepoSession
from lastversion.repo_holders.github import GitHubRepoSession
from lastversion.repo_holders.gitlab import GitLabRepoSession
from lastversion.repo_holders.helmchat import HelmChartRepoSession
from lastversion.repo_holders.local import LocalVersionSession
from lastversion.repo_holders.mercurial import MercurialRepoSession
from lastversion.repo_holders.pypi import PypiRepoSession
from lastversion.repo_holders.sourceforge import SourceForgeRepoSession
from lastversion.repo_holders.system import SystemRepoSession
from lastversion.repo_holders.wikipedia import WikipediaRepoSession
from lastversion.repo_holders.wordpress import WordPressPluginRepoSession

log = logging.getLogger(__name__)


class HolderFactory:
    """
    Holders are order in a way that the ones that can be matched by domain and can't be self-hosted go first
    With the last ones being dynamic (feed lookup, etc.)
    """

    HOLDERS = OrderedDict(
        {
            # non self-hosted
            "wp": WordPressPluginRepoSession,
            "sf": SourceForgeRepoSession,
            "wiki": WikipediaRepoSession,
            "helm_chart": HelmChartRepoSession,
            "alpine": AlpineRepoSession,
            # self-hosted possible, but primary domain exists (or subdomain marker)
            "github": GitHubRepoSession,
            "gitlab": GitLabRepoSession,
            "bitbucket": BitBucketRepoSession,
            "pip": PypiRepoSession,
            "hg": MercurialRepoSession,
            "gitea": GiteaRepoSession,
            # misc
            "website-feed": FeedRepoSession,
            "local": LocalVersionSession,
            "system": SystemRepoSession,
        }
    )

    DEFAULT_HOLDER = "github"

    @staticmethod
    def guess_from_homepage(repo, hostname):
        """
        Try to guess the right holder for a given repo and domain.
        Args:
            repo:
            hostname:

        Returns:

        """
        pass

    @staticmethod
    def create_holder_from_known_repo(known_repo, project_hosting_class):
        """Create a holder from a known repo."""
        pass

    @staticmethod
    def try_match_with_holder_class(project_hosting_name, project_hosting_class, repo, hostname):
        """Try to match a holder class with a given repo."""
        pass

    @staticmethod
    def get_instance_for_repo(repo, at=None):
        """
        Find the right hosting for this repo.
        Go through subclasses to find the one that is holding a given project.
        The repo is either a complete URL or a name allowing to identify a single project.
        """
        pass
