# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import header_param_client_argument_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["HeaderParams", "AsyncHeaderParams"]


class HeaderParams(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HeaderParamsWithRawResponse:
        return HeaderParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeaderParamsWithStreamingResponse:
        return HeaderParamsWithStreamingResponse(self)

    def client_argument(
        self,
        *,
        foo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        The `X-Client-Secret` header shouldn't be included in params definitions as it
        is already sent as a client argument.

        Whereas the `X-Custom-Endpoint-Header` should be included as it is only used
        here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/header_params/client_argument",
            body=maybe_transform({"foo": foo}, header_param_client_argument_params.HeaderParamClientArgumentParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncHeaderParams(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHeaderParamsWithRawResponse:
        return AsyncHeaderParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeaderParamsWithStreamingResponse:
        return AsyncHeaderParamsWithStreamingResponse(self)

    async def client_argument(
        self,
        *,
        foo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        The `X-Client-Secret` header shouldn't be included in params definitions as it
        is already sent as a client argument.

        Whereas the `X-Custom-Endpoint-Header` should be included as it is only used
        here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/header_params/client_argument",
            body=maybe_transform({"foo": foo}, header_param_client_argument_params.HeaderParamClientArgumentParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class HeaderParamsWithRawResponse:
    def __init__(self, header_params: HeaderParams) -> None:
        self._header_params = header_params

        self.client_argument = to_raw_response_wrapper(
            header_params.client_argument,
        )


class AsyncHeaderParamsWithRawResponse:
    def __init__(self, header_params: AsyncHeaderParams) -> None:
        self._header_params = header_params

        self.client_argument = async_to_raw_response_wrapper(
            header_params.client_argument,
        )


class HeaderParamsWithStreamingResponse:
    def __init__(self, header_params: HeaderParams) -> None:
        self._header_params = header_params

        self.client_argument = to_streamed_response_wrapper(
            header_params.client_argument,
        )


class AsyncHeaderParamsWithStreamingResponse:
    def __init__(self, header_params: AsyncHeaderParams) -> None:
        self._header_params = header_params

        self.client_argument = async_to_streamed_response_wrapper(
            header_params.client_argument,
        )
