# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime

import httpx

from .enums import (
    Enums,
    AsyncEnums,
    EnumsWithRawResponse,
    AsyncEnumsWithRawResponse,
    EnumsWithStreamingResponse,
    AsyncEnumsWithStreamingResponse,
)
from .arrays import (
    Arrays,
    AsyncArrays,
    ArraysWithRawResponse,
    AsyncArraysWithRawResponse,
    ArraysWithStreamingResponse,
    AsyncArraysWithStreamingResponse,
)
from ...types import TypeDatesResponse, TypeDatetimesResponse, type_dates_params, type_datetimes_params
from .objects import (
    Objects,
    AsyncObjects,
    ObjectsWithRawResponse,
    AsyncObjectsWithRawResponse,
    ObjectsWithStreamingResponse,
    AsyncObjectsWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from .primitives import (
    Primitives,
    AsyncPrimitives,
    PrimitivesWithRawResponse,
    AsyncPrimitivesWithRawResponse,
    PrimitivesWithStreamingResponse,
    AsyncPrimitivesWithStreamingResponse,
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
from .read_only_params import (
    ReadOnlyParams,
    AsyncReadOnlyParams,
    ReadOnlyParamsWithRawResponse,
    AsyncReadOnlyParamsWithRawResponse,
    ReadOnlyParamsWithStreamingResponse,
    AsyncReadOnlyParamsWithStreamingResponse,
)
from .write_only_responses import (
    WriteOnlyResponses,
    AsyncWriteOnlyResponses,
    WriteOnlyResponsesWithRawResponse,
    AsyncWriteOnlyResponsesWithRawResponse,
    WriteOnlyResponsesWithStreamingResponse,
    AsyncWriteOnlyResponsesWithStreamingResponse,
)

__all__ = ["Types", "AsyncTypes"]


class Types(SyncAPIResource):
    @cached_property
    def primitives(self) -> Primitives:
        return Primitives(self._client)

    @cached_property
    def read_only_params(self) -> ReadOnlyParams:
        return ReadOnlyParams(self._client)

    @cached_property
    def write_only_responses(self) -> WriteOnlyResponses:
        return WriteOnlyResponses(self._client)

    @cached_property
    def enums(self) -> Enums:
        return Enums(self._client)

    @cached_property
    def objects(self) -> Objects:
        return Objects(self._client)

    @cached_property
    def arrays(self) -> Arrays:
        return Arrays(self._client)

    @cached_property
    def with_raw_response(self) -> TypesWithRawResponse:
        return TypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesWithStreamingResponse:
        return TypesWithStreamingResponse(self)

    def dates(
        self,
        *,
        required_date: Union[str, date],
        required_nullable_date: Union[str, date, None],
        list_date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        oneof_date: Union[Union[str, date], int] | NotGiven = NOT_GIVEN,
        optional_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TypeDatesResponse:
        """
        Endpoint that has date types should generate params/responses with rich date
        types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/types/dates",
            body=maybe_transform(
                {
                    "required_date": required_date,
                    "required_nullable_date": required_nullable_date,
                    "list_date": list_date,
                    "oneof_date": oneof_date,
                    "optional_date": optional_date,
                },
                type_dates_params.TypeDatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TypeDatesResponse,
        )

    def datetimes(
        self,
        *,
        required_datetime: Union[str, datetime],
        required_nullable_datetime: Union[str, datetime, None],
        list_datetime: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        oneof_datetime: Union[Union[str, datetime], int] | NotGiven = NOT_GIVEN,
        optional_datetime: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TypeDatetimesResponse:
        """
        Endpoint that has date-time types.

        Args:
          oneof_datetime: union type coming from the `oneof_datetime` property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/types/datetimes",
            body=maybe_transform(
                {
                    "required_datetime": required_datetime,
                    "required_nullable_datetime": required_nullable_datetime,
                    "list_datetime": list_datetime,
                    "oneof_datetime": oneof_datetime,
                    "optional_datetime": optional_datetime,
                },
                type_datetimes_params.TypeDatetimesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TypeDatetimesResponse,
        )


class AsyncTypes(AsyncAPIResource):
    @cached_property
    def primitives(self) -> AsyncPrimitives:
        return AsyncPrimitives(self._client)

    @cached_property
    def read_only_params(self) -> AsyncReadOnlyParams:
        return AsyncReadOnlyParams(self._client)

    @cached_property
    def write_only_responses(self) -> AsyncWriteOnlyResponses:
        return AsyncWriteOnlyResponses(self._client)

    @cached_property
    def enums(self) -> AsyncEnums:
        return AsyncEnums(self._client)

    @cached_property
    def objects(self) -> AsyncObjects:
        return AsyncObjects(self._client)

    @cached_property
    def arrays(self) -> AsyncArrays:
        return AsyncArrays(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTypesWithRawResponse:
        return AsyncTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesWithStreamingResponse:
        return AsyncTypesWithStreamingResponse(self)

    async def dates(
        self,
        *,
        required_date: Union[str, date],
        required_nullable_date: Union[str, date, None],
        list_date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        oneof_date: Union[Union[str, date], int] | NotGiven = NOT_GIVEN,
        optional_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TypeDatesResponse:
        """
        Endpoint that has date types should generate params/responses with rich date
        types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/types/dates",
            body=maybe_transform(
                {
                    "required_date": required_date,
                    "required_nullable_date": required_nullable_date,
                    "list_date": list_date,
                    "oneof_date": oneof_date,
                    "optional_date": optional_date,
                },
                type_dates_params.TypeDatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TypeDatesResponse,
        )

    async def datetimes(
        self,
        *,
        required_datetime: Union[str, datetime],
        required_nullable_datetime: Union[str, datetime, None],
        list_datetime: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        oneof_datetime: Union[Union[str, datetime], int] | NotGiven = NOT_GIVEN,
        optional_datetime: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TypeDatetimesResponse:
        """
        Endpoint that has date-time types.

        Args:
          oneof_datetime: union type coming from the `oneof_datetime` property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/types/datetimes",
            body=maybe_transform(
                {
                    "required_datetime": required_datetime,
                    "required_nullable_datetime": required_nullable_datetime,
                    "list_datetime": list_datetime,
                    "oneof_datetime": oneof_datetime,
                    "optional_datetime": optional_datetime,
                },
                type_datetimes_params.TypeDatetimesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TypeDatetimesResponse,
        )


class TypesWithRawResponse:
    def __init__(self, types: Types) -> None:
        self._types = types

        self.dates = to_raw_response_wrapper(
            types.dates,
        )
        self.datetimes = to_raw_response_wrapper(
            types.datetimes,
        )

    @cached_property
    def primitives(self) -> PrimitivesWithRawResponse:
        return PrimitivesWithRawResponse(self._types.primitives)

    @cached_property
    def read_only_params(self) -> ReadOnlyParamsWithRawResponse:
        return ReadOnlyParamsWithRawResponse(self._types.read_only_params)

    @cached_property
    def write_only_responses(self) -> WriteOnlyResponsesWithRawResponse:
        return WriteOnlyResponsesWithRawResponse(self._types.write_only_responses)

    @cached_property
    def enums(self) -> EnumsWithRawResponse:
        return EnumsWithRawResponse(self._types.enums)

    @cached_property
    def objects(self) -> ObjectsWithRawResponse:
        return ObjectsWithRawResponse(self._types.objects)

    @cached_property
    def arrays(self) -> ArraysWithRawResponse:
        return ArraysWithRawResponse(self._types.arrays)


class AsyncTypesWithRawResponse:
    def __init__(self, types: AsyncTypes) -> None:
        self._types = types

        self.dates = async_to_raw_response_wrapper(
            types.dates,
        )
        self.datetimes = async_to_raw_response_wrapper(
            types.datetimes,
        )

    @cached_property
    def primitives(self) -> AsyncPrimitivesWithRawResponse:
        return AsyncPrimitivesWithRawResponse(self._types.primitives)

    @cached_property
    def read_only_params(self) -> AsyncReadOnlyParamsWithRawResponse:
        return AsyncReadOnlyParamsWithRawResponse(self._types.read_only_params)

    @cached_property
    def write_only_responses(self) -> AsyncWriteOnlyResponsesWithRawResponse:
        return AsyncWriteOnlyResponsesWithRawResponse(self._types.write_only_responses)

    @cached_property
    def enums(self) -> AsyncEnumsWithRawResponse:
        return AsyncEnumsWithRawResponse(self._types.enums)

    @cached_property
    def objects(self) -> AsyncObjectsWithRawResponse:
        return AsyncObjectsWithRawResponse(self._types.objects)

    @cached_property
    def arrays(self) -> AsyncArraysWithRawResponse:
        return AsyncArraysWithRawResponse(self._types.arrays)


class TypesWithStreamingResponse:
    def __init__(self, types: Types) -> None:
        self._types = types

        self.dates = to_streamed_response_wrapper(
            types.dates,
        )
        self.datetimes = to_streamed_response_wrapper(
            types.datetimes,
        )

    @cached_property
    def primitives(self) -> PrimitivesWithStreamingResponse:
        return PrimitivesWithStreamingResponse(self._types.primitives)

    @cached_property
    def read_only_params(self) -> ReadOnlyParamsWithStreamingResponse:
        return ReadOnlyParamsWithStreamingResponse(self._types.read_only_params)

    @cached_property
    def write_only_responses(self) -> WriteOnlyResponsesWithStreamingResponse:
        return WriteOnlyResponsesWithStreamingResponse(self._types.write_only_responses)

    @cached_property
    def enums(self) -> EnumsWithStreamingResponse:
        return EnumsWithStreamingResponse(self._types.enums)

    @cached_property
    def objects(self) -> ObjectsWithStreamingResponse:
        return ObjectsWithStreamingResponse(self._types.objects)

    @cached_property
    def arrays(self) -> ArraysWithStreamingResponse:
        return ArraysWithStreamingResponse(self._types.arrays)


class AsyncTypesWithStreamingResponse:
    def __init__(self, types: AsyncTypes) -> None:
        self._types = types

        self.dates = async_to_streamed_response_wrapper(
            types.dates,
        )
        self.datetimes = async_to_streamed_response_wrapper(
            types.datetimes,
        )

    @cached_property
    def primitives(self) -> AsyncPrimitivesWithStreamingResponse:
        return AsyncPrimitivesWithStreamingResponse(self._types.primitives)

    @cached_property
    def read_only_params(self) -> AsyncReadOnlyParamsWithStreamingResponse:
        return AsyncReadOnlyParamsWithStreamingResponse(self._types.read_only_params)

    @cached_property
    def write_only_responses(self) -> AsyncWriteOnlyResponsesWithStreamingResponse:
        return AsyncWriteOnlyResponsesWithStreamingResponse(self._types.write_only_responses)

    @cached_property
    def enums(self) -> AsyncEnumsWithStreamingResponse:
        return AsyncEnumsWithStreamingResponse(self._types.enums)

    @cached_property
    def objects(self) -> AsyncObjectsWithStreamingResponse:
        return AsyncObjectsWithStreamingResponse(self._types.objects)

    @cached_property
    def arrays(self) -> AsyncArraysWithStreamingResponse:
        return AsyncArraysWithStreamingResponse(self._types.arrays)
