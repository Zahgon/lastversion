"""Configuration management for lastversion.

Loads configuration from platform-appropriate location and provides access to
settings throughout the application.

Config file locations:
- Linux: ~/.config/lastversion/lastversion.yml
- macOS: ~/Library/Application Support/lastversion/lastversion.yml
- Windows: C:\\Users\\<user>\\AppData\\Local\\lastversion\\lastversion.yml
"""

import copy
import logging
import os
from typing import Any, Dict, Optional

import yaml
from appdirs import user_cache_dir, user_config_dir

log = logging.getLogger(__name__)

# Default configuration values
DEFAULT_CONFIG: Dict[str, Any] = {
    "cache": {
        # Release data cache (stores parsed JSON release data)
        "release_cache": {
            "enabled": False,  # Off by default
            "ttl": 3600,  # 1 hour in seconds when enabled
        },
        # Cache backend: "file" (default) or "redis"
        "backend": "file",
        # File backend settings
        "file": {
            "path": None,  # None = use default appdirs location
            "max_age": 86400,  # Auto-cleanup: delete files older than 24 hours
            "max_size": 104857600,  # 100MB max cache size
        },
        # Redis backend settings (requires lastversion[redis])
        "redis": {
            "url": None,  # e.g., "redis://localhost:6379/0"
            "host": "localhost",
            "port": 6379,
            "db": 0,
            "password": None,
            "key_prefix": "lastversion:",
        },
    }
}

# Singleton instance
_config_instance: Optional["Config"] = None


def deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge two dictionaries, with override taking precedence.

    Args:
        base: Base dictionary with default values.
        override: Dictionary with values to override.

    Returns:
        Merged dictionary.
    """
    pass


class Config:
    """Configuration manager for lastversion.

    Loads configuration from platform-appropriate location and provides
    access to settings. Uses singleton pattern for global access.
    """

    APP_NAME = "lastversion"
    CONFIG_FILENAME = "lastversion.yml"

    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration.

        Args:
            config_path: Optional path to config file. If None, uses default location.
        """
        pass

    def _get_default_config_path(self) -> str:
        """Get the default configuration file path.

        Returns:
            Path to the default config file.
        """
        pass

    def load(self) -> "Config":
        """Load configuration from file.

        Returns:
            Self for chaining.
        """
        pass

    @property
    def config_path(self) -> str:
        """Get the path to the configuration file."""
        pass

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by dot-separated key.

        Args:
            key: Dot-separated key path (e.g., "cache.backend").
            default: Default value if key not found.

        Returns:
            Configuration value or default.
        """
        pass

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value by dot-separated key.

        This only affects the runtime configuration, not the file.

        Args:
            key: Dot-separated key path (e.g., "cache.backend").
            value: Value to set.
        """
        pass

    @property
    def cache_backend(self) -> str:
        """Get the configured cache backend."""
        pass

    @property
    def release_cache_enabled(self) -> bool:
        """Check if release data cache is enabled."""
        pass

    @property
    def release_cache_ttl(self) -> int:
        """Get the release cache TTL in seconds."""
        pass

    @property
    def file_cache_path(self) -> str:
        """Get the file cache path."""
        pass

    @property
    def file_cache_max_age(self) -> int:
        """Get the max age for file cache entries in seconds."""
        pass

    @property
    def file_cache_max_size(self) -> int:
        """Get the max size for file cache in bytes."""
        pass

    @property
    def redis_url(self) -> Optional[str]:
        """Get the Redis URL if configured."""
        pass

    @property
    def redis_host(self) -> str:
        """Get the Redis host."""
        pass

    @property
    def redis_port(self) -> int:
        """Get the Redis port."""
        pass

    @property
    def redis_db(self) -> int:
        """Get the Redis database number."""
        pass

    @property
    def redis_password(self) -> Optional[str]:
        """Get the Redis password."""
        pass

    @property
    def redis_key_prefix(self) -> str:
        """Get the Redis key prefix."""
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Return the full configuration as a dictionary."""
        pass


def get_config(config_path: Optional[str] = None) -> Config:
    """Get the global configuration instance.

    Args:
        config_path: Optional path to config file. Only used on first call.

    Returns:
        The global Config instance.
    """
    pass


def reset_config() -> None:
    """Reset the global configuration instance.

    Useful for testing.
    """
    pass
