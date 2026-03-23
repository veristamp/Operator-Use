"""CDP Log Methods Types"""
from __future__ import annotations
from typing import TypedDict, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.log.types import ViolationSetting




class startViolationsReportParameters(TypedDict, total=True):
    config: List[ViolationSetting]
    """Configuration for violations."""
