# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["Tests", "AsyncTests"]


class Tests(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestsWithRawResponse:
        return TestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsWithStreamingResponse:
        return TestsWithStreamingResponse(self)

    def run_codegen(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Testing codegen change with new Github action"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/tests/run_codegen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestsWithRawResponse:
        return AsyncTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsWithStreamingResponse:
        return AsyncTestsWithStreamingResponse(self)

    async def run_codegen(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Testing codegen change with new Github action"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/tests/run_codegen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TestsWithRawResponse:
    __test__ = False

    def __init__(self, tests: Tests) -> None:
        self._tests = tests

        self.run_codegen = to_raw_response_wrapper(
            tests.run_codegen,
        )


class AsyncTestsWithRawResponse:
    def __init__(self, tests: AsyncTests) -> None:
        self._tests = tests

        self.run_codegen = async_to_raw_response_wrapper(
            tests.run_codegen,
        )


class TestsWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: Tests) -> None:
        self._tests = tests

        self.run_codegen = to_streamed_response_wrapper(
            tests.run_codegen,
        )


class AsyncTestsWithStreamingResponse:
    def __init__(self, tests: AsyncTests) -> None:
        self._tests = tests

        self.run_codegen = async_to_streamed_response_wrapper(
            tests.run_codegen,
        )
