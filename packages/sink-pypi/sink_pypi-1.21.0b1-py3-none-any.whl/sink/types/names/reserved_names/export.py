# File generated from our OpenAPI spec by Stainless.

from typing import List

from .return_ import Return
from ...._models import BaseModel

__all__ = ["Export"]


class Export(BaseModel):
    export: List[Return]
    """test reserved word in response property"""
