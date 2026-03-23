"""CDP Tethering Methods Types"""
from __future__ import annotations
from typing import TypedDict

class bindParameters(TypedDict, total=True):
    port: int
    """Port number to bind."""
class unbindParameters(TypedDict, total=True):
    port: int
    """Port number to unbind."""
