"""Exceptions for Free@Home."""


class FreeAtHomeError(Exception):
    """Generic FreeAtHome exception."""


class FreeAtHomeConnectionTimeoutError(Exception):
    """FreeAtHome connection timeout exception."""


class FreeAtHomeUnauthorizedError(Exception):
    """FreeAtHome unauthorized exception."""


class FreeAtHomeConnectionError(Exception):
    """FreeAtHome connection excpetion."""


class FreeAtHomeConnectionClosedError(Exception):
    """FreeAtHome WebSocket connection has been closed."""


class FreeAtHomeEmptyResponseError(Exception):
    """FreeAtHome returned wrong or empty response."""
