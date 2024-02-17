import warnings
import importlib.metadata

try:
    __version__ = importlib.metadata.version("pythonji-2")
except importlib.metadata.PackageNotFoundError as e:
    warnings.warn(f"Could not determine version of pythonji-2", stacklevel=1)
    warnings.warn(str(e), stacklevel=1)
    __version__ = "unknown"
