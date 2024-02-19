# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

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
from ...types.types import ModelString, PrimitiveStringsResponse, primitive_strings_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Primitives", "AsyncPrimitives"]


class Primitives(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrimitivesWithRawResponse:
        return PrimitivesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrimitivesWithStreamingResponse:
        return PrimitivesWithStreamingResponse(self)

    def strings(
        self,
        *,
        string_param: ModelString | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PrimitiveStringsResponse:
        """
        Endpoint that has a request body property that points to a string model &
        returns an object with a string model prop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/types/primitives/strings",
            body=maybe_transform({"string_param": string_param}, primitive_strings_params.PrimitiveStringsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PrimitiveStringsResponse,
        )


class AsyncPrimitives(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrimitivesWithRawResponse:
        return AsyncPrimitivesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrimitivesWithStreamingResponse:
        return AsyncPrimitivesWithStreamingResponse(self)

    async def strings(
        self,
        *,
        string_param: ModelString | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PrimitiveStringsResponse:
        """
        Endpoint that has a request body property that points to a string model &
        returns an object with a string model prop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/types/primitives/strings",
            body=maybe_transform({"string_param": string_param}, primitive_strings_params.PrimitiveStringsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PrimitiveStringsResponse,
        )


class PrimitivesWithRawResponse:
    def __init__(self, primitives: Primitives) -> None:
        self._primitives = primitives

        self.strings = to_raw_response_wrapper(
            primitives.strings,
        )


class AsyncPrimitivesWithRawResponse:
    def __init__(self, primitives: AsyncPrimitives) -> None:
        self._primitives = primitives

        self.strings = async_to_raw_response_wrapper(
            primitives.strings,
        )


class PrimitivesWithStreamingResponse:
    def __init__(self, primitives: Primitives) -> None:
        self._primitives = primitives

        self.strings = to_streamed_response_wrapper(
            primitives.strings,
        )


class AsyncPrimitivesWithStreamingResponse:
    def __init__(self, primitives: AsyncPrimitives) -> None:
        self._primitives = primitives

        self.strings = async_to_streamed_response_wrapper(
            primitives.strings,
        )
