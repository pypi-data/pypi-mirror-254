"""Asynchronous Python client for Cambridge Audio StreamMagic Devices."""
from .stream_magic import StreamMagic, StreamMagicConnectionError, StreamMagicError
from .models import Info, Source, State

__all__ = [
    "StreamMagic",
    "StreamMagicConnectionError",
    "StreamMagicError",
    "Info",
    "Source",
    "State",
]