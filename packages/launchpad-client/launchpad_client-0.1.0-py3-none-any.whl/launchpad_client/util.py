"""Utility functions."""

import urllib.parse
from collections.abc import Iterable, Sequence

from lazr.restfulclient.resource import Entry  # type: ignore[import-untyped]
from typing_extensions import Any

from launchpad_client import const


def getattrs(obj: object, path: Iterable[str]) -> Any:  # noqa: ANN401
    """Get an attribute from an object tree based on a path.

    :param obj: The root object of the tree.
    :param path: The getattr path.
    :returns: The resulting object.
    :raises: AttributeError if an attribute is not found.

    getattr_path(obj, "a.b.c") is equivalent to obj.a.b.c
    """
    if isinstance(path, str):
        path = path.split(".")
    path = iter(path)
    try:
        attr = next(path)
    except StopIteration:
        return obj
    try:
        inner = getattr(obj, attr)
    except AttributeError as exc:
        raise AttributeError(
            f"{obj.__class__.__name__!r} object has no attribute path {exc.name!r}",
            name=exc.name,
            obj=obj,
        ) from None
    try:
        return getattrs(inner, path)
    except AttributeError as exc:
        partial_path = f"{attr}.{exc.name}"
        raise AttributeError(
            f"{obj.__class__.__name__!r} object has no attribute path {partial_path!r}",
            name=partial_path,
            obj=obj,
        ) from None


def set_innermost_attr(
    obj: object,
    path: Sequence[str],
    value: Any,  # noqa: ANN401
) -> None:
    """Set the innermost attribute based on a path."""
    parent_path: Sequence[str] | str
    if isinstance(path, str):
        parent_path, _, attr_name = path.rpartition(".")
    else:
        parent_path = path[:-1]
        attr_name = path[-1]
    parent = getattrs(obj, parent_path) if parent_path else obj
    setattr(parent, attr_name, value)


def get_resource_type(entry: Entry) -> str:
    """Get the resource type of a Launchpad entry object as a string."""
    return str(urllib.parse.urlparse(entry.resource_type_link).fragment)


def get_person_link(person: str | Entry) -> str:
    """Get a link to a person or team.

    :param person: The person or team to link
    :returns: A Launchpad compatible link to the person.

    If the input is a string, this function assumes it is either a username or a
    link and coerces that. If it's lazr Entry, it retrieves the name and then
    converts that into a link.
    """
    if isinstance(person, Entry):
        if (resource_type := get_resource_type(person)) not in ("person", "team"):
            raise TypeError(f"Invalid resource type {resource_type!r}")
        person = person.name
    person = person.lstrip("/~").split("/", maxsplit=1)[0]
    return f"/~{person}"


def get_architecture_name(name: str) -> str:
    """Convert a string into its canonical Launchpad architecture name.

    :param name: An architecture name that may or may not be correct.
    :returns: A Launchpad architecture name.
    :raises: ValueError if there's no way to convert the string into an architecture name.
    """
    name = name.strip().lower()
    mapped_name = const.ARCHITECTURE_MAP.get(name, name)
    if mapped_name not in const.ARCHITECTURES:
        raise ValueError(f"Unknown architecture {name!r}")
    return mapped_name


def get_processor(name: str) -> str:
    """Convert a string into a Launchpad processor link."""
    return f"/+processors/{get_architecture_name(name)}"
