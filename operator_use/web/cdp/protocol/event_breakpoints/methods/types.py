"""CDP EventBreakpoints Methods Types"""
from __future__ import annotations
from typing import TypedDict

class setInstrumentationBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Instrumentation name to stop on."""
class removeInstrumentationBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Instrumentation name to stop on."""
