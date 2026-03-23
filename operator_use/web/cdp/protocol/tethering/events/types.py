"""CDP Tethering Events"""
from __future__ import annotations
from typing import TypedDict

class acceptedEvent(TypedDict, total=True):
    port: int
    """Port number that was successfully bound."""
    connectionId: str
    """Connection id to be used."""
