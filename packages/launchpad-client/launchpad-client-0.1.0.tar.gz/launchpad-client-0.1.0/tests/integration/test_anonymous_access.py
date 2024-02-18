"""Tests for anonymous access."""

import launchpad_client
from launchpad_client import models


def test_get_basic_items(anonymous_lp):
    lp = launchpad_client.Launchpad(anonymous_lp)

    snapstore_server = lp.get_project("snapstore-server")
    assert snapstore_server.name == "snapstore-server"
    assert snapstore_server.title == "Snap Store Server"

    snap_recipes = list(models.SnapRecipe.find(lp, owner="lengau"))
    assert len(snap_recipes) > 0
    for recipe in snap_recipes:
        assert recipe.owner_name == "lengau"
