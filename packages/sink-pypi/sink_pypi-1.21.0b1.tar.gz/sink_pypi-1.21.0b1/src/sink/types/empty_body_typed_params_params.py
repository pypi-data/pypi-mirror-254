# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmptyBodyTypedParamsParams"]


class EmptyBodyTypedParamsParams(TypedDict, total=False):
    body: Required[object]

    query_param: str
    """Query param description"""

    second_query_param: str
    """Query param description"""
