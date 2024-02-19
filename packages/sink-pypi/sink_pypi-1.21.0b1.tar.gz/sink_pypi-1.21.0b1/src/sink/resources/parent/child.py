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
from ...types.parent import ChildInlinedResponseResponse

__all__ = ["Child", "AsyncChild"]


class Child(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChildWithRawResponse:
        return ChildWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChildWithStreamingResponse:
        return ChildWithStreamingResponse(self)

    def inlined_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildInlinedResponseResponse:
        """Method with inlined response model."""
        return self._get(
            "/inlined_response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildInlinedResponseResponse,
        )


class AsyncChild(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChildWithRawResponse:
        return AsyncChildWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChildWithStreamingResponse:
        return AsyncChildWithStreamingResponse(self)

    async def inlined_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildInlinedResponseResponse:
        """Method with inlined response model."""
        return await self._get(
            "/inlined_response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildInlinedResponseResponse,
        )


class ChildWithRawResponse:
    def __init__(self, child: Child) -> None:
        self._child = child

        self.inlined_response = to_raw_response_wrapper(
            child.inlined_response,
        )


class AsyncChildWithRawResponse:
    def __init__(self, child: AsyncChild) -> None:
        self._child = child

        self.inlined_response = async_to_raw_response_wrapper(
            child.inlined_response,
        )


class ChildWithStreamingResponse:
    def __init__(self, child: Child) -> None:
        self._child = child

        self.inlined_response = to_streamed_response_wrapper(
            child.inlined_response,
        )


class AsyncChildWithStreamingResponse:
    def __init__(self, child: AsyncChild) -> None:
        self._child = child

        self.inlined_response = async_to_streamed_response_wrapper(
            child.inlined_response,
        )
