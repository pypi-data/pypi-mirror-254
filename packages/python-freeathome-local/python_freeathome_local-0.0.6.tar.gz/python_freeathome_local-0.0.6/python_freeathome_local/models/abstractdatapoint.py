"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Any

from ..pairingids import PairingIDs

if TYPE_CHECKING:
    from .abstractchannel import AbstractChannel


class AbstractDatapoint(ABC):
    """Model for an abstract Datapoint."""

    __channel: AbstractChannel
    __identifier: str = ""
    __pairing_id: PairingIDs
    __value: str = ""

    def __init__(
        self,
        channel: AbstractChannel,
        identifier: str,
        pairing_id: PairingIDs,
        value: str,
    ):
        """Initialize an AbstractDatapoint."""
        self.__channel = channel
        self.__identifier = identifier
        self.__pairing_id = pairing_id
        self.__value = value

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = (
            f"Identifier: {self.__identifier}\n"
            f"Pairing   : {self.__pairing_id}\n"
            f"Value     : {self.__value}"
        )

        return string

    def get_channel(self) -> AbstractChannel:
        """Return Channel of the Datapoint."""
        return self.__channel

    def get_identifier(self) -> str:
        """Return Identifier of the Datapoint."""
        return self.__identifier

    def get_pairing_id(self) -> PairingIDs:
        """Return PairingID of the Datapoint."""
        return self.__pairing_id

    def set_value(self, value: Any) -> AbstractDatapoint:
        """Set value of the Datapoint."""
        if isinstance(value, bool):
            if value is True:
                value = 1
            elif value is False:
                value = 0

        self.__value = value
        return self

    def get_value(self) -> str:
        """Return value of the Datapoint."""
        return self.__value
