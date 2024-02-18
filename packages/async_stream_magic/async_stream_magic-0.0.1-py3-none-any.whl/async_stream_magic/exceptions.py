"""Exceptions for StreamMagic Devices."""

class StreamMagicError(Exception):
    """Generic StreamMagic Device exception."""


class StreamMagicConnectionError(StreamMagicError):
    """StreamMagic Device connection exception."""