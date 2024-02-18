"""Errors for launchpad-client."""


class LaunchpadError(Exception):
    """Base error for launchpad-client."""


class NotFoundError(LaunchpadError):
    """An error for an item not being found."""
