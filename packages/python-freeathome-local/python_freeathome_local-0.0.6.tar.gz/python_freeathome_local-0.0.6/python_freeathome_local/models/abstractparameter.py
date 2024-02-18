"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC

from ..parameterids import ParameterIDs


class AbstractParameter(ABC):
    """Model for an abstract Parameter."""

    __identifier: str = ""
    __parameter_id: ParameterIDs
    __value: str = ""

    def __init__(self, identifier: str, parameter_id: ParameterIDs, value: str):
        """Initialize an AbstractParameter."""
        self.__identifier = identifier
        self.__parameter_id = parameter_id
        self.__value = value

    def __str__(self) -> str:
        """Redefine object-to-string."""
        return f"{self.__identifier} - {self.__value} - {self.__parameter_id}"

    def get_identifier(self) -> str:
        """Return identifier."""
        return self.__identifier
