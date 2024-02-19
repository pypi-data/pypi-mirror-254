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
from ...types.decorator_tests import KeepThisResourceKeepThisMethodResponse

__all__ = ["KeepThisResource", "AsyncKeepThisResource"]


class KeepThisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeepThisResourceWithRawResponse:
        return KeepThisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeepThisResourceWithStreamingResponse:
        return KeepThisResourceWithStreamingResponse(self)

    def keep_this_method(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeepThisResourceKeepThisMethodResponse:
        """
        Nested method that should render because it is not skipped nor are its
        ancestors.
        """
        return self._get(
            "/decorator_tests/nested/keep/this/method",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeepThisResourceKeepThisMethodResponse,
        )


class AsyncKeepThisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeepThisResourceWithRawResponse:
        return AsyncKeepThisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeepThisResourceWithStreamingResponse:
        return AsyncKeepThisResourceWithStreamingResponse(self)

    async def keep_this_method(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeepThisResourceKeepThisMethodResponse:
        """
        Nested method that should render because it is not skipped nor are its
        ancestors.
        """
        return await self._get(
            "/decorator_tests/nested/keep/this/method",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeepThisResourceKeepThisMethodResponse,
        )


class KeepThisResourceWithRawResponse:
    def __init__(self, keep_this_resource: KeepThisResource) -> None:
        self._keep_this_resource = keep_this_resource

        self.keep_this_method = to_raw_response_wrapper(
            keep_this_resource.keep_this_method,
        )


class AsyncKeepThisResourceWithRawResponse:
    def __init__(self, keep_this_resource: AsyncKeepThisResource) -> None:
        self._keep_this_resource = keep_this_resource

        self.keep_this_method = async_to_raw_response_wrapper(
            keep_this_resource.keep_this_method,
        )


class KeepThisResourceWithStreamingResponse:
    def __init__(self, keep_this_resource: KeepThisResource) -> None:
        self._keep_this_resource = keep_this_resource

        self.keep_this_method = to_streamed_response_wrapper(
            keep_this_resource.keep_this_method,
        )


class AsyncKeepThisResourceWithStreamingResponse:
    def __init__(self, keep_this_resource: AsyncKeepThisResource) -> None:
        self._keep_this_resource = keep_this_resource

        self.keep_this_method = async_to_streamed_response_wrapper(
            keep_this_resource.keep_this_method,
        )
