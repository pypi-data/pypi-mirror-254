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
class SwitchActuatorChannel(AbstractChannel):
    """Model for a SwitchActuator-Channel."""

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
        """Initialize a SwitchActuatorChannel."""
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

    async def set_switch_on_off(self, status: bool):  # type: ignore
        """Turn the channel on or off."""
        datapoint = self.get_input_by_pairing_id(PairingIDs.AL_SWITCH_ON_OFF)
        return await datapoint.set_value(status)  # type: ignore

    async def turn_on(self):  # type: ignore
        """Turn on the channel."""
        return await self.set_switch_on_off(True)

    async def turn_off(self):  # type: ignore
        """Turn off the channel."""
        return await self.set_switch_on_off(False)

    async def set_forced(self, status: bool):  # type: ignore
        """Set Forced."""
        datapoint = self.get_input_by_pairing_id(PairingIDs.AL_FORCED)
        return await datapoint.set_value(status)  # type: ignore

    async def set_timed_start_stop(self, status: bool):  # type: ignore
        """Set TimedStartStop."""
        datapoint = self.get_input_by_pairing_id(PairingIDs.AL_TIMED_START_STOP)
        return await datapoint.set_value(status)  # type: ignore

    async def set_timed_movement(self, status: bool):  # type: ignore
        """Set TimedMovement."""
        datapoint = self.get_input_by_pairing_id(PairingIDs.AL_TIMED_MOVEMENT)
        return await datapoint.set_value(status)  # type: ignore

    def get_info_on_off(self) -> bool:
        """Return InfoOnOff."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_INFO_ON_OFF)
        return datapoint.get_value() == "1"

    def get_state(self) -> bool:
        """Return InfoOnOff."""
        return self.get_info_on_off()

    def get_info_force(self) -> bool:
        """Return InfoForce."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_INFO_FORCE)
        return datapoint.get_value() == "1"

    def get_info_error(self) -> bool:
        """Return InfoError."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_INFO_ERROR)
        return datapoint.get_value() == "1"
