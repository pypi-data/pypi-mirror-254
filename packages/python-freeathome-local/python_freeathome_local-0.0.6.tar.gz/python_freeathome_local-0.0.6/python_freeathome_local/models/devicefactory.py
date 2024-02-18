"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from .floor import Floor
from .tpdevice import TPDevice

if TYPE_CHECKING:
    from .abstractdevice import AbstractDevice
    from .sysap import SysAp


@dataclass
class DeviceFactory:
    """Factory class for a device."""

    # pylint: disable=too-many-locals,too-many-branches
    @classmethod
    def create(
        cls, sys_ap: SysAp, serial_number: str, config: dict[str, Any]
    ) -> AbstractDevice | None:
        """Create a specific device object based on provided config."""
        orig_floor = ""
        orig_room = ""
        display_name = ""
        unresponsive = False
        unresponsive_counter = 0
        defect = False
        channels = {}
        parameters = {}
        return_ok = False

        if "floor" in config:
            orig_floor = config["floor"]

            if orig_floor != "":
                floor = sys_ap.get_floorplan().get_floor_by_identifier(
                    int(orig_floor, 16)
                )

        if "room" in config:
            orig_room = config["room"]

            if orig_room != "" and isinstance(floor, Floor):
                room = floor.get_room_by_identifier(int(orig_room, 16))

        if "displayName" in config:
            display_name = config["displayName"]

        if "unresponsive" in config:
            unresponsive = config["unresponsive"]

        if "unresponsiveCounter" in config:
            unresponsive_counter = config["unresponsiveCounter"]

        if "defect" in config:
            defect = config["defect"]

        if "channels" in config:
            channels = config["channels"]

        if "parameters" in config:
            parameters = config["parameters"]

        if "interface" in config:
            interface = config["interface"]

            if "sonos" == config["interface"]:
                # We ignore sonos devices
                print(
                    f"We ignore the device '{serial_number}' as it is a Sonos"
                )
            elif "hue" == config["interface"]:
                # We ignore hue devices
                print(f"We ignore device '{serial_number}' as it is a Hue")
            elif "TP" == config["interface"]:
                # TP devices will be processed
                print(
                    f"Let's process device '{serial_number}' "
                    f"with the name '{display_name}' as it is a TP device"
                )
                device = TPDevice(
                    sys_ap=sys_ap,
                    interface=interface,
                    serial_number=serial_number,
                    floor=floor if "floor" in locals() else None,
                    room=room if "room" in locals() else None,
                    display_name=display_name,
                    unresponsive=unresponsive,
                    unresponsive_counter=unresponsive_counter,
                    defect=defect,
                    channels=channels,
                    parameters=parameters,
                )
                return_ok = True

                if len(device.get_channels()) == 0:
                    return_ok = False
                    print("\tNo channels, so not added.")

            else:
                # All other interface devices will be ignored
                print(
                    f"We ignore device '{serial_number}' "
                    f"with the interface '{interface}' "
                    f"and the name '{display_name}'"
                )
        else:
            # We ignore devices without an interface
            print(
                f"The device '{serial_number}' "
                f"with the name '{display_name}' will be ignored"
            )

        return device if return_ok is True else None
