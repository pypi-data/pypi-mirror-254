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
class TemperatureSensorChannel(AbstractChannel):
    """Model for a Temperature-Sensor-Channel."""

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
        """Initialize TemperatureSensorChannel."""
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

    def get_outdoor_temperature(self) -> float:
        """Return OutdoorTemperature."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_OUTDOOR_TEMPERATURE
        )
        return float(datapoint.get_value())

    def get_state(self) -> float:
        """Return OutdoorTemperature."""
        return self.get_outdoor_temperature()

    def get_frost_alarm(self) -> bool:
        """Return FrostAlarm."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_FROST_ALARM)
        return datapoint.get_value() == "1"
