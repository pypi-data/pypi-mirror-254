# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .simple_object import SimpleObject

__all__ = ["ObjectWithChildRef"]


class ObjectWithChildRef(BaseModel):
    bar: Optional[SimpleObject] = None

    foo: Optional[str] = None
