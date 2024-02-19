# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

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
from ...types.names import DiscriminatedUnion, VariantsSinglePropObjects
from ..._base_client import (
    make_request_options,
)

__all__ = ["Unions", "AsyncUnions"]


class Unions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnionsWithRawResponse:
        return UnionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnionsWithStreamingResponse:
        return UnionsWithStreamingResponse(self)

    def discriminated(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscriminatedUnion:
        return cast(
            DiscriminatedUnion,
            self._get(
                "/names/unions/discriminated_union",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, DiscriminatedUnion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def variants_single_prop_objects(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantsSinglePropObjects:
        return cast(
            VariantsSinglePropObjects,
            self._get(
                "/names/unions/variants_single_prop_objects",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VariantsSinglePropObjects
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUnions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnionsWithRawResponse:
        return AsyncUnionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnionsWithStreamingResponse:
        return AsyncUnionsWithStreamingResponse(self)

    async def discriminated(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscriminatedUnion:
        return cast(
            DiscriminatedUnion,
            await self._get(
                "/names/unions/discriminated_union",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, DiscriminatedUnion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def variants_single_prop_objects(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantsSinglePropObjects:
        return cast(
            VariantsSinglePropObjects,
            await self._get(
                "/names/unions/variants_single_prop_objects",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VariantsSinglePropObjects
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UnionsWithRawResponse:
    def __init__(self, unions: Unions) -> None:
        self._unions = unions

        self.discriminated = to_raw_response_wrapper(
            unions.discriminated,
        )
        self.variants_single_prop_objects = to_raw_response_wrapper(
            unions.variants_single_prop_objects,
        )


class AsyncUnionsWithRawResponse:
    def __init__(self, unions: AsyncUnions) -> None:
        self._unions = unions

        self.discriminated = async_to_raw_response_wrapper(
            unions.discriminated,
        )
        self.variants_single_prop_objects = async_to_raw_response_wrapper(
            unions.variants_single_prop_objects,
        )


class UnionsWithStreamingResponse:
    def __init__(self, unions: Unions) -> None:
        self._unions = unions

        self.discriminated = to_streamed_response_wrapper(
            unions.discriminated,
        )
        self.variants_single_prop_objects = to_streamed_response_wrapper(
            unions.variants_single_prop_objects,
        )


class AsyncUnionsWithStreamingResponse:
    def __init__(self, unions: AsyncUnions) -> None:
        self._unions = unions

        self.discriminated = async_to_streamed_response_wrapper(
            unions.discriminated,
        )
        self.variants_single_prop_objects = async_to_streamed_response_wrapper(
            unions.variants_single_prop_objects,
        )
