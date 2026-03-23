"""CDP Performance Events"""
from __future__ import annotations
from typing import TypedDict, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.performance.types import Metric

class metricsEvent(TypedDict, total=True):
    metrics: List[Metric]
    """Current values of the metrics."""
    title: str
    """Timestamp title."""
