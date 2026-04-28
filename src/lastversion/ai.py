"""OpenAI-powered helpers for generating RPM changelog summaries.

This module intentionally uses only OpenAI's API (no local heuristics) to
summarize upstream release notes into concise bullets suitable for RPM
%changelog entries.
"""

import json
import logging
import os
from typing import List, Optional

import requests

log = logging.getLogger(__name__)


def _get_openai_api_key() -> Optional[str]:
    pass


def _get_openai_model() -> str:
    pass


def generate_changelog(raw_notes: str, context: dict) -> Optional[List[str]]:
    """Generate a concise bullet list from upstream release notes using OpenAI.

    Args:
        raw_notes: Upstream release notes/description (markdown/plain).
        context: Minimal context like {"repo": str, "tag": str, "version": str}.
        bullets: Target number of bullets (3-7 permitted).

    Returns:
        List of bullet strings (without leading dashes), or None on failure.
    """
    pass
