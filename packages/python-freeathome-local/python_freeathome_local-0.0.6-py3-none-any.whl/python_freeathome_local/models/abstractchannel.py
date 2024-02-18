"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from abc import ABC
from typing import TYPE_CHECKING, Any

from ..functionids import FunctionIDs
from ..pairingids import PairingIDs
from .datapointfactory import DatapointFactory
from .inputdatapoint import InputDatapoint
from .outputdatapoint import OutputDatapoint
from .parameter import Parameter
from .parameterfactory import ParameterFactory

if TYPE_CHECKING:
    from .abstractdatapoint import AbstractDatapoint
    from .abstractdevice import AbstractDevice
    from .floor import Floor
    from .room import Room


# pylint: disable=too-many-instance-attributes
class AbstractChannel(ABC):
    """Model for an abstract Channel."""

    _device: AbstractDevice
    _identifier: str = ""
    _floor: Floor | None = None
    _room: Room | None = None
    _display_name: str = ""
    _function_id: FunctionIDs | None = None
    _inputs: dict[str, InputDatapoint] | None = None
    _outputs: dict[str, OutputDatapoint] | None = None
    _parameters: dict[str, Parameter] | None = None

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        device: AbstractDevice,
        identifier: str,
        floor: Floor | None,
        room: Room | None,
        display_name: str,
        function_id: FunctionIDs,
        parameters: dict[str, Any],
        inputs: dict[str, Any],
        outputs: dict[str, Any],
    ):
        """Initialize an AbstractChannel."""
        self._device = device
        self._identifier = identifier
        self._floor = floor
        self._room = room
        self._display_name = display_name
        self._function_id = function_id
        self._inputs = {}
        self._outputs = {}
        self._parameters = {}

        for key, value in parameters.items():
            parameter = ParameterFactory.create(key, value)

            if parameter is not None:
                if isinstance(parameter, Parameter):
                    self._parameters[key] = parameter

        for key, value in inputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                if isinstance(datapoint, InputDatapoint):
                    self._inputs[key] = datapoint

        for key, value in outputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                if isinstance(datapoint, OutputDatapoint):
                    self._outputs[key] = datapoint

    def __str__(self) -> str:
        """Redefine object-to-string."""
        if self._floor is None:
            floor = "<Not set>"
        else:
            floor = self._floor.get_name()

        if self._room is None:
            room = "<Not set>"
        else:
            room = self._room.get_name()

        string = (
            f"Identifier: {self._identifier}\n"
            f"Name      : {self._display_name}\n"
            f"Floor     : {floor}\n"
            f"Room      : {room}\n"
            f"Function  : {self._function_id}"
        )

        if isinstance(self._inputs, dict):
            string = f"{string}\nInputs: {len(self._inputs)}\n----------"

            for datapoint_i in self._inputs.values():
                value = str(datapoint_i)
                string = (
                    f"{string}\n"
                    f"{textwrap.indent(value, '    ')}\n"
                    f"----------"
                )

        if isinstance(self._outputs, dict):
            string = f"{string}\nOutputs: {len(self._outputs)}\n----------"

            for datapoint_o in self._outputs.values():
                value = str(datapoint_o)
                string = (
                    f"{string}\n"
                    f"{textwrap.indent(value, '    ')}\n"
                    f"----------"
                )

        if isinstance(self._parameters, dict):
            string = (
                f"{string}\nParameters: {len(self._parameters)}\n----------"
            )

            for parameter in self._parameters.values():
                value = str(parameter)
                string = (
                    f"{string}\n"
                    f"{textwrap.indent(value, '    ')}\n"
                    f"----------"
                )

        return string

    def get_device(self) -> AbstractDevice:
        """Return Device of the Channel."""
        return self._device

    def get_identifier(self) -> str:
        """Return Identifier of the Channel."""
        return self._identifier

    def get_display_name(self) -> str:
        """Return DisplayName of the Channel."""
        return self._display_name

    def get_function_id(self) -> FunctionIDs | None:
        """Return FunctionID of the Channel."""
        return self._function_id

    def get_inputs(self) -> dict[str, InputDatapoint] | None:
        """Return all InputDatapoints of the Channel."""
        return self._inputs

    def update_from_dict(
        self, key: str, value: str
    ) -> AbstractDatapoint | None:
        """Return Datapoint object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data

        Returns:
        -------
            The updated Datapoint object.
        """
        datapoint = None

        if isinstance(self._outputs, dict):
            if key in self._outputs:
                if isinstance(self._outputs[key], OutputDatapoint):
                    datapoint = self._outputs[key].set_value(value)
                    return datapoint
        if isinstance(self._inputs, dict):
            if key in self._inputs:
                # Very special handling for MovementDetector because
                # for whatever reason an Input-Datapoint is set through
                # the websocket instead of an Output-Datapoint ...
                if isinstance(self._inputs[key], InputDatapoint):
                    datapoint = self._inputs[key].set_special_value(int(value))
                    return datapoint

        print(self.get_display_name(), " - ", key, " : ", value)
        return datapoint

    def get_output_by_pairing_id(
        self, pairing_id: PairingIDs
    ) -> AbstractDatapoint:
        """Return OutputDatapoint of a specific PairingID."""
        if isinstance(self._outputs, dict):
            for value in self._outputs.values():
                if value.get_pairing_id() == pairing_id:
                    return value

        raise NameError

    def get_input_by_pairing_id(
        self, pairing_id: PairingIDs
    ) -> AbstractDatapoint:
        """Return InputDatapoint of a specific PairingID."""
        if isinstance(self._inputs, dict):
            for value in self._inputs.values():
                if value.get_pairing_id() == pairing_id:
                    return value

        raise NameError
