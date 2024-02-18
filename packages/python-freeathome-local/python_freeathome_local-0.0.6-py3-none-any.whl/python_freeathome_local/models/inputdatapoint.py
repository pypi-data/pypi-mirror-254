"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .abstractdatapoint import AbstractDatapoint

if TYPE_CHECKING:
    from ..pairingids import PairingIDs
    from .abstractchannel import AbstractChannel


@dataclass
class InputDatapoint(AbstractDatapoint):
    """Model for an Input-Datapoint."""

    # pylint: disable=useless-parent-delegation
    def __init__(
        self,
        channel: AbstractChannel,
        identifier: str,
        pairing_id: PairingIDs,
        value: str,
    ):
        """Initialize a Inputdatapoint."""
        super().__init__(channel, identifier, pairing_id, value)

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Input-Datapoint:\n" f"{parent}"

    # pylint: disable=invalid-overridden-method
    async def set_value(self, value: int) -> None:  # type: ignore
        """Set Value of current Datapoint and inform SysAp."""
        # Running mypy over this function I get
        #   error: Return type "Coroutine[Any, Any, InputDatapoint]"
        #       of "setValue" incompatible with return type "AbstractDatapoint"
        #       in supertype "AbstractDatapoint"  [override]
        #    I don't know how to solve this
        super().set_value(value)
        #        return (
        #            await self.get_channel()
        #            .get_device()
        #            .get_sys_ap()
        #            .get_api()
        #            .set_datapoint(self)
        #        )
        await self.get_channel().get_device().get_sys_ap().get_api().set_datapoint(
            self
        )

    def set_special_value(self, value: int) -> InputDatapoint:
        """Set Value of current Datapoint without informing SysAp."""
        super().set_value(value)
        return self
