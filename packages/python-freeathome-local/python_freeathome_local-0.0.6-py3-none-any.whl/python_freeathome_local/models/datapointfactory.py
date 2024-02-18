"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..pairingids import PairingIDs
from .inputdatapoint import InputDatapoint
from .outputdatapoint import OutputDatapoint

if TYPE_CHECKING:
    from .abstractchannel import AbstractChannel
    from .abstractdatapoint import AbstractDatapoint


@dataclass
class DatapointFactory:
    """Factory class for a Datapoint."""

    @classmethod
    def create(
        cls, channel: AbstractChannel, identifier: str, config: dict[str, Any]
    ) -> AbstractDatapoint:
        """Create a specific parameter object based on provided config."""
        pairing_id = 0
        value = ""

        if "value" in config:
            value = config["value"]

        if "pairingID" in config:
            pairing_id = int(config["pairingID"])

        for pairing in PairingIDs:
            if pairing_id == pairing.value:
                pairing_value = pairing
                break

        if "i" == identifier[:1]:
            datapoint = InputDatapoint(
                channel=channel,
                identifier=identifier,
                pairing_id=pairing_value,
                value=value,
            )
        elif "o" == identifier[:1]:
            datapoint = OutputDatapoint(
                channel=channel,
                identifier=identifier,
                pairing_id=pairing_value,
                value=value,
            )  # type: ignore

        try:
            datapoint
        except NameError:
            datapoint = None  # type: ignore

        return datapoint
