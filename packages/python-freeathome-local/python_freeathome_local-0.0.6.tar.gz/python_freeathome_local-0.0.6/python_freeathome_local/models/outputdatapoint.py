"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .abstractdatapoint import AbstractDatapoint

if TYPE_CHECKING:
    from ..pairingids import PairingIDs
    from .abstractchannel import AbstractChannel


@dataclass
class OutputDatapoint(AbstractDatapoint):
    """Model for an Output-Datapoint."""

    # pylint: disable=useless-parent-delegation
    def __init__(
        self,
        channel: AbstractChannel,
        identifier: str,
        pairing_id: PairingIDs,
        value: str,
    ):
        """Initialize an OutputDatapoint."""
        super().__init__(channel, identifier, pairing_id, value)

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Output-Datapoint:\n" f"{parent}"
