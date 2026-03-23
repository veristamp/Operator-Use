"""CDP Performance Types"""
from __future__ import annotations
from typing import TypedDict

class Metric(TypedDict, total=True):
    """Run-time execution metric."""
    name: str
    """Metric name."""
    value: float
    """Metric value."""
