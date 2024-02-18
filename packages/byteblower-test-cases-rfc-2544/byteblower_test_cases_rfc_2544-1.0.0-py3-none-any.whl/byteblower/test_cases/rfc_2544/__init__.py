"""Perform throughput test based on RFC 2544 using ByteBlower."""
from ._version import version as __version__  # noqa: F401; version info
from .throughput import run
