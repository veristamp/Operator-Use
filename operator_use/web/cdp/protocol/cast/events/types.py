"""CDP Cast Events"""
from __future__ import annotations
from typing import TypedDict, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.cast.types import Sink

class sinksUpdatedEvent(TypedDict, total=True):
    sinks: List[Sink]
class issueUpdatedEvent(TypedDict, total=True):
    issueMessage: str
