# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import RootResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["Testing", "AsyncTesting"]


class Testing(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestingWithRawResponse:
        return TestingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestingWithStreamingResponse:
        return TestingWithStreamingResponse(self)

    def root(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RootResponse:
        return self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RootResponse,
        )


class AsyncTesting(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestingWithRawResponse:
        return AsyncTestingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestingWithStreamingResponse:
        return AsyncTestingWithStreamingResponse(self)

    async def root(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RootResponse:
        return await self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RootResponse,
        )


class TestingWithRawResponse:
    __test__ = False

    def __init__(self, testing: Testing) -> None:
        self._testing = testing

        self.root = to_raw_response_wrapper(
            testing.root,
        )


class AsyncTestingWithRawResponse:
    def __init__(self, testing: AsyncTesting) -> None:
        self._testing = testing

        self.root = async_to_raw_response_wrapper(
            testing.root,
        )


class TestingWithStreamingResponse:
    __test__ = False

    def __init__(self, testing: Testing) -> None:
        self._testing = testing

        self.root = to_streamed_response_wrapper(
            testing.root,
        )


class AsyncTestingWithStreamingResponse:
    def __init__(self, testing: AsyncTesting) -> None:
        self._testing = testing

        self.root = async_to_streamed_response_wrapper(
            testing.root,
        )
