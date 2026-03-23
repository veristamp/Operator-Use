"""CDP DeviceAccess Types"""
from __future__ import annotations
from typing import TypedDict

RequestId = str
"""Device request id."""
DeviceId = str
"""A device id."""
class PromptDevice(TypedDict, total=True):
    """Device information displayed in a user prompt to select a device."""
    id: DeviceId
    name: str
    """Display name as it appears in a device request user prompt."""
