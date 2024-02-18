"""A game of chess."""

from importlib.metadata import PackageNotFoundError, version
from importlib.util import find_spec
from pathlib import Path

__version__: str | None

try:
    __version__ = version("pychesstools")
except PackageNotFoundError:
    __version__ = None

WORKING_DIRECTORY = Path(__file__).parent
RICH_AVAILABLE = bool(find_spec("rich"))
