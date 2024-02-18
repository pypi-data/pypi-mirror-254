"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from abc import ABC
from typing import TYPE_CHECKING, Any

from .abstractparameter import AbstractParameter
from .channelfactory import ChannelFactory
from .floor import Floor
from .parameterfactory import ParameterFactory
from .room import Room

if TYPE_CHECKING:
    from .abstractchannel import AbstractChannel
    from .abstractdatapoint import AbstractDatapoint
    from .sysap import SysAp


# pylint: disable=too-many-instance-attributes
class AbstractDevice(ABC):
    """Model for an abstract Device."""

    __sys_ap: SysAp
    __serial_number: str = ""
    __floor: Floor | None = None
    __room: Room | None = None
    __display_name: str = ""
    __unresponsive: bool = False
    __unresponsive_counter: int = 0
    __defect: bool = False
    __channels: dict[str, AbstractChannel]
    __parameters: dict[str, AbstractParameter]

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        sys_ap: SysAp,
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
        """Initialize an AbstractDevice."""
        self.__sys_ap = sys_ap
        self.__serial_number = serial_number
        self.__floor = floor
        self.__room = room
        self.__display_name = display_name
        self.__unresponsive = unresponsive
        self.__unresponsive_counter = unresponsive_counter
        self.__defect = defect
        self.__channels = {}
        self.__parameters = {}

        for key, value in channels.items():
            channel = ChannelFactory.create(self, key, value)

            if channel is not None:
                self.__channels[key] = channel

        for key, value in parameters.items():
            parameter = ParameterFactory.create(key, value)

            if parameter is not None:
                self.__parameters[key] = parameter

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = (
            f"Serial      : {self.__serial_number}\n"
            f"Defect      : {self.__defect}\n"
            f"Unresponsive: {self.__unresponsive}\n"
            f"U-Counter   : {self.__unresponsive_counter}\n"
            f"Name        : {self.__display_name}\n"
            f"Floor       : {self.__floor}\n"
            f"Room        : {self.__room}\n"
            f"Channels    : {len(self.__channels)}"
        )

        for channel in self.__channels.values():
            value = str(channel)
            string = f"{string}\n" f"{textwrap.indent(value, '    ')}\n"

        string = (
            f"{string}\n"
            f"Parameters: {len(self.__parameters)}\n"
            f"----------"
        )

        for parameter in self.__parameters.values():
            value = str(parameter)
            string = f"{string}\n" f"{textwrap.indent(value, '    ')}\n"

        return string

    def get_sys_ap(self) -> SysAp:
        """Return SysAp of the Device."""
        return self.__sys_ap

    def get_serial_number(self) -> str:
        """Return SerialNumber of the Device."""
        return self.__serial_number

    def get_channels(self) -> dict:
        """Return all Channels of the Device."""
        return self.__channels

    def get_channel_by_identifier(self, identifier: str) -> AbstractChannel:
        """Return specific Channel of the Device."""
        return self.__channels[identifier]

    def get_display_name(self) -> str:
        """Return DisplayName of the Device."""
        return self.__display_name

    def update_from_dict(
        self, key: str, value: str
    ) -> AbstractDatapoint | None:
        """Return Channel object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data

        Returns:
        -------
            The updated Datapoint object.
        """
        datapoint = None
        splitted = key.split("/")

        if splitted[0] in self.__channels:
            datapoint = self.__channels[splitted[0]].update_from_dict(
                splitted[1], value
            )

        return datapoint
