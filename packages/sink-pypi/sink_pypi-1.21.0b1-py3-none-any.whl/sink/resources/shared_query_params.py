# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import (
    shared_query_param_delete_params,
    shared_query_param_retrieve_params,
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

__all__ = ["SharedQueryParams", "AsyncSharedQueryParams"]


class SharedQueryParams(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SharedQueryParamsWithRawResponse:
        return SharedQueryParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharedQueryParamsWithStreamingResponse:
        return SharedQueryParamsWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        get1: str | NotGiven = NOT_GIVEN,
        shared1: str | NotGiven = NOT_GIVEN,
        shared2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/json", **(extra_headers or {})}
        return self._get(
            "/shared-query-params",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "get1": get1,
                        "shared1": shared1,
                        "shared2": shared2,
                    },
                    shared_query_param_retrieve_params.SharedQueryParamRetrieveParams,
                ),
            ),
            cast_to=str,
        )

    def delete(
        self,
        *,
        get1: str | NotGiven = NOT_GIVEN,
        shared1: str | NotGiven = NOT_GIVEN,
        shared2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> str:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "application/json", **(extra_headers or {})}
        return self._delete(
            "/shared-query-params",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "get1": get1,
                        "shared1": shared1,
                        "shared2": shared2,
                    },
                    shared_query_param_delete_params.SharedQueryParamDeleteParams,
                ),
            ),
            cast_to=str,
        )


class AsyncSharedQueryParams(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSharedQueryParamsWithRawResponse:
        return AsyncSharedQueryParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharedQueryParamsWithStreamingResponse:
        return AsyncSharedQueryParamsWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        get1: str | NotGiven = NOT_GIVEN,
        shared1: str | NotGiven = NOT_GIVEN,
        shared2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/json", **(extra_headers or {})}
        return await self._get(
            "/shared-query-params",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "get1": get1,
                        "shared1": shared1,
                        "shared2": shared2,
                    },
                    shared_query_param_retrieve_params.SharedQueryParamRetrieveParams,
                ),
            ),
            cast_to=str,
        )

    async def delete(
        self,
        *,
        get1: str | NotGiven = NOT_GIVEN,
        shared1: str | NotGiven = NOT_GIVEN,
        shared2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> str:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "application/json", **(extra_headers or {})}
        return await self._delete(
            "/shared-query-params",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "get1": get1,
                        "shared1": shared1,
                        "shared2": shared2,
                    },
                    shared_query_param_delete_params.SharedQueryParamDeleteParams,
                ),
            ),
            cast_to=str,
        )


class SharedQueryParamsWithRawResponse:
    def __init__(self, shared_query_params: SharedQueryParams) -> None:
        self._shared_query_params = shared_query_params

        self.retrieve = to_raw_response_wrapper(
            shared_query_params.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            shared_query_params.delete,
        )


class AsyncSharedQueryParamsWithRawResponse:
    def __init__(self, shared_query_params: AsyncSharedQueryParams) -> None:
        self._shared_query_params = shared_query_params

        self.retrieve = async_to_raw_response_wrapper(
            shared_query_params.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            shared_query_params.delete,
        )


class SharedQueryParamsWithStreamingResponse:
    def __init__(self, shared_query_params: SharedQueryParams) -> None:
        self._shared_query_params = shared_query_params

        self.retrieve = to_streamed_response_wrapper(
            shared_query_params.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            shared_query_params.delete,
        )


class AsyncSharedQueryParamsWithStreamingResponse:
    def __init__(self, shared_query_params: AsyncSharedQueryParams) -> None:
        self._shared_query_params = shared_query_params

        self.retrieve = async_to_streamed_response_wrapper(
            shared_query_params.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            shared_query_params.delete,
        )
