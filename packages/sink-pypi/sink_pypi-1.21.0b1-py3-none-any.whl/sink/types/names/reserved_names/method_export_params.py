# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MethodExportParams"]


class MethodExportParams(TypedDict, total=False):
    let: str
    """test reserved word in query parameter"""

    const: str
    """test reserved word in body property"""
