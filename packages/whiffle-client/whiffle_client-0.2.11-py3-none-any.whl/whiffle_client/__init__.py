from whiffle_client.client import Client, CONFIG_FILE_PATH_LOCATIONS
import importlib

__version__ = importlib.metadata.version("whiffle_client")

__all__ = [Client, CONFIG_FILE_PATH_LOCATIONS]
