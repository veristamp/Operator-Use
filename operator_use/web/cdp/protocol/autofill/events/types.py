"""CDP Autofill Events"""
from __future__ import annotations
from typing import TypedDict, List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.autofill.types import AddressUI
    from cdp.protocol.autofill.types import FilledField

class addressFormFilledEvent(TypedDict, total=True):
    filledFields: List[FilledField]
    """Information about the fields that were filled"""
    addressUi: AddressUI
    """An UI representation of the address used to fill the form. Consists of a 2D array where each child represents an address/profile line."""
