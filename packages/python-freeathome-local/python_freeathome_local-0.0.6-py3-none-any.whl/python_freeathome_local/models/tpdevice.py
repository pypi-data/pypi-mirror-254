"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from .abstractdevice import AbstractDevice

if TYPE_CHECKING:
    from .floor import Floor
    from .room import Room
    from .sysap import SysAp


@dataclass
class TPDevice(AbstractDevice):
    """Model for a TP-Device."""

    __interface: str = "TP"

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        sys_ap: SysAp,
        interface: str,
        serial_number: str,
        floor: Floor | None,
        room: Room | None,
        display_name: str,
        unresponsive: bool,
        unresponsive_counter: int,
        defect: bool,
        channels: dict[str, Any],
        parameters: dict[str, Any],
    ):
        """Initialize a TP-Device."""
        super().__init__(
            sys_ap,
            serial_number,
            floor,
            room,
            display_name,
            unresponsive,
            unresponsive_counter,
            defect,
            channels,
            parameters,
        )
        self.__interface = interface

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"TP-Device:\n" f"Interface: {self.__interface}\n" f"{parent}"
