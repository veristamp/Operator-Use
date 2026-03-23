"""CDP Accessibility Events"""
from __future__ import annotations
from typing import TypedDict, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.accessibility.types import AXNode

class loadCompleteEvent(TypedDict, total=True):
    root: AXNode
    """New document root node."""
class nodesUpdatedEvent(TypedDict, total=True):
    nodes: List[AXNode]
    """Updated node data."""
