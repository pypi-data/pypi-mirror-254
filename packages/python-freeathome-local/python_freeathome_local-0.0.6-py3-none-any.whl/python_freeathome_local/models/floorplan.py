"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from dataclasses import dataclass
from typing import Any

from .floor import Floor


@dataclass
class Floorplan:
    """Model for a Floorplan."""

    __floors: dict[int, Floor]

    def __init__(self, config: dict[str, Any]):
        """Initialize a Floorplan."""
        self.__floors = {}

        for key, value in config.items():
            floor_id = int(key, 16)
            floor = Floor(floor_id, value)

            self.__floors[floor_id] = floor

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = f"Floors: {len(self.__floors)}"

        for floor in self.__floors.values():
            value = str(floor)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        return string

    def get_floor_by_identifier(self, identifier: int) -> Floor:
        """Return Floor by specific ID."""
        return self.__floors[identifier]
