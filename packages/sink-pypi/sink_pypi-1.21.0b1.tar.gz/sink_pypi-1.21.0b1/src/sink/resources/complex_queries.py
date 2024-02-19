# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import (
    ComplexQueryArrayQueryResponse,
    ComplexQueryObjectQueryResponse,
    complex_query_array_query_params,
    complex_query_object_query_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
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

__all__ = ["ComplexQueries", "AsyncComplexQueries"]


class ComplexQueries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComplexQueriesWithRawResponse:
        return ComplexQueriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComplexQueriesWithStreamingResponse:
        return ComplexQueriesWithStreamingResponse(self)

    def array_query(
        self,
        *,
        include: List[Literal["users", "users.comments", "users.posts"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ComplexQueryArrayQueryResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/array_query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include}, complex_query_array_query_params.ComplexQueryArrayQueryParams
                ),
            ),
            cast_to=ComplexQueryArrayQueryResponse,
        )

    def object_query(
        self,
        *,
        include: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ComplexQueryObjectQueryResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/object_query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include}, complex_query_object_query_params.ComplexQueryObjectQueryParams
                ),
            ),
            cast_to=ComplexQueryObjectQueryResponse,
        )


class AsyncComplexQueries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComplexQueriesWithRawResponse:
        return AsyncComplexQueriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComplexQueriesWithStreamingResponse:
        return AsyncComplexQueriesWithStreamingResponse(self)

    async def array_query(
        self,
        *,
        include: List[Literal["users", "users.comments", "users.posts"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ComplexQueryArrayQueryResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/array_query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include}, complex_query_array_query_params.ComplexQueryArrayQueryParams
                ),
            ),
            cast_to=ComplexQueryArrayQueryResponse,
        )

    async def object_query(
        self,
        *,
        include: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ComplexQueryObjectQueryResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/object_query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include}, complex_query_object_query_params.ComplexQueryObjectQueryParams
                ),
            ),
            cast_to=ComplexQueryObjectQueryResponse,
        )


class ComplexQueriesWithRawResponse:
    def __init__(self, complex_queries: ComplexQueries) -> None:
        self._complex_queries = complex_queries

        self.array_query = to_raw_response_wrapper(
            complex_queries.array_query,
        )
        self.object_query = to_raw_response_wrapper(
            complex_queries.object_query,
        )


class AsyncComplexQueriesWithRawResponse:
    def __init__(self, complex_queries: AsyncComplexQueries) -> None:
        self._complex_queries = complex_queries

        self.array_query = async_to_raw_response_wrapper(
            complex_queries.array_query,
        )
        self.object_query = async_to_raw_response_wrapper(
            complex_queries.object_query,
        )


class ComplexQueriesWithStreamingResponse:
    def __init__(self, complex_queries: ComplexQueries) -> None:
        self._complex_queries = complex_queries

        self.array_query = to_streamed_response_wrapper(
            complex_queries.array_query,
        )
        self.object_query = to_streamed_response_wrapper(
            complex_queries.object_query,
        )


class AsyncComplexQueriesWithStreamingResponse:
    def __init__(self, complex_queries: AsyncComplexQueries) -> None:
        self._complex_queries = complex_queries

        self.array_query = async_to_streamed_response_wrapper(
            complex_queries.array_query,
        )
        self.object_query = async_to_streamed_response_wrapper(
            complex_queries.object_query,
        )
