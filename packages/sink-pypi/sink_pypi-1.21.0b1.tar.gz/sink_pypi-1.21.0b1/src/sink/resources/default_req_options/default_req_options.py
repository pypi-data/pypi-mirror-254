# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .child import (
    Child,
    AsyncChild,
    ChildWithRawResponse,
    AsyncChildWithRawResponse,
    ChildWithStreamingResponse,
    AsyncChildWithStreamingResponse,
)
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
from ...types.shared import BasicSharedModelObject

__all__ = ["DefaultReqOptions", "AsyncDefaultReqOptions"]


class DefaultReqOptions(SyncAPIResource):
    @cached_property
    def child(self) -> Child:
        return Child(self._client)

    @cached_property
    def with_raw_response(self) -> DefaultReqOptionsWithRawResponse:
        return DefaultReqOptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultReqOptionsWithStreamingResponse:
        return DefaultReqOptionsWithStreamingResponse(self)

    def example_method(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """Testing resource level default request options."""
        extra_headers = {"X-My-Header": "true", "X-My-Other-Header": "false", **(extra_headers or {})}
        return self._get(
            "/default_req_options",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )


class AsyncDefaultReqOptions(AsyncAPIResource):
    @cached_property
    def child(self) -> AsyncChild:
        return AsyncChild(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDefaultReqOptionsWithRawResponse:
        return AsyncDefaultReqOptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultReqOptionsWithStreamingResponse:
        return AsyncDefaultReqOptionsWithStreamingResponse(self)

    async def example_method(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """Testing resource level default request options."""
        extra_headers = {"X-My-Header": "true", "X-My-Other-Header": "false", **(extra_headers or {})}
        return await self._get(
            "/default_req_options",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )


class DefaultReqOptionsWithRawResponse:
    def __init__(self, default_req_options: DefaultReqOptions) -> None:
        self._default_req_options = default_req_options

        self.example_method = to_raw_response_wrapper(
            default_req_options.example_method,
        )

    @cached_property
    def child(self) -> ChildWithRawResponse:
        return ChildWithRawResponse(self._default_req_options.child)


class AsyncDefaultReqOptionsWithRawResponse:
    def __init__(self, default_req_options: AsyncDefaultReqOptions) -> None:
        self._default_req_options = default_req_options

        self.example_method = async_to_raw_response_wrapper(
            default_req_options.example_method,
        )

    @cached_property
    def child(self) -> AsyncChildWithRawResponse:
        return AsyncChildWithRawResponse(self._default_req_options.child)


class DefaultReqOptionsWithStreamingResponse:
    def __init__(self, default_req_options: DefaultReqOptions) -> None:
        self._default_req_options = default_req_options

        self.example_method = to_streamed_response_wrapper(
            default_req_options.example_method,
        )

    @cached_property
    def child(self) -> ChildWithStreamingResponse:
        return ChildWithStreamingResponse(self._default_req_options.child)


class AsyncDefaultReqOptionsWithStreamingResponse:
    def __init__(self, default_req_options: AsyncDefaultReqOptions) -> None:
        self._default_req_options = default_req_options

        self.example_method = async_to_streamed_response_wrapper(
            default_req_options.example_method,
        )

    @cached_property
    def child(self) -> AsyncChildWithStreamingResponse:
        return AsyncChildWithStreamingResponse(self._default_req_options.child)
