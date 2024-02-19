"""Module init."""

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

__version__ = importlib.metadata.version("chris")

__all__ = [
    "__version__",
]
