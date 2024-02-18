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
class MovementDetectorChannel(AbstractChannel):
    """Model for a Movement-Detector-Channel."""

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
        """Initialize a MovementDetectorChannel."""
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

    def get_info_on_off(self) -> bool:
        """Return InfoOnOff."""
        # This will be only set if the movement detector is e.g. attached
        # to a switch or light
        datapoint = self.get_input_by_pairing_id(PairingIDs.AL_INFO_ON_OFF)
        return datapoint.get_value() == "1"

    def get_state(self) -> bool:
        """Return InfoOnOff."""
        return self.get_info_on_off()

    def get_brightness_level(self) -> float:
        """Return BrightnessLevel."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_BRIGHTNESS_LEVEL
        )
        return float(datapoint.get_value())

    def get_timed_movement(self) -> bool:
        """Return always True, just when it is triggered it is movement."""
        # A momentary switch, which is triggered if movement is detected.
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_TIMED_MOVEMENT)
        return datapoint.get_value() == "1"

    def get_timed_presence(self) -> bool:
        """I don't know."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_TIMED_PRESENCE)
        return datapoint.get_value() == "1"
