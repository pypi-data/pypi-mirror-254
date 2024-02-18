"""Main Launchpad client."""

import pathlib

import launchpadlib.launchpad  # type: ignore[import-untyped]
import launchpadlib.uris  # type: ignore[import-untyped]
import platformdirs
from typing_extensions import Any, Self

from launchpad_client import models

DEFAULT_CACHE_PATH = platformdirs.user_cache_path("launchpad-client")


class Launchpad:
    """A client for Launchpad."""

    def __init__(self, launchpad: launchpadlib.launchpad.Launchpad) -> None:
        self.lp = launchpad

    @classmethod
    def anonymous(
        cls,
        app_name: str,
        root: str = launchpadlib.uris.LPNET_SERVICE_ROOT,
        cache_dir: pathlib.Path | None = DEFAULT_CACHE_PATH,
        version: str = "devel",
        timeout: int | None = None,
    ) -> Self:
        """Get an anonymous Launchpad client."""
        return cls(
            launchpadlib.launchpad.Launchpad.login_anonymously(
                consumer_name=app_name,
                service_root=root,
                launchpadlib_dir=cache_dir,
                version=version,
                timeout=timeout,
            ),
        )

    @classmethod
    def login(
        cls,
        app_name: str,
        root: str = launchpadlib.uris.LPNET_SERVICE_ROOT,
        cache_dir: pathlib.Path | None = DEFAULT_CACHE_PATH,
        credentials_file: pathlib.Path | None = None,
        **kwargs: Any,
    ) -> Self:
        """Login to Launchpad."""
        return cls(
            launchpadlib.launchpad.Launchpad.login_with(
                application_name=app_name,
                service_root=root,
                launchpadlib_dir=cache_dir,
                credentials_file=credentials_file,
                **kwargs,
            ),
        )

    def get_recipe(
        self,
        type_: models.RecipeType | str,
        name: str,
        owner: str,
        project: str | None = None,
    ) -> models.Recipe:
        """Get a recipe.

        :param type_: The type of recipe to get.
        :param owner: The owner of the recipe.
        :param name: The name of the recipe.
        :param project: (Optional) The project to which the recipe is attached
        :returns: A Recipe object of the appropriate type.
        :raises: ValueError if the type requested is invalid.

        A charm recipe requires a project. If none is given, the first charm matching
        the owner and name is returned, even if multiple recipes exist.
        """
        if isinstance(type_, str):
            type_ = models.RecipeType.__members__.get(type_.upper(), type_)
            type_ = models.RecipeType(type_)

        if type_ is models.RecipeType.SNAP:
            return models.SnapRecipe.get(self, name, owner)
        if type_ is models.RecipeType.CHARM:
            if project:
                return models.CharmRecipe.get(self, name, owner, project)
            result = None
            for recipe in models.CharmRecipe.find(self, owner, name=name):
                if recipe is not None:
                    raise ValueError(
                        f"Multiple charm recipes for {name!r} found with owner {owner!r}",
                    )
                result = recipe
            if result is None:
                raise ValueError(
                    f"Could not find charm recipe {name!r} with owner {owner!r}",
                )
            return result

        raise TypeError(f"Unknown recipe type: {type_}")

    def get_project(self, name: str) -> models.Project:
        """Get a project."""
        return models.Project.get(self, name)
