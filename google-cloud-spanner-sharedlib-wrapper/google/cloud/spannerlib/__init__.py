"""Python wrapper for the Spanner Go library."""

import logging
from typing import Final

from google.cloud.spannerlib.connection import Connection

__version__: Final[str] = "0.1.1"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__: list[str] = [
    "Connection",
]
