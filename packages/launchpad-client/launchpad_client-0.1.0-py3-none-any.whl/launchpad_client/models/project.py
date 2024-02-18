"""Project class."""

from __future__ import annotations  # noqa: I001

import enum
from collections.abc import Iterable
from typing_extensions import Self, Any
from typing import TYPE_CHECKING

from typing_extensions import override

from launchpad_client.models.base import LaunchpadObject

if TYPE_CHECKING:
    from launchpad_client import Launchpad


class ProjectType(enum.Enum):
    """The possible types of project."""

    Project = "project"


class Project(LaunchpadObject):
    """A Launchpad Project.

    https://api.launchpad.net/devel.html#project
    """

    _resource_types = ProjectType
    _attr_map = {}

    name: str
    title: str
    display_name: str
    summary: str
    description: str

    @classmethod
    @override
    def new(
        cls,
        lp: Launchpad,
        title: str,
        name: str,
        display_name: str,
        summary: str,
        *,
        description: str | None = None,
        **kwargs: Any,
    ) -> Self:
        """Create a new project.

        https://api.launchpad.net/devel.html#projects-new_project
        """
        if description:
            kwargs["description"] = description
        return cls(
            lp,
            lp.lp.projects.new_project(
                title=title,
                name=name,
                display_name=display_name,
                summary=summary,
                **kwargs,
            ),
        )

    @classmethod
    @override
    def get(cls, lp: Launchpad, name: str) -> Self:
        """Get an existing project."""
        return cls(lp, lp.lp.projects[name])

    @classmethod
    @override
    def find(cls, lp: Launchpad, text: str) -> Iterable[Self]:
        """Find projects by a search term."""
        for lp_project in lp.lp.projects.search(text):
            yield cls(lp, lp_project)
