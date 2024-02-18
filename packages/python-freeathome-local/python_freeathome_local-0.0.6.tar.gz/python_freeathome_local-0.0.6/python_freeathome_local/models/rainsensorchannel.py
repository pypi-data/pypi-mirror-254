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
class RainSensorChannel(AbstractChannel):
    """Model for a Rain-Sensor-Channel."""

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
        """Initialize a RainSensorChannel."""
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

    def get_rain_alarm(self) -> bool:
        """Return RainAlarm."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_RAIN_ALARM)
        return datapoint.get_value() == "1"

    def get_state(self) -> bool:
        """Return RainAlarm."""
        return self.get_rain_alarm()

    def get_rain_sensor_activation_percentage(self) -> float:
        """Return RainSensorActivationPercentage."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_RAIN_SENSOR_ACTIVATION_PERCENTAGE
        )
        return float(datapoint.get_value())

    def get_rain_sensor_frequency(self) -> float:
        """Return RainSensorFrequency."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_RAIN_SENSOR_FREQUENCY
        )
        return float(datapoint.get_value())
