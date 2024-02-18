"""Asynchronous Python client for Free@Home."""

# pylint: disable=unused-import

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..functionids import FunctionIDs
from .abstractchannel import AbstractChannel
from .blindsensorchannel import BlindSensorChannel  # noqa: F401
from .brightnesssensorchannel import BrightnessSensorChannel  # noqa: F401

# fmt: off
from .desdoorringingsensorchannel import DesDoorRingingSensorChannel  # noqa: F401

# fmt: on
from .floor import Floor
from .forceonoffsensorchannel import ForceOnOffSensorChannel  # noqa: F401
from .movementdetectorchannel import MovementDetectorChannel  # noqa: F401
from .rainsensorchannel import RainSensorChannel  # noqa: F401
from .switchactuatorchannel import SwitchActuatorChannel  # noqa: F401
from .switchsensorchannel import SwitchSensorChannel  # noqa: F401
from .temperaturesensorchannel import TemperatureSensorChannel  # noqa: F401
from .triggerchannel import TriggerChannel  # noqa: F401
from .windowdoorsensorchannel import WindowDoorSensorChannel  # noqa: F401
from .windsensorchannel import WindSensorChannel  # noqa: F401

if TYPE_CHECKING:
    from .abstractdevice import AbstractDevice


@dataclass
class ChannelFactory:
    """Factory class for a channel."""

    # pylint: disable=too-many-locals,too-many-branches
    @classmethod
    def create(
        cls, the_device: AbstractDevice, identifier: str, config: dict[str, Any]
    ) -> AbstractChannel | None:
        """Create a specific channel object based on provided config."""
        device = the_device
        orig_floor = ""
        orig_room = ""
        display_name = ""
        function_id = 0x0
        parameters = {}
        inputs = {}
        outputs = {}
        channel = None

        if "floor" in config:
            orig_floor = config["floor"]

            if orig_floor != "":
                floor = (
                    device.get_sys_ap()
                    .get_floorplan()
                    .get_floor_by_identifier(int(orig_floor, 16))
                )

        if "room" in config:
            orig_room = config["room"]

            if orig_room != "" and isinstance(floor, Floor):
                room = floor.get_room_by_identifier(int(orig_room, 16))

        if "displayName" in config:
            display_name = config["displayName"]

        if "parameters" in config:
            parameters = config["parameters"]

        if "inputs" in config:
            inputs = config["inputs"]

        if "outputs" in config:
            outputs = config["outputs"]

        if "functionID" in config and config["functionID"] != "":
            function_id = int(config["functionID"], 16)
            print(f"\t{function_id} - {FunctionIDs(function_id).name}")

            if function_id in FunctionIDs:
                class_name = (
                    FunctionIDs(function_id)
                    .name.removeprefix("FID_")
                    .title()
                    .replace("_", "")
                    + "Channel"
                )

                try:
                    channel = globals()[class_name](
                        device=device,
                        identifier=identifier,
                        floor=floor if "floor" in locals() else None,
                        room=room if "room" in locals() else None,
                        display_name=display_name,
                        function_id=FunctionIDs(function_id),
                        parameters=parameters,
                        inputs=inputs,
                        outputs=outputs,
                    )
                    print("\t\tok")
                except KeyError:
                    # channel = None
                    print(f"\t\t{class_name} not defined")

        if isinstance(channel, AbstractChannel):
            return channel

        return None
