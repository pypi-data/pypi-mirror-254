# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
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
from ...types.body_params import ModelNewTypeString, union_param_union_enum_new_type_params

__all__ = ["Unions", "AsyncUnions"]


class Unions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnionsWithRawResponse:
        return UnionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnionsWithStreamingResponse:
        return UnionsWithStreamingResponse(self)

    def param_union_enum_new_type(
        self,
        *,
        model: Union[ModelNewTypeString, Literal["gpt-4", "gpt-3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Defines a request parameter that is configured to generate a `NewType` type in
        Python and is used in a union type alongside an enum.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/body_params/unions/param_union_enum_new_type",
            body=maybe_transform(
                {"model": model}, union_param_union_enum_new_type_params.UnionParamUnionEnumNewTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncUnions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnionsWithRawResponse:
        return AsyncUnionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnionsWithStreamingResponse:
        return AsyncUnionsWithStreamingResponse(self)

    async def param_union_enum_new_type(
        self,
        *,
        model: Union[ModelNewTypeString, Literal["gpt-4", "gpt-3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Defines a request parameter that is configured to generate a `NewType` type in
        Python and is used in a union type alongside an enum.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/body_params/unions/param_union_enum_new_type",
            body=maybe_transform(
                {"model": model}, union_param_union_enum_new_type_params.UnionParamUnionEnumNewTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class UnionsWithRawResponse:
    def __init__(self, unions: Unions) -> None:
        self._unions = unions

        self.param_union_enum_new_type = to_raw_response_wrapper(
            unions.param_union_enum_new_type,
        )


class AsyncUnionsWithRawResponse:
    def __init__(self, unions: AsyncUnions) -> None:
        self._unions = unions

        self.param_union_enum_new_type = async_to_raw_response_wrapper(
            unions.param_union_enum_new_type,
        )


class UnionsWithStreamingResponse:
    def __init__(self, unions: Unions) -> None:
        self._unions = unions

        self.param_union_enum_new_type = to_streamed_response_wrapper(
            unions.param_union_enum_new_type,
        )


class AsyncUnionsWithStreamingResponse:
    def __init__(self, unions: AsyncUnions) -> None:
        self._unions = unions

        self.param_union_enum_new_type = async_to_streamed_response_wrapper(
            unions.param_union_enum_new_type,
        )
