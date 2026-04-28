"""Provides a custom argparse action to show the program's version and exit."""

import logging
import sys as _sys
from argparse import SUPPRESS, Action

import lastversion

from .__about__ import __self__, __version__
from .exceptions import ApiCredentialsError

log = logging.getLogger(__name__)


class VersionAction(Action):
    """Custom argparse action to show the program's version and exit."""

    def __init__(self, **kwargs):
        # Set default values if not provided in kwargs
        pass

    def __call__(self, parser, namespace, values, option_string=None):
        pass
