"""launchpad-client base file."""

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("launchpad-client")
    except PackageNotFoundError:
        __version__ = "dev"

from . import errors
from .errors import LaunchpadError
from .launchpad import Launchpad
from .models import LaunchpadObject, RecipeType, Recipe, SnapRecipe, CharmRecipe

__all__ = [
    "__version__",
    "errors",
    "LaunchpadError",
    "Launchpad",
    "LaunchpadObject",
    "RecipeType",
    "Recipe",
    "SnapRecipe",
    "CharmRecipe",
]
