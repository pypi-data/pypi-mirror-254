# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DiscriminatedUnion", "Foo", "Bar"]


class Foo(BaseModel):
    foo: Optional[str] = None

    type: Optional[Literal["foo"]] = None


class Bar(BaseModel):
    bar: Optional[str] = None

    type: Optional[Literal["bar"]] = None


DiscriminatedUnion = Union[Foo, Bar]
