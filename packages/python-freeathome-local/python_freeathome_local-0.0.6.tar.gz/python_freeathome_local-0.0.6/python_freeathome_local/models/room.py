"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Room:
    """Model for a Room."""

    __identifier: int
    __name: str

    def __init__(self, identifier: int, config: dict[str, Any]):
        """Initialize a Room."""
        self.__identifier = identifier
        self.__name = ""

        if "name" in config:
            self.__name = config["name"]

    def __str__(self) -> str:
        """Redefine object-to-string."""
        return f"{self.__identifier} - {self.__name}"

    def get_identifier(self) -> int:
        """Return Id of Room."""
        return self.__identifier

    def get_name(self) -> str:
        """Return Name of Room."""
        return self.__name
