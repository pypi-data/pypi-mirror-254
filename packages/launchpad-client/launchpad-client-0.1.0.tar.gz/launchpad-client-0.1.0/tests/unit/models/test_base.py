"""Basic Launchpad object tests."""

import enum
from typing import Any
from unittest import mock

import pytest
from launchpad_client import Launchpad, LaunchpadObject
from lazr.restfulclient.resource import Entry
from typing_extensions import Self


class Type(enum.Enum):
    """Resource types for testing."""

    THIS = "this"
    VALID = "valid_type"
    NAME = "something"


class FakeLaunchpadObject(LaunchpadObject):
    """A Launchpad object for testing."""

    _resource_types = Type
    _attr_map = {}

    @classmethod
    def get(cls, *args: Any, **kwargs: Any) -> Self:
        raise NotImplementedError

    @classmethod
    def new(cls, *args: Any, **kwargs: Any) -> Self:
        raise NotImplementedError


class TestInit:
    """Tests for the initialiser."""

    @pytest.mark.parametrize("resource_type", [t.value for t in Type])
    def test_init_success(self, resource_type):
        mock_entry = mock.Mock(spec=Entry)
        mock_entry.resource_type_link = f"https://localhost/#{resource_type}"
        mock_entry.lp_attributes = []
        mock_lp = mock.Mock(spec_set=Launchpad)

        FakeLaunchpadObject(mock_lp, mock_entry)

    def test_attribute_not_set(self):
        class NoTypes(LaunchpadObject):
            @classmethod
            def get(cls, *args: Any, **kwargs: Any) -> Self:
                ...

            @classmethod
            def new(cls, *args: Any, **kwargs: Any) -> Self:
                ...

        with pytest.raises(
            AttributeError,
            match="NoTypes requires _resource_types",
        ):
            NoTypes(mock.Mock(), mock.Mock())

        class NoAttrMap(NoTypes):
            _resource_types = Type

        with pytest.raises(AttributeError, match="NoAttrMap requires _attr_map"):
            NoAttrMap(mock.Mock(), mock.Mock())

    @pytest.mark.parametrize("resource_type", ["ThIs", "invalid_type", "NAME"])
    def test_invalid_resource_type(self, resource_type):
        mock_entry = mock.Mock(spec=Entry)
        mock_entry.resource_type_link = f"https://localhost/#{resource_type}"
        mock_entry.lp_attributes = []
        mock_lp = mock.Mock(spec_set=Launchpad)

        with pytest.raises(
            TypeError,
            match="Launchpadlib entry not a valid resource type for",
        ):
            FakeLaunchpadObject(mock_lp, mock_entry)
