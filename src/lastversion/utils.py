"""Utility functions for lastversion."""

import errno
import io
import logging
import os
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote

import distro
import requests
import tqdm

from lastversion.exceptions import TarPathTraversalException

# Global quiet mode flag - when True, suppresses progress bars and non-error output
QUIET_MODE = False

PY7ZR_AVAILABLE = False
try:
    # noinspection PyUnresolvedReferences
    import py7zr

    PY7ZR_AVAILABLE = True
except ImportError:
    pass

RPM_AVAILABLE = False
try:
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    import rpm

    RPM_AVAILABLE = True
except ImportError:
    pass

DOWNLOAD_TIMEOUT = 30

log = logging.getLogger(__name__)
content_disposition_regex = re.compile(r"filename(?P<priority>\*)?=((?P<encoding>\S+)'')?(?P<filename>[^;]*)")

# matches os.name to known extensions that are meant *mostly* to run on it,
# and not other os.name-s
os_extensions = {
    "nt": (".exe", ".msi", ".msi.asc", ".msi.sha256"),
    "posix": (".tgz", ".tar.gz"),
}

# Extensions exclusive to specific distros as per `distro.id()`
extension_distros = {
    "deb": ["ubuntu", "debian"],
    "rpm": ["rhel", "centos", "fedora", "amazon", "cloudlinux"],
    "apk": ["alpine"],
    "dmg": ["darwin"],
}

# matches *start* of sys.platform value to words in asset name
platform_markers = {
    "win": ["windows", "win"],
    "linux": ["linux"],
    "darwin": ["osx", "darwin"],
    "freebsd": ["freebsd", "netbsd", "openbsd"],
}

# this is all too simple for now
# noinspection SpellCheckingInspection
non_amd64_markers = [
    "i386",
    "i686",
    "arm",
    "arm64",
    "386",
    "ppc64",
    "armv7",
    "armv7l",
    "mips64",
    "ppc64",
    "mips64le",
    "ppc64le",
    "aarch64",
    "armhf",
    "armv7hl",
]

# Markers indicating x86_64/amd64 architecture
x86_64_markers = [
    "x86_64",
    "x86-64",
    "amd64",
    "x64",
]


def is_file_ext_not_compatible_with_os(file_ext):
    """
    Check if the file extension is not compatible with the OS
    Returns:

    """
    pass


def is_asset_name_compatible_with_platform(asset_name):
    """Check if an asset has words that indicate it's not for this platform."""
    pass


def is_not_compatible_to_distro(asset_ext):
    """
    Check if the file extension is not compatible with the current distro.
    The function supports only Linux and OSX distros.
    """
    pass


def is_not_compatible_bitness(asset_name):
    """Check if an asset has words that show it's not meant for this machine's arch.

    On x86_64/AMD64: filters out arm/aarch64/32-bit assets
    On aarch64/arm64: filters out x86_64/amd64 assets
    """
    pass


def asset_does_not_belong_to_machine(asset_name):
    """
    Check if an asset's name contains words that indicate it's not meant for
    this machine

    Args:
        asset_name (str): Base name of asset, e.g. `example.zip`

    Returns:

    """
    pass


def requests_response_patched_enter(self):
    """
    Monkey patching older requests library's response class, so it can use
    context manager.
    See https://github.com/psf/requests/issues/4136
    Args:
        self:

    Returns:

    """
    pass


# noinspection PyUnusedLocal
# pylint: disable=unused-argument
def requests_response_patched_exit(self, *args):
    """Patched exit method for requests.Response"""
    pass


if not hasattr(requests.Response, "__exit__"):
    requests.Response.__enter__ = requests_response_patched_enter
    requests.Response.__exit__ = requests_response_patched_exit


def extract_appimage_desktop_file(appimage_path):
    """Extracts the desktop file from an AppImage

    Args:
        appimage_path (str): Path to the AppImage

    Returns:
        str: Path to the extracted desktop file

    """
    pass


def get_content_disposition_filename(response):
    """Get the preferred filename from the `Content-Disposition` header.

    Examples:
        `attachment; filename="emulation-station-de-2.0.0-x64.deb";
        filename*=UTF-8''emulation-station-de-2.0.0-x64.deb`

    """
    pass


def download_file(url, local_filename=None):
    """Download a URL to the given filename.

    Args:
        url (str): URL to download from
        local_filename (str, optional): Destination filename
            Defaults to current directory plus base name of the URL.
    Returns:
        str: Destination filename, on success

    """
    pass


def check_if_tar_safe(tar_file: tarfile.TarFile) -> bool:
    """CVE-2007-4559"""
    pass


def extract_tar(buffer: io.BytesIO, to_dir):
    """Extract a tar/zip archive to dir.
    If the archive has only one top dir, it will be stripped.
    """
    pass


def extract_zip(buffer: io.BytesIO, to_dir):
    """
    Extract a tar/zip archive to dir.
    If the archive has only one top dir, it will be stripped.
    """
    pass


def detect_archive_type(buffer: io.BytesIO, url: str) -> str:
    """Detect archive type by magic bytes or file extension.

    Args:
        buffer: File buffer to read magic bytes from.
        url: URL to fall back on extension detection.

    Returns:
        Archive type: '7z', 'zip', or 'tar' (for any tar variant).
    """
    pass


def extract_7z(buffer: io.BytesIO, to_dir):
    """
    Extract a 7z archive to dir.
    py7zr maybe hard to strip the top level dir.
    """
    pass


def extract_file(url: str, to_dir="."):
    """Extract an archive from url to dir, stripping the top level dir by default."""
    pass


def rpm_installed_version(name):
    """Get the installed version of a package with the given name.

    Args:
        name (str): Package name

    Returns:
        string: Version of the installed packaged, or None
    """
    pass


def ensure_directory_exists(directory_path):
    """
    Ensure that the given directory exists.
    Workaround for `exist_ok=True` not being available in Python 2.7.

    Args:
        directory_path (str):

    Returns:

    """
    pass
