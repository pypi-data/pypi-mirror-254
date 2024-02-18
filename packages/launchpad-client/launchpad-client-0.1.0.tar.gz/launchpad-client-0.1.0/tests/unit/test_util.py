"""Tests for utility functions."""

from unittest import mock

import pytest
from hypothesis import given, strategies
from launchpad_client import const, util
from lazr.restfulclient.resource import Entry


class TestGetattrs:
    """Tests for getattrs function."""

    @given(path=strategies.iterables(strategies.text()))
    def test_success(self, path):
        obj = mock.Mock()

        actual = util.getattrs(obj, path)

        assert isinstance(actual, mock.Mock)

    @pytest.mark.parametrize(
        ("obj", "path", "expected"),
        [
            ("", ["__class__", "__name__"], "str"),
            (format, ["__call__", "__call__", "__class__", "__class__"], type),
            (1, "real.imag.numerator.denominator.__class__", int),
        ],
    )
    def test_success_examples(self, obj, path, expected):
        actual = util.getattrs(obj, path)

        assert actual == expected

    @pytest.mark.parametrize(
        ("obj", "path", "partial_path"),
        [
            ("", "non_attribute", "non_attribute"),
            ("", "upper.not.an.attribute", "upper.not"),
        ],
    )
    def test_exception(self, obj, path, partial_path):
        with pytest.raises(AttributeError) as exc_info:
            util.getattrs(obj, path)

        assert exc_info.value.name == partial_path
        assert exc_info.value.obj == obj


class TestGetPersonLink:
    """Tests for get_person_link."""

    @pytest.mark.parametrize("value", ["someone", "/~someone", "/~someone/+snaps"])
    def test_string_success(self, value):
        assert util.get_person_link(value) == "/~someone"

    @pytest.mark.parametrize("resource_type", ["person", "team"])
    def test_entry_success(self, resource_type):
        mock_entry = mock.Mock(spec=Entry)
        mock_entry.resource_type_link = f"http://blah/#{resource_type}"
        mock_entry.name = "someone"

        assert util.get_person_link(mock_entry) == "/~someone"

    def test_entry_wrong_type(self):
        mock_entry = mock.Mock(spec=Entry, resource_type_link="http://blah/#poo")

        with pytest.raises(TypeError, match="Invalid resource type 'poo'"):
            util.get_person_link(mock_entry)


class TestGetArchitectureName:
    """Tests for get_architecture_name."""

    @pytest.mark.parametrize("arch", const.ARCHITECTURES)
    def test_architecture_passthrough(self, arch):
        assert util.get_architecture_name(arch) == arch

    @pytest.mark.parametrize("arch", const.ARCHITECTURE_MAP.keys())
    def test_architecture_map(self, arch):
        assert util.get_architecture_name(arch) in const.ARCHITECTURES

    @pytest.mark.parametrize("arch", ["gothic", "brutalist"])
    def test_invalid_architecture(self, arch):
        with pytest.raises(ValueError, match="Unknown architecture"):
            util.get_architecture_name(arch)

    @pytest.mark.parametrize("arch", ["AMD64", " x64 ", "          ARMhf"])
    def test_string_manipulation(self, arch):
        assert util.get_architecture_name(arch) in const.ARCHITECTURES
