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
from ...pagination import SyncPageCursor, AsyncPageCursor
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.pagination_tests import cursor_list_params

__all__ = ["Cursor", "AsyncCursor"]


class Cursor(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CursorWithRawResponse:
        return CursorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CursorWithStreamingResponse:
        return CursorWithStreamingResponse(self)

    def list(
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
    ) -> SyncPageCursor[MyModel]:
        """
        Test case for cursor pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor",
            page=SyncPageCursor[MyModel],
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
                    cursor_list_params.CursorListParams,
                ),
            ),
            model=MyModel,
        )


class AsyncCursor(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCursorWithRawResponse:
        return AsyncCursorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCursorWithStreamingResponse:
        return AsyncCursorWithStreamingResponse(self)

    def list(
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
    ) -> AsyncPaginator[MyModel, AsyncPageCursor[MyModel]]:
        """
        Test case for cursor pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/cursor",
            page=AsyncPageCursor[MyModel],
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
                    cursor_list_params.CursorListParams,
                ),
            ),
            model=MyModel,
        )


class CursorWithRawResponse:
    def __init__(self, cursor: Cursor) -> None:
        self._cursor = cursor

        self.list = to_raw_response_wrapper(
            cursor.list,
        )


class AsyncCursorWithRawResponse:
    def __init__(self, cursor: AsyncCursor) -> None:
        self._cursor = cursor

        self.list = async_to_raw_response_wrapper(
            cursor.list,
        )


class CursorWithStreamingResponse:
    def __init__(self, cursor: Cursor) -> None:
        self._cursor = cursor

        self.list = to_streamed_response_wrapper(
            cursor.list,
        )


class AsyncCursorWithStreamingResponse:
    def __init__(self, cursor: AsyncCursor) -> None:
        self._cursor = cursor

        self.list = async_to_streamed_response_wrapper(
            cursor.list,
        )
