# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import PathParamMultipleResponse, PathParamSingularResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.shared import BasicSharedModelObject

__all__ = ["PathParams", "AsyncPathParams"]


class PathParams(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PathParamsWithRawResponse:
        return PathParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PathParamsWithStreamingResponse:
        return PathParamsWithStreamingResponse(self)

    def dashed_param(
        self,
        dashed_param: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that uses a `dash` separator.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not dashed_param:
            raise ValueError(f"Expected a non-empty value for `dashed_param` but received {dashed_param!r}")
        return self._post(
            f"/path_params/{dashed_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    def date_param(
        self,
        date_param: Union[str, date],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is a date type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not date_param:
            raise ValueError(f"Expected a non-empty value for `date_param` but received {date_param!r}")
        return self._post(
            f"/path_params/dates/{date_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    def datetime_param(
        self,
        datetime_param: Union[str, datetime],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is a date-time type.

        Args:
          datetime_param: An ISO 8601 timestamp for when the card was created. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not datetime_param:
            raise ValueError(f"Expected a non-empty value for `datetime_param` but received {datetime_param!r}")
        return self._post(
            f"/path_params/date_times/{datetime_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    def enum_param(
        self,
        enum_param: Literal["A", "B", "C"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is an enum type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not enum_param:
            raise ValueError(f"Expected a non-empty value for `enum_param` but received {enum_param!r}")
        return self._post(
            f"/path_params/enums/{enum_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    def integer_param(
        self,
        integer_param: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is of an integer type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/path_params/{integer_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    def multiple(
        self,
        last: str,
        *,
        first: str,
        second: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PathParamMultipleResponse:
        """
        Endpoint with multiple path parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not first:
            raise ValueError(f"Expected a non-empty value for `first` but received {first!r}")
        if not second:
            raise ValueError(f"Expected a non-empty value for `second` but received {second!r}")
        if not last:
            raise ValueError(f"Expected a non-empty value for `last` but received {last!r}")
        return self._post(
            f"/path_params/{first}/{second}/{last}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PathParamMultipleResponse,
        )

    def params_mixed_types(
        self,
        string_param: str,
        *,
        integer_param: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """Endpoint with multiple path parameters that are of different types, e.g.

        one
        integer type and the other string type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not string_param:
            raise ValueError(f"Expected a non-empty value for `string_param` but received {string_param!r}")
        return self._post(
            f"/path_params/mixed/{integer_param}/{string_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    def singular(
        self,
        singular: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PathParamSingularResponse:
        """
        Endpoint with a singular path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not singular:
            raise ValueError(f"Expected a non-empty value for `singular` but received {singular!r}")
        return self._post(
            f"/path_params/{singular}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PathParamSingularResponse,
        )


class AsyncPathParams(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPathParamsWithRawResponse:
        return AsyncPathParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPathParamsWithStreamingResponse:
        return AsyncPathParamsWithStreamingResponse(self)

    async def dashed_param(
        self,
        dashed_param: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that uses a `dash` separator.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not dashed_param:
            raise ValueError(f"Expected a non-empty value for `dashed_param` but received {dashed_param!r}")
        return await self._post(
            f"/path_params/{dashed_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    async def date_param(
        self,
        date_param: Union[str, date],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is a date type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not date_param:
            raise ValueError(f"Expected a non-empty value for `date_param` but received {date_param!r}")
        return await self._post(
            f"/path_params/dates/{date_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    async def datetime_param(
        self,
        datetime_param: Union[str, datetime],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is a date-time type.

        Args:
          datetime_param: An ISO 8601 timestamp for when the card was created. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not datetime_param:
            raise ValueError(f"Expected a non-empty value for `datetime_param` but received {datetime_param!r}")
        return await self._post(
            f"/path_params/date_times/{datetime_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    async def enum_param(
        self,
        enum_param: Literal["A", "B", "C"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is an enum type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not enum_param:
            raise ValueError(f"Expected a non-empty value for `enum_param` but received {enum_param!r}")
        return await self._post(
            f"/path_params/enums/{enum_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    async def integer_param(
        self,
        integer_param: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a singular path parameter that is of an integer type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/path_params/{integer_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    async def multiple(
        self,
        last: str,
        *,
        first: str,
        second: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PathParamMultipleResponse:
        """
        Endpoint with multiple path parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not first:
            raise ValueError(f"Expected a non-empty value for `first` but received {first!r}")
        if not second:
            raise ValueError(f"Expected a non-empty value for `second` but received {second!r}")
        if not last:
            raise ValueError(f"Expected a non-empty value for `last` but received {last!r}")
        return await self._post(
            f"/path_params/{first}/{second}/{last}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PathParamMultipleResponse,
        )

    async def params_mixed_types(
        self,
        string_param: str,
        *,
        integer_param: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """Endpoint with multiple path parameters that are of different types, e.g.

        one
        integer type and the other string type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not string_param:
            raise ValueError(f"Expected a non-empty value for `string_param` but received {string_param!r}")
        return await self._post(
            f"/path_params/mixed/{integer_param}/{string_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BasicSharedModelObject,
        )

    async def singular(
        self,
        singular: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PathParamSingularResponse:
        """
        Endpoint with a singular path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not singular:
            raise ValueError(f"Expected a non-empty value for `singular` but received {singular!r}")
        return await self._post(
            f"/path_params/{singular}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PathParamSingularResponse,
        )


class PathParamsWithRawResponse:
    def __init__(self, path_params: PathParams) -> None:
        self._path_params = path_params

        self.dashed_param = to_raw_response_wrapper(
            path_params.dashed_param,
        )
        self.date_param = to_raw_response_wrapper(
            path_params.date_param,
        )
        self.datetime_param = to_raw_response_wrapper(
            path_params.datetime_param,
        )
        self.enum_param = to_raw_response_wrapper(
            path_params.enum_param,
        )
        self.integer_param = to_raw_response_wrapper(
            path_params.integer_param,
        )
        self.multiple = to_raw_response_wrapper(
            path_params.multiple,
        )
        self.params_mixed_types = to_raw_response_wrapper(
            path_params.params_mixed_types,
        )
        self.singular = to_raw_response_wrapper(
            path_params.singular,
        )


class AsyncPathParamsWithRawResponse:
    def __init__(self, path_params: AsyncPathParams) -> None:
        self._path_params = path_params

        self.dashed_param = async_to_raw_response_wrapper(
            path_params.dashed_param,
        )
        self.date_param = async_to_raw_response_wrapper(
            path_params.date_param,
        )
        self.datetime_param = async_to_raw_response_wrapper(
            path_params.datetime_param,
        )
        self.enum_param = async_to_raw_response_wrapper(
            path_params.enum_param,
        )
        self.integer_param = async_to_raw_response_wrapper(
            path_params.integer_param,
        )
        self.multiple = async_to_raw_response_wrapper(
            path_params.multiple,
        )
        self.params_mixed_types = async_to_raw_response_wrapper(
            path_params.params_mixed_types,
        )
        self.singular = async_to_raw_response_wrapper(
            path_params.singular,
        )


class PathParamsWithStreamingResponse:
    def __init__(self, path_params: PathParams) -> None:
        self._path_params = path_params

        self.dashed_param = to_streamed_response_wrapper(
            path_params.dashed_param,
        )
        self.date_param = to_streamed_response_wrapper(
            path_params.date_param,
        )
        self.datetime_param = to_streamed_response_wrapper(
            path_params.datetime_param,
        )
        self.enum_param = to_streamed_response_wrapper(
            path_params.enum_param,
        )
        self.integer_param = to_streamed_response_wrapper(
            path_params.integer_param,
        )
        self.multiple = to_streamed_response_wrapper(
            path_params.multiple,
        )
        self.params_mixed_types = to_streamed_response_wrapper(
            path_params.params_mixed_types,
        )
        self.singular = to_streamed_response_wrapper(
            path_params.singular,
        )


class AsyncPathParamsWithStreamingResponse:
    def __init__(self, path_params: AsyncPathParams) -> None:
        self._path_params = path_params

        self.dashed_param = async_to_streamed_response_wrapper(
            path_params.dashed_param,
        )
        self.date_param = async_to_streamed_response_wrapper(
            path_params.date_param,
        )
        self.datetime_param = async_to_streamed_response_wrapper(
            path_params.datetime_param,
        )
        self.enum_param = async_to_streamed_response_wrapper(
            path_params.enum_param,
        )
        self.integer_param = async_to_streamed_response_wrapper(
            path_params.integer_param,
        )
        self.multiple = async_to_streamed_response_wrapper(
            path_params.multiple,
        )
        self.params_mixed_types = async_to_streamed_response_wrapper(
            path_params.params_mixed_types,
        )
        self.singular = async_to_streamed_response_wrapper(
            path_params.singular,
        )
