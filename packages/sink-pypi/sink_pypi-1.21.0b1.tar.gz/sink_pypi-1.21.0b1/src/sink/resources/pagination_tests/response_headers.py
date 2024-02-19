# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import MyModel
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPageCursorFromHeaders, AsyncPageCursorFromHeaders
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.pagination_tests import response_header_basic_cursor_params

__all__ = ["ResponseHeaders", "AsyncResponseHeaders"]


class ResponseHeaders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponseHeadersWithRawResponse:
        return ResponseHeadersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseHeadersWithStreamingResponse:
        return ResponseHeadersWithStreamingResponse(self)

    def basic_cursor(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageCursorFromHeaders[MyModel]:
        """
        Test case for response headers with cursor pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/response_headers/basic_cursor",
            page=SyncPageCursorFromHeaders[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    response_header_basic_cursor_params.ResponseHeaderBasicCursorParams,
                ),
            ),
            model=MyModel,
        )


class AsyncResponseHeaders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponseHeadersWithRawResponse:
        return AsyncResponseHeadersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseHeadersWithStreamingResponse:
        return AsyncResponseHeadersWithStreamingResponse(self)

    def basic_cursor(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageCursorFromHeaders[MyModel]]:
        """
        Test case for response headers with cursor pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/response_headers/basic_cursor",
            page=AsyncPageCursorFromHeaders[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    response_header_basic_cursor_params.ResponseHeaderBasicCursorParams,
                ),
            ),
            model=MyModel,
        )


class ResponseHeadersWithRawResponse:
    def __init__(self, response_headers: ResponseHeaders) -> None:
        self._response_headers = response_headers

        self.basic_cursor = to_raw_response_wrapper(
            response_headers.basic_cursor,
        )


class AsyncResponseHeadersWithRawResponse:
    def __init__(self, response_headers: AsyncResponseHeaders) -> None:
        self._response_headers = response_headers

        self.basic_cursor = async_to_raw_response_wrapper(
            response_headers.basic_cursor,
        )


class ResponseHeadersWithStreamingResponse:
    def __init__(self, response_headers: ResponseHeaders) -> None:
        self._response_headers = response_headers

        self.basic_cursor = to_streamed_response_wrapper(
            response_headers.basic_cursor,
        )


class AsyncResponseHeadersWithStreamingResponse:
    def __init__(self, response_headers: AsyncResponseHeaders) -> None:
        self._response_headers = response_headers

        self.basic_cursor = async_to_streamed_response_wrapper(
            response_headers.basic_cursor,
        )
