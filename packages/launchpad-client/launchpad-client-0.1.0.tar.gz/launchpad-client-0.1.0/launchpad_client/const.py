"""Constants for launchpad_client."""

from types import MappingProxyType

ARCHITECTURES = (
    "ia64",
    "sparc",
    "hppa",
    "i386",
    "amd64",
    "armel",
    "armhf",
    "lpia",
    "ppc64el",
    "s390x",
    "arm64",
    "powerpc",
    "riscv64",
)
"""Architectures supported by Launchpad."""

ARCHITECTURE_MAP = MappingProxyType({"x86_64": "amd64", "x64": "amd64", "x86": "i386"})
"""Map of alternative architecture names to Debian architectures."""
