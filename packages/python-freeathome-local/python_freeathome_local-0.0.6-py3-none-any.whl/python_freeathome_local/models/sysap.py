"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self
from uuid import UUID

from ..exceptions import FreeAtHomeError
from .abstractdevice import AbstractDevice
from .devicefactory import DeviceFactory
from .floorplan import Floorplan

if TYPE_CHECKING:
    from ..freeathome import FreeAtHome


# pylint: disable=too-many-instance-attributes
@dataclass
class SysAp:
    """Model for a SysAp."""

    __api: FreeAtHome
    __identifier: UUID
    __connection_state: str
    __name: str
    __uart_serial_number: str
    __version: str
    __devices: dict[str, AbstractDevice]
    __floorplan: Floorplan

    # pylint: disable=too-many-locals,too-many-branches
    @classmethod
    def from_api(
        cls,
        api: FreeAtHome,
        identifier: str,
        config: dict[str, Any],
        sys_ap_only: bool = True,
    ) -> Self:
        """Initialize a SysAp device from the API."""
        try:
            correct_id = UUID(str(identifier))
        except ValueError as exception:
            msg = f"The provided id '{identifier}' is malformed."
            raise FreeAtHomeError(msg) from exception

        if "connectionState" in config:
            conn_state = config["connectionState"]
        else:
            msg = "connectionState is not defined"
            raise FreeAtHomeError(msg)

        sysap_name = ""

        if "sysapName" in config:
            sysap_name = config["sysapName"]

        if "sysap" in config:
            uart_serial_number = ""

            if "uartSerialNumber" in config["sysap"]:
                uart_serial_number = config["sysap"]["uartSerialNumber"]

            version = ""

            if "version" in config["sysap"]:
                version = config["sysap"]["version"]

        else:
            msg = "SysapSection missing"
            raise FreeAtHomeError(msg)

        sys_ap = cls(
            api=api,
            identifier=correct_id,
            connection_state=conn_state,
            name=sysap_name,
            uart_serial_number=uart_serial_number,
            version=version,
        )

        if sys_ap_only is False:
            if "floorplan" in config:
                for key, value in config["floorplan"].items():
                    sys_ap.set_floorplan(Floorplan(value))

            if "devices" in config:
                for key, value in config["devices"].items():
                    device = DeviceFactory.create(sys_ap, key, value)

                    if device is not None:
                        sys_ap.set_device(key, device)
        #                        sysAp.__devices[key] = device

        return sys_ap

    def update_from_dict(self, data: dict[str, Any]) -> list:
        """Return list of updated datapoints from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data

        Returns:
        -------
            The updated datapoint objects as list.
        """
        datapoints = []

        if "datapoints" in data:
            for key, value in data["datapoints"].items():
                splitted = key.split("/", 1)
                # print(key, " has the value ", value)

                if splitted[0] in self.__devices:
                    datapoint = self.__devices[splitted[0]].update_from_dict(
                        splitted[1], value
                    )

                    if datapoint is not None:
                        datapoints.append(datapoint)
                        # print(
                        #     datapoint.get_channel().get_display_name(),
                        #     " - ",
                        #     datapoint.get_pairing_id().name,
                        #     " : ",
                        #     datapoint.get_value()
                        # )

                # else:
                #    print(f"Not defined : {key} has the value {value}")

        return datapoints

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = (
            f"Name      : {self.__name}\n"
            f"Identifier: {self.__identifier}\n"
            f"State     : {self.__connection_state}\n"
            f"uartSerial: {self.__uart_serial_number}\n"
            f"Version   : {self.__version}\n"
            f"Devices   : {len(self.__devices)}"
        )

        for device in self.__devices.values():
            value = str(device)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        value = str(self.__floorplan)
        string = f"{string}\n" f"{textwrap.indent(value, '    ')}"

        return string

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        api: FreeAtHome,
        identifier: UUID,
        connection_state: str,
        name: str,
        uart_serial_number: str,
        version: str,
    ) -> None:
        """Initialize a SysAp device class.

        Args:
        ----
            data: The full API response from a SysAp.

        Raises:
        ------
            FreeAtHomeError: In case the given API response is incomplete in a
                way that a Device object cannot be constructed from it.
        """
        self.__api = api
        self.__identifier = identifier
        self.__connection_state = connection_state
        self.__name = name
        self.__uart_serial_number = uart_serial_number
        self.__version = version
        self.__devices = {}

    def get_api(self) -> FreeAtHome:
        """Return API."""
        return self.__api

    def get_identifier(self) -> UUID:
        """Return Id of SysAp."""
        return self.__identifier

    def get_name(self) -> str:
        """Return name of SysAp."""
        return self.__name

    def get_version(self) -> str:
        """Return version of SysAp."""
        return self.__version

    def get_devices(self) -> dict[str, AbstractDevice]:
        """Return all devices."""
        return self.__devices

    def get_floorplan(self) -> Floorplan:
        """Return Floorplan."""
        return self.__floorplan

    def get_device_by_identifier(self, identifier: str) -> AbstractDevice:
        """Return specific Device by ID."""
        return self.__devices[identifier]

    def set_device(self, key: str, device: AbstractDevice) -> None:
        """Set specific Device."""
        self.__devices[key] = device

    def set_floorplan(self, floorplan: Floorplan) -> None:
        """Set Floorplan."""
        self.__floorplan = floorplan
