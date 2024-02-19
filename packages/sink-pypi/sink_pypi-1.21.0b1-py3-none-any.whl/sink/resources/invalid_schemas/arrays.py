# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.invalid_schemas import ArrayMissingItemsResponse

__all__ = ["Arrays", "AsyncArrays"]


class Arrays(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArraysWithRawResponse:
        return ArraysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArraysWithStreamingResponse:
        return ArraysWithStreamingResponse(self)

    def missing_items(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrayMissingItemsResponse:
        return self._get(
            "/invalid_schemas/arrays/missing_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrayMissingItemsResponse,
        )


class AsyncArrays(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArraysWithRawResponse:
        return AsyncArraysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArraysWithStreamingResponse:
        return AsyncArraysWithStreamingResponse(self)

    async def missing_items(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrayMissingItemsResponse:
        return await self._get(
            "/invalid_schemas/arrays/missing_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrayMissingItemsResponse,
        )


class ArraysWithRawResponse:
    def __init__(self, arrays: Arrays) -> None:
        self._arrays = arrays

        self.missing_items = to_raw_response_wrapper(
            arrays.missing_items,
        )


class AsyncArraysWithRawResponse:
    def __init__(self, arrays: AsyncArrays) -> None:
        self._arrays = arrays

        self.missing_items = async_to_raw_response_wrapper(
            arrays.missing_items,
        )


class ArraysWithStreamingResponse:
    def __init__(self, arrays: Arrays) -> None:
        self._arrays = arrays

        self.missing_items = to_streamed_response_wrapper(
            arrays.missing_items,
        )


class AsyncArraysWithStreamingResponse:
    def __init__(self, arrays: AsyncArrays) -> None:
        self._arrays = arrays

        self.missing_items = async_to_streamed_response_wrapper(
            arrays.missing_items,
        )
