"""CDP DeviceAccess Events"""
from __future__ import annotations
from typing import TypedDict, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.device_access.types import PromptDevice
    from cdp.protocol.device_access.types import RequestId

class deviceRequestPromptedEvent(TypedDict, total=True):
    id: RequestId
    devices: List[PromptDevice]
