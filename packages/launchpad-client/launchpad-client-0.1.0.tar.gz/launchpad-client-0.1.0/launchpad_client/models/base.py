"""Base LaunchpadObject."""

from __future__ import annotations

import abc
import enum
import inspect
from collections.abc import Iterable, Mapping
from typing import TYPE_CHECKING

from lazr.restfulclient.resource import Entry  # type: ignore[import-untyped]
from typing_extensions import Any, Self

from launchpad_client import util

if TYPE_CHECKING:
    from launchpad_client.launchpad import Launchpad


class LaunchpadObject(metaclass=abc.ABCMeta):
    """A generic Launchpad object."""

    _resource_types: enum.EnumMeta
    _attr_map: Mapping[str, str]
    """Mapping of attributes for this object to their paths in Launchpad."""

    _lp: Launchpad
    _obj: Entry

    def __init__(self, lp: Launchpad, lp_obj: Entry) -> None:
        self._lp = lp
        self._obj = lp_obj

        for req_attr in ("_resource_types", "_attr_map"):
            if not hasattr(self.__class__, req_attr):
                raise AttributeError(
                    f"Class {self.__class__.__name__} requires {req_attr} attribute.",
                )

        try:
            self._resource_types(self._resource_type)
        except ValueError:
            raise TypeError(
                f"Launchpadlib entry not a valid resource type for {self.__class__.__name__}. "
                f"type: {self._resource_type!r}, "
                f"valid: {[t.value for t in self._resource_types]}",  # type: ignore[var-annotated]
            ) from None

    @classmethod
    @abc.abstractmethod
    def new(cls, *args: Any, **kwargs: Any) -> Self:
        """Create a new launchpad object."""

    @classmethod
    @abc.abstractmethod
    def get(cls, *args: Any, **kwargs: Any) -> Self:
        """Get an existing launchpad object."""

    @classmethod
    def find(cls, *args: Any, **kwargs: Any) -> Iterable[Self]:
        """Find existing Launchpad objects by various parameters."""
        raise NotImplementedError(f"{cls.__name__} does not implement find.")

    @property
    def _resource_type(self) -> str:
        """The resource type of the Launchpad entry."""
        return util.get_resource_type(self._obj)

    def __getattr__(self, item: str) -> Any:  # noqa: ANN401
        annotations = inspect.get_annotations(self.__class__, eval_str=True)
        if item in annotations:
            lp_obj = util.getattrs(self._obj, self._attr_map.get(item, item))
            cls = annotations[item]
            if issubclass(cls, LaunchpadObject):
                return cls(self._lp, lp_obj)
        if item in self._attr_map:
            return util.getattrs(self._obj, self._attr_map[item])
        if item in self._obj.lp_attributes:
            return getattr(self._obj, item)
        if item in (*self._obj.lp_entries, *self._obj.lp_collections):
            raise NotImplementedError("Cannot yet return meta types")
        raise AttributeError(f"{self.__class__.__name__!r} has no attribute {item!r}")

    def __setattr__(self, key: str, value: Any) -> None:  # noqa: ANN401
        if key in ("_lp", "_obj"):
            self.__dict__[key] = value
            return
        annotations = inspect.get_annotations(self.__class__, eval_str=True)
        if key in annotations:
            attr_path = self._attr_map.get(key, default=key)
            util.set_innermost_attr(self._obj, attr_path, value)
        elif key in self._attr_map:
            util.set_innermost_attr(self._obj, self._attr_map[key], value)
        elif key in (
            *self._obj.lp_attributes,
            *self._obj.lp_entries,
            *self._obj.lp_collections,
        ):
            setattr(self._obj, key, value)
        else:
            raise AttributeError(
                f"{self.__class__.__name__!r} has no attribute {key!r}",
            )

    def get_entry(self, item: str | None = None) -> Entry:
        """Get the launchpadlib Entry object for an item.

        :param item: The name of the entry to get, or None to get this object's entry.
        :returns: The Entry requested.

        This method essentially acts as a bail-out to directly access launchpadlib.
        If you use it, please file an issue with your use case.
        """
        if item is None:
            return self._obj
        if item in self._obj.lp_entries:
            return getattr(self._obj, item)
        raise ValueError(f"Entry type {self.resource_type!r} has no entry {item!r}")
