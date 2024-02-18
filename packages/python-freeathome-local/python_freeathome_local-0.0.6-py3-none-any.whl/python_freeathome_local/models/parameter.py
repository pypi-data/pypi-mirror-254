"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .abstractparameter import AbstractParameter

if TYPE_CHECKING:
    from ..parameterids import ParameterIDs


@dataclass
class Parameter(AbstractParameter):
    """Model for a Parameter."""

    # pylint: disable=useless-parent-delegation
    def __init__(self, identifier: str, parameter_id: ParameterIDs, value: str):
        """Initialize a Parameter."""
        super().__init__(identifier, parameter_id, value)
