"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..pairingids import PairingIDs
from .abstractchannel import AbstractChannel

if TYPE_CHECKING:
    from ..functionids import FunctionIDs
    from .abstractdevice import AbstractDevice
    from .floor import Floor
    from .room import Room


@dataclass
class TriggerChannel(AbstractChannel):
    """Model for a Trigger-Channel."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        device: AbstractDevice,
        identifier: str,
        floor: Floor,
        room: Room,
        display_name: str,
        function_id: FunctionIDs,
        parameters: dict[str, Any],
        inputs: dict[str, Any],
        outputs: dict[str, Any],
    ):
        """Initialize a TriggerChannel."""
        super().__init__(
            device,
            identifier,
            floor,
            room,
            display_name,
            function_id,
            parameters,
            inputs,
            outputs,
        )

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Trigger-Channel:\n" f"{parent}"

    async def set_timed_start_stop(self):  # type: ignore
        """Trigger the channel."""
        datapoint = self.get_input_by_pairing_id(PairingIDs.AL_TIMED_START_STOP)
        return await datapoint.set_value(1)  # type: ignore

    async def press(self):  # type: ignore
        """Trigger the channel."""
        return await self.set_timed_start_stop()  # type: ignore
