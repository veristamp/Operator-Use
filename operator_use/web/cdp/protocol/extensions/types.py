"""CDP Extensions Types"""
from __future__ import annotations
from typing import TypedDict, Literal

StorageArea = Literal['session','local','sync','managed']
"""Storage areas."""
class ExtensionInfo(TypedDict, total=True):
    """Detailed information about an extension."""
    id: str
    """Extension id."""
    name: str
    """Extension name."""
    version: str
    """Extension version."""
    path: str
    """The path from which the extension was loaded."""
    enabled: bool
    """Extension enabled status."""
