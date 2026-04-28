"""The base project holder class."""

import datetime
import json
import logging
import os
import platform
import re
import time

import feedparser
import requests
from cachecontrol import CacheControlAdapter
from cachecontrol.caches.file_cache import FileCache
from packaging.version import InvalidVersion

from lastversion.__about__ import __version__
from lastversion.config import get_config

# This class basically corresponds to something (often a website) which holds
# projects (usually a bunch). Often this is a github-like website, so we subclass session
# but this also maybe something special, which either way can be used as a source of version
# information for a project based on its URL or name (see LocalVersionSession)
# it is instantiated with a particular project in mind/set, but also has some methods for
# stuff like searching one
from lastversion.utils import asset_does_not_belong_to_machine, ensure_directory_exists
from lastversion.version import Version

log = logging.getLogger(__name__)


def _safe_open_write(filename, fmode):
    """Open a file for secure write, mirroring CacheControl's behavior without
    relying on its private API.
    """
    pass


class LockAcquireTimeout(Exception):
    """Raised when an internal lock cannot be acquired within timeout."""


def _is_process_alive(pid):
    """Check if a process with given PID is still running.

    Args:
        pid: Process ID to check.

    Returns:
        bool: True if process is alive, False otherwise.
    """
    pass


class InternalTimedDirLock:
    """File-based lock with PID tracking for stale lock detection.

    This lock creates a `.lock` file containing the holder's PID.
    Uses atomic file creation (O_CREAT | O_EXCL) to prevent race conditions.

    If an existing lock is found, the lock checks whether the holding process
    is still alive. If the process is dead (crashed, killed), the stale lock
    is automatically cleaned up and acquisition proceeds.

    This avoids the need for age-based stale lock detection while providing
    robust recovery from process failures.

    Note: Also handles cleanup of old directory-based locks from pre-v3.6.7.
    """

    def __init__(self, path, threaded=True, timeout=None):
        # `path` is the target data file path to be protected
        self.path = path
        self._lock_file = f"{path}.lock"
        self._timeout = 5 if timeout is None else timeout

    def _read_lock_pid(self):
        """Read the PID from an existing lock file.

        Returns:
            int or None: The PID if readable, None otherwise.
        """
        pass

    def _write_lock_file(self):
        """Atomically create lock file with current PID.

        Returns:
            bool: True if lock was acquired, False if already exists.
        """
        pass

    def _cleanup_stale_lock(self):
        """Remove a stale lock from a dead process.

        Handles both:
        - New-style lock files (v3.6.7+)
        - Old-style lock directories (pre-v3.6.7)

        Returns:
            bool: True if stale lock was cleaned up, False otherwise.
        """
        pass

    def __enter__(self):
        deadline = time.time() + self._timeout
        while True:
            if self._write_lock_file():
                break
            # Lock exists - check if holder is still alive
            if self._cleanup_stale_lock():
                # Stale lock cleaned up, try again immediately
                continue
            if time.time() >= deadline:
                raise LockAcquireTimeout(f"Failed to acquire lock for {self.path}")
            time.sleep(0.1)
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            os.remove(self._lock_file)
        except (IOError, OSError):
            pass
        return False


class SafeFileCache(FileCache):
    """FileCache that avoids hanging on lock acquisition by timing out and
    skipping cache writes on lock errors.
    """

    def _write(self, path, data: bytes):
        # Ensure directory exists
        pass


def matches_filter(filter_s, positive, version_s):
    """Check if a version string matches a filter string.

    Args:
        filter_s (str): Filter string.
        positive (bool): Whether filter is positive or negative.
        version_s (str): Version string, often a tag name.

    Returns:
        bool: True if version matches filter, False otherwise.
    """
    pass


class BaseProjectHolder(requests.Session):
    """
    Generic project holder class abstracts a web-accessible project storage.
    E.g., project on GitHub, project on Gitlab, etc.
    A project may not have a name and be identified by a hostname only.
    In that case, the repo property is None.
    Either hostname and/or property have to be present
    """

    # List of odd repos where last char is part of version not beta level
    LAST_CHAR_FIX_REQUIRED_ON = []

    # web-accessible project holders may have a single well-known domain usable by everyone
    # in case of GitHub, that is GitHub.com, for Mercurial web gui - here isn't one, etc.
    DEFAULT_HOSTNAME = None
    SUBDOMAIN_INDICATOR = None
    # E.g., WordPress plugin directory is only one, but Gitea and GitHub can be hosted on arbitrary domains
    CAN_BE_SELF_HOSTED = False
    KNOWN_REPO_URLS = {}
    KNOWN_REPOS_BY_NAME = {}
    # e.g. owner/project, but mercurial just /project together with hostname
    # adapter array should list how many elements make up "repo", e.g. for hg.nginx.com/repo it
    # is only one instead of 2
    # or a "format" specifier for matching
    # 0 means no project name in URI (identified by hostname), 1 means project name is first component, etc.
    # True means as many as given in URI
    REPO_URL_PROJECT_COMPONENTS = 2
    # If URI starts with project name, 0. Otherwise, skip through this many URI dirs

    REPO_URL_PROJECT_OFFSET = 0
    # When a project is identified by whichever URI there is (varying number of components)
    REPO_IS_URI = False
    RELEASE_URL_FORMAT = None
    SHORT_RELEASE_URL_FORMAT = None

    # Instance of project holder itself uniquely identifies a project (noname)
    REPO_IS_HOLDER = False
    DEFAULT_TIMEOUT = 30  # default timeout in seconds

    CACHE_DISABLED = False

    # Conventional changelog file candidates to try at a tag
    CHANGELOG_CANDIDATES = [
        "CHANGELOG.md",
        "CHANGELOG",
        "CHANGES.md",
        "CHANGES",
        "NEWS.md",
        "NEWS",
        "docs/CHANGELOG.md",
        "docs/CHANGES.md",
        "docs/NEWS.md",
    ]

    def repo_changelog(self, tag):
        """Default: no changelog retrieval; subclasses may override."""
        pass

    def repo_changelog_path(self, tag):
        """Default: no changelog path; subclasses may override to return (text, path)."""
        pass

    def collect_release_notes(self, tag, release):
        """Collect release notes text and provenance.

        Returns:
            (text, source): text string or None; source is 'release_body' or a filename path
        """
        pass

    @property
    def name(self):
        """Get project name, useful in URLs for assets, etc."""
        pass

    def __init__(self, name=None, hostname=None):
        super().__init__()
        self.mount("https://", requests.adapters.HTTPAdapter(max_retries=5))
        app_name = __name__.split(".", maxsplit=1)[0]

        # Load configuration
        config = get_config()

        self.cache_dir = None
        self.cache = None
        if not self.CACHE_DISABLED:
            # Use configured cache path or default
            self.cache_dir = config.file_cache_path
            log.info("Using cache directory: %s.", self.cache_dir)
            # Use a lock with a finite timeout to avoid rare hangs on cache writes
            lock_cls = InternalTimedDirLock
            self.cache = SafeFileCache(self.cache_dir, lock_class=lock_cls)
            cache_adapter = CacheControlAdapter(cache=self.cache)
            # noinspection HttpUrlsUsage
            self.mount("http://", cache_adapter)
            self.mount("https://", cache_adapter)
        else:
            log.info("Cache is disabled for this holder.")
            # Still need cache_dir for names_cache_filename even if HTTP cache is disabled
            self.cache_dir = config.file_cache_path

        self.names_cache_filename = f"{self.cache_dir}/repos.json"

        self.user_agent = f"{app_name}/{__version__}"
        self.headers.update({"User-Agent": self.user_agent})
        log.info("Created instance of %s", type(self).__name__)
        self.branches = None
        self.only = None
        self.exclude = None
        self.having_asset = None
        self.hostname = hostname
        if not self.hostname and self.DEFAULT_HOSTNAME:
            self.hostname = self.DEFAULT_HOSTNAME
        # identifies a project on a given hostname
        # normalize repo to number of meaningful parameters
        self.repo = self.get_base_repo_from_repo_arg(name)
        # in some case we do not specify repo, but feed is discovered; no repo is given then
        self.feed_url = None
        self.even = False
        self.formal = False

    def request(self, *args, **kwargs):
        """Set default timeout for requests."""
        pass

    def get_name_cache(self):
        """Return name cache from file."""
        pass

    def update_name_cache(self, cache_data):
        """Update name cache file with new data."""
        pass

    @classmethod
    def clear_cache(cls, repo=None):
        """Clear the HTTP cache and release data cache.

        Args:
            repo: Optional repo identifier. If provided, clears cache only for
                  URLs containing this repo. If None, clears all cache.

        Returns:
            int: Number of cache entries cleared
        """
        pass

    def is_instance(self):
        """Check if project holder is valid instance."""
        pass

    def set_branches(self, branches):
        """Sets project holder's branches."""
        pass

    def set_only(self, only):
        """Sets "only" tag selector for this holder."""
        pass

    def set_exclude(self, exclude):
        """Sets "exclude" tag selector for this holder."""
        pass

    def set_even(self, even):
        """Set to return only releases with even numbering like 1.2.3."""
        pass

    def set_formal(self, formal):
        """Set to return only formally tagged releases."""
        pass

    def set_having_asset(self, having_asset):
        """Sets "having_asset" selector for this holder."""
        pass

    @staticmethod
    def is_link(repo):
        """Check if repo is a link."""
        pass

    @classmethod
    def get_host_repo_for_link(cls, repo):
        """Return hostname and repo from a link."""
        pass

    @classmethod
    def get_base_repo_from_repo_arg(cls, repo_arg):
        """Return meaningful URI components from a repo."""
        pass

    @classmethod
    def is_official_for_repo(cls, repo, hostname):
        """Check if repo is a known repo for this type of project holder."""
        pass

    @classmethod
    def is_matching_hostname(cls, hostname):
        """Check if given hostname matches to the project hosting's domains.

        Args:
            hostname: May include port (netloc format) for non-standard ports.
        """
        pass

    def matches_major_filter(self, version, major):
        """Check if version matches major filter."""
        pass

    def remove_prefix(self, version_s):
        """Remove project name prefix from version string."""
        pass

    def sanitize_version(self, version_s, pre_ok=False, major=None):
        """
        Extract a version from tag name; that satisfies this holder's filters, etc.

        Returns:
            Version or None: The return value can be a Version object or None.
        """
        pass

    def _type(self):
        """Get project holder's class name."""
        pass

    def release_download_url(self, release, shorter=False):
        """Get release download URL."""
        pass

    def get_assets(self, release, short_urls, assets_filter=None):
        """Get assets for a given release."""
        pass

    def get_assets_with_digests(self, release, short_urls, assets_filter=None):
        """Get assets with digest information for a given release.

        Returns a list of dicts with url, name, size, and digest (if available).
        This provides more detailed asset info for JSON output.
        """
        pass

    def get_canonical_link(self):
        """Get the canonical link for a project."""
        pass

    def get_feed_response(self, url):
        """
        Get feed response.
        Ensures that the same `Accept` header is used for all feed requests.
        Clears cookies after request to ensure cache-ability of further requests.
        """
        pass

    def find_release_in_feed(self, url, pre_ok=False, major=None):
        """
        Find release in feed.
        To leverage cachecontrol, we fetch the feed using requests as usual,
        then supply its text to feedparser as a raw string
        """
        pass
