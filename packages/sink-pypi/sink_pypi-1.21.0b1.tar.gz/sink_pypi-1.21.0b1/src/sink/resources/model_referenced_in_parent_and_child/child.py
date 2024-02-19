# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...types import ModelReferencedInParentAndChild
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

__all__ = ["Child", "AsyncChild"]


class Child(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChildWithRawResponse:
        return ChildWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChildWithStreamingResponse:
        return ChildWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelReferencedInParentAndChild:
        return self._get(
            "/model_referenced_in_parent_and_child/child",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelReferencedInParentAndChild,
        )


class AsyncChild(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChildWithRawResponse:
        return AsyncChildWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChildWithStreamingResponse:
        return AsyncChildWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelReferencedInParentAndChild:
        return await self._get(
            "/model_referenced_in_parent_and_child/child",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelReferencedInParentAndChild,
        )


class ChildWithRawResponse:
    def __init__(self, child: Child) -> None:
        self._child = child

        self.retrieve = to_raw_response_wrapper(
            child.retrieve,
        )


class AsyncChildWithRawResponse:
    def __init__(self, child: AsyncChild) -> None:
        self._child = child

        self.retrieve = async_to_raw_response_wrapper(
            child.retrieve,
        )


class ChildWithStreamingResponse:
    def __init__(self, child: Child) -> None:
        self._child = child

        self.retrieve = to_streamed_response_wrapper(
            child.retrieve,
        )


class AsyncChildWithStreamingResponse:
    def __init__(self, child: AsyncChild) -> None:
        self._child = child

        self.retrieve = async_to_streamed_response_wrapper(
            child.retrieve,
        )
