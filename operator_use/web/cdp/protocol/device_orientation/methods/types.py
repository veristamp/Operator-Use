"""CDP DeviceOrientation Methods Types"""
from __future__ import annotations
from typing import TypedDict


class setDeviceOrientationOverrideParameters(TypedDict, total=True):
    alpha: float
    """Mock alpha"""
    beta: float
    """Mock beta"""
    gamma: float
    """Mock gamma"""
