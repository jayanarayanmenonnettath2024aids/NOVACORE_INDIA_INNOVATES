import os
from typing import Any, Dict
import yaml
from loguru import logger
from pydantic import BaseSettings

class EnterpriseConfigLoader:
    """
    Advanced configuration manager for production deployments.
    Supports hierarchical loading from YAML, environment variables, and defaults.
    """
    def __init__(self, env: str = "production"):
        self.env = env
        self.config: Dict[str, Any] = {}
        logger.info(f"EnterpriseConfigLoader initialized for environment: {env}")

    def load_from_yaml(self, path: str):
        """Loads configuration from a YAML file."""
        if not os.path.exists(path):
            logger.warning(f"Config file not found: {path}. Skipping YAML load.")
            return
            
        try:
            with open(path, 'r') as f:
                yaml_data = yaml.safe_load(f)
                self.config.update(yaml_data)
                logger.info(f"Loaded config from {path}")
        except Exception as e:
            logger.error(f"Failed to parse YAML config: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value with nesting support (e.g. 'db.host')."""
        parts = key.split('.')
        val = self.config
        for part in parts:
            if isinstance(val, dict):
                val = val.get(part)
            else:
                return default
        return val if val is not None else default

    def set_override(self, key: str, value: Any):
        """Allows runtime overrides of configuration values."""
        self.config[key] = value
        logger.debug(f"Config override: {key} set to {value}")

config_loader = EnterpriseConfigLoader()
