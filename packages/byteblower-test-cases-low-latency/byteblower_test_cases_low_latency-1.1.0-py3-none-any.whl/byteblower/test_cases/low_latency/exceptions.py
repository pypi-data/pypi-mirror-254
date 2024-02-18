"""Module related to exceptions and handling of them."""
class LowLatencyException(Exception):
    """Base class for all low-latency test exceptions."""


class InvalidInput(LowLatencyException):
    """Raised when the user provided invalid input values."""


class FeatureNotSupported(LowLatencyException):
    """
    Raised when a specific feature is not supported yet.

    .. versionadded:: 1.1.0
       Added for improved exception handling.
    """

class MaximumUdpPortExceeded(LowLatencyException):
    """Exceeded maximum allowed UDP port number (65535)."""


class MissingDirection(InvalidInput):

    def __init__(self, name):
        message = f"Missing direction in {name} configuration."
        super().__init__(message)
