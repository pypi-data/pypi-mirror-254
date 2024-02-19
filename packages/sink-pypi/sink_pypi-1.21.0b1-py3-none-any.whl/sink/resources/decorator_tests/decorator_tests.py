# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...types import DecoratorTestKeepMeResponse
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .languages import (
    Languages,
    AsyncLanguages,
    LanguagesWithRawResponse,
    AsyncLanguagesWithRawResponse,
    LanguagesWithStreamingResponse,
    AsyncLanguagesWithStreamingResponse,
)
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
from .keep_this_resource import (
    KeepThisResource,
    AsyncKeepThisResource,
    KeepThisResourceWithRawResponse,
    AsyncKeepThisResourceWithRawResponse,
    KeepThisResourceWithStreamingResponse,
    AsyncKeepThisResourceWithStreamingResponse,
)

__all__ = ["DecoratorTests", "AsyncDecoratorTests"]


class DecoratorTests(SyncAPIResource):
    @cached_property
    def languages(self) -> Languages:
        return Languages(self._client)

    @cached_property
    def keep_this_resource(self) -> KeepThisResource:
        return KeepThisResource(self._client)

    @cached_property
    def with_raw_response(self) -> DecoratorTestsWithRawResponse:
        return DecoratorTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DecoratorTestsWithStreamingResponse:
        return DecoratorTestsWithStreamingResponse(self)

    def keep_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecoratorTestKeepMeResponse:
        """Top-level method that should not be skipped."""
        return self._get(
            "/decorator_tests/keep/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecoratorTestKeepMeResponse,
        )


class AsyncDecoratorTests(AsyncAPIResource):
    @cached_property
    def languages(self) -> AsyncLanguages:
        return AsyncLanguages(self._client)

    @cached_property
    def keep_this_resource(self) -> AsyncKeepThisResource:
        return AsyncKeepThisResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDecoratorTestsWithRawResponse:
        return AsyncDecoratorTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDecoratorTestsWithStreamingResponse:
        return AsyncDecoratorTestsWithStreamingResponse(self)

    async def keep_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecoratorTestKeepMeResponse:
        """Top-level method that should not be skipped."""
        return await self._get(
            "/decorator_tests/keep/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecoratorTestKeepMeResponse,
        )


class DecoratorTestsWithRawResponse:
    def __init__(self, decorator_tests: DecoratorTests) -> None:
        self._decorator_tests = decorator_tests

        self.keep_me = to_raw_response_wrapper(
            decorator_tests.keep_me,
        )

    @cached_property
    def languages(self) -> LanguagesWithRawResponse:
        return LanguagesWithRawResponse(self._decorator_tests.languages)

    @cached_property
    def keep_this_resource(self) -> KeepThisResourceWithRawResponse:
        return KeepThisResourceWithRawResponse(self._decorator_tests.keep_this_resource)


class AsyncDecoratorTestsWithRawResponse:
    def __init__(self, decorator_tests: AsyncDecoratorTests) -> None:
        self._decorator_tests = decorator_tests

        self.keep_me = async_to_raw_response_wrapper(
            decorator_tests.keep_me,
        )

    @cached_property
    def languages(self) -> AsyncLanguagesWithRawResponse:
        return AsyncLanguagesWithRawResponse(self._decorator_tests.languages)

    @cached_property
    def keep_this_resource(self) -> AsyncKeepThisResourceWithRawResponse:
        return AsyncKeepThisResourceWithRawResponse(self._decorator_tests.keep_this_resource)


class DecoratorTestsWithStreamingResponse:
    def __init__(self, decorator_tests: DecoratorTests) -> None:
        self._decorator_tests = decorator_tests

        self.keep_me = to_streamed_response_wrapper(
            decorator_tests.keep_me,
        )

    @cached_property
    def languages(self) -> LanguagesWithStreamingResponse:
        return LanguagesWithStreamingResponse(self._decorator_tests.languages)

    @cached_property
    def keep_this_resource(self) -> KeepThisResourceWithStreamingResponse:
        return KeepThisResourceWithStreamingResponse(self._decorator_tests.keep_this_resource)


class AsyncDecoratorTestsWithStreamingResponse:
    def __init__(self, decorator_tests: AsyncDecoratorTests) -> None:
        self._decorator_tests = decorator_tests

        self.keep_me = async_to_streamed_response_wrapper(
            decorator_tests.keep_me,
        )

    @cached_property
    def languages(self) -> AsyncLanguagesWithStreamingResponse:
        return AsyncLanguagesWithStreamingResponse(self._decorator_tests.languages)

    @cached_property
    def keep_this_resource(self) -> AsyncKeepThisResourceWithStreamingResponse:
        return AsyncKeepThisResourceWithStreamingResponse(self._decorator_tests.keep_this_resource)
