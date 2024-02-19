# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BodyParamObjectWithArrayOfObjectsParams", "ArrayProp"]


class BodyParamObjectWithArrayOfObjectsParams(TypedDict, total=False):
    array_prop: List[ArrayProp]


class ArrayProp(TypedDict, total=False):
    kind: Required[Literal["VIRTUAL", "PHYSICAL"]]
