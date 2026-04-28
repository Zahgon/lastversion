"""Version class for lastversion"""

import re
from datetime import datetime

from packaging.version import InvalidVersion
from packaging.version import Version as PackagingVersion


class Version(PackagingVersion):
    """
    This class abstracts handling of a project's versions. It implements the
    scheme defined in PEP 440. A `Version` instance is comparison-aware and
    can be compared and sorted using the standard Python interfaces.

    This class is descendant from `Version` found in `packaging.version`,
    and implements some additional normalization during instantiation.

    Args:
        version (str): The string representation of a version which will be
                      parsed and normalized before use.
    Raises:
        InvalidVersion: If the `version`` does not conform to PEP 440 in
                        any way, then this exception will be raised.
    """

    # Precompile the regular expressions
    rc_pattern = re.compile(r"^rc(\d+)\.")
    post_pattern = re.compile(r"^p(\d+)$")

    regex_dashed_substitutions = [
        (re.compile(r"-p(\d+)$"), "-post\\1"),
        (re.compile(r"-preview-(\d+)"), "-pre\\1"),
        (re.compile(r"-early-access-(\d+)"), "-alpha\\1"),
        (re.compile(r"-pre-(\d+)"), "-pre\\1"),
        (re.compile(r"-beta[-.]rc(\d+)"), "-beta\\1"),
        (re.compile(r"^pre-(.*)"), "\\1-pre0"),
    ]

    part_to_pypi_dict = {
        "devel": "dev0",
        "test": "dev0",
        "dev": "dev0",
        "alpha": "a0",
        "beta": "b0",
        "rc": "rc0",
        "preview": "rc0",
        "pre": "rc0",
    }

    @staticmethod
    def special_cases_transformation(version):
        """
        Special cases for version transformation.
        " SP-" => ".post" (a Service Pack version is a post release)
        """
        pass

    def fix_letter_post_release(self, match):
        """Fix letter post release"""
        pass

    def is_semver(self):
        """Check if this a (shorthand) semantic version"""
        pass

    @staticmethod
    def part_to_pypi(part):
        """
        Convert a version part to a PyPI compatible string
        See https://peps.python.org/pep-0440/
        Helps devel releases to be correctly identified
        See https://www.python.org/dev/peps/pep-0440/#developmental-releases
        """
        pass

    @staticmethod
    def join_dashed_number_status(version):
        """
        Join status with its number when separated by dash in a version string.
        E.g., 4.27-chaos-preview-3 -> 4.27-chaos-pre3
        Helps devel releases to be correctly identified
        # https://www.python.org/dev/peps/pep-0440/#developmental-releases

        Args:
            version:

        Returns:
            str:
        """
        pass

    def filter_relevant_parts(self, version):
        """
        Filter out irrelevant parts from version string.
        Parse out version components separated by dash.
        """
        pass

    def __init__(self, version, char_fix_required=False):
        """Instantiate the `Version` object.

        Args:
            version (str): The version-like string
            char_fix_required (bool): Should we treat alphanumerics as part of version
        """
        pass

    @property
    def epoch(self):
        # type: () -> int
        """
        An integer giving the version epoch of this Version instance
        """
        pass

    @property
    def release(self):
        """
        A tuple of integers giving the components of the release segment
        of this Version instance; that is, the 1.2.3 part of the version
        number, including trailing zeroes but not including the epoch or
        any prerelease/development/post-release suffixes
        """
        pass

    @property
    def pre(self):
        pass

    @property
    def post(self):
        pass

    @property
    def dev(self):
        pass

    @property
    def local(self):
        pass

    @property
    def major(self):
        # type: () -> int
        pass

    @property
    def minor(self):
        # type: () -> int
        pass

    @property
    def micro(self):
        # type: () -> int
        pass

    @staticmethod
    def is_not_date(num):
        """Helper function to determine if a number is not a date"""
        pass

    @property
    def is_prerelease(self):
        """
        Version is a prerelease if it contains all the following:
        * 90+ micro component
        * no date in micro component

        Returns:
            bool:
        """
        pass

    @property
    def even(self):
        """Check if this is an even minor version"""
        pass

    def sem_extract_base(self, level=None):
        """
        Return Version with desired semantic version level base
        E.g., for 5.9.3 it will return 5.9 (patch is None)
        """
        pass

    def __str__(self):
        # type: () -> str
        pass
