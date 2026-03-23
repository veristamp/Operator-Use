"""CDP Performance Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Literal, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.performance.types import Metric


class enableParameters(TypedDict, total=False):
    timeDomain: NotRequired[Literal["timeTicks", "threadTicks"]]
    """Time domain to use for collecting and reporting duration metrics."""



class getMetricsReturns(TypedDict):
    metrics: List[Metric]
    """Current values for run-time metrics."""
