# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from ..shared import SimpleObject
from ..._models import BaseModel

__all__ = ["UnionTypeNullableUnionResponse", "BasicObject"]


class BasicObject(BaseModel):
    item: Optional[str] = None


UnionTypeNullableUnionResponse = Union[SimpleObject, BasicObject, None]
