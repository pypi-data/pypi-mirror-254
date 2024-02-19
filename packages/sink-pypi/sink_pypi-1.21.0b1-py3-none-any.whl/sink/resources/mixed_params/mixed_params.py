# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...types import mixed_param_query_and_body_params, mixed_param_query_body_and_path_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from .duplicates import (
    Duplicates,
    AsyncDuplicates,
    DuplicatesWithRawResponse,
    AsyncDuplicatesWithRawResponse,
    DuplicatesWithStreamingResponse,
    AsyncDuplicatesWithStreamingResponse,
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
from ...types.shared import BasicSharedModelObject

__all__ = ["MixedParams", "AsyncMixedParams"]


class MixedParams(SyncAPIResource):
    @cached_property
    def duplicates(self) -> Duplicates:
        return Duplicates(self._client)

    @cached_property
    def with_raw_response(self) -> MixedParamsWithRawResponse:
        return MixedParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MixedParamsWithStreamingResponse:
        return MixedParamsWithStreamingResponse(self)

    def query_and_body(
        self,
        *,
        query_param: str | NotGiven = NOT_GIVEN,
        body_param: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a `requestBody` that defines both query and body params

        Args:
          query_param: Query param description

          body_param: Body param description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/mixed_params/query_and_body",
            body=maybe_transform(
                {"body_param": body_param}, mixed_param_query_and_body_params.MixedParamQueryAndBodyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {"query_param": query_param}, mixed_param_query_and_body_params.MixedParamQueryAndBodyParams
                ),
            ),
            cast_to=BasicSharedModelObject,
        )

    def query_body_and_path(
        self,
        path_param: str | NotGiven = NOT_GIVEN,
        *,
        query_param: str | NotGiven = NOT_GIVEN,
        body_param: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a `requestBody` that defines query, body and path params

        Args:
          query_param: Query param description

          body_param: Body param description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not path_param:
            raise ValueError(f"Expected a non-empty value for `path_param` but received {path_param!r}")
        return self._post(
            f"/mixed_params/query_body_and_path/{path_param}",
            body=maybe_transform(
                {"body_param": body_param}, mixed_param_query_body_and_path_params.MixedParamQueryBodyAndPathParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {"query_param": query_param},
                    mixed_param_query_body_and_path_params.MixedParamQueryBodyAndPathParams,
                ),
            ),
            cast_to=BasicSharedModelObject,
        )


class AsyncMixedParams(AsyncAPIResource):
    @cached_property
    def duplicates(self) -> AsyncDuplicates:
        return AsyncDuplicates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMixedParamsWithRawResponse:
        return AsyncMixedParamsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMixedParamsWithStreamingResponse:
        return AsyncMixedParamsWithStreamingResponse(self)

    async def query_and_body(
        self,
        *,
        query_param: str | NotGiven = NOT_GIVEN,
        body_param: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a `requestBody` that defines both query and body params

        Args:
          query_param: Query param description

          body_param: Body param description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/mixed_params/query_and_body",
            body=maybe_transform(
                {"body_param": body_param}, mixed_param_query_and_body_params.MixedParamQueryAndBodyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {"query_param": query_param}, mixed_param_query_and_body_params.MixedParamQueryAndBodyParams
                ),
            ),
            cast_to=BasicSharedModelObject,
        )

    async def query_body_and_path(
        self,
        path_param: str | NotGiven = NOT_GIVEN,
        *,
        query_param: str | NotGiven = NOT_GIVEN,
        body_param: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BasicSharedModelObject:
        """
        Endpoint with a `requestBody` that defines query, body and path params

        Args:
          query_param: Query param description

          body_param: Body param description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not path_param:
            raise ValueError(f"Expected a non-empty value for `path_param` but received {path_param!r}")
        return await self._post(
            f"/mixed_params/query_body_and_path/{path_param}",
            body=maybe_transform(
                {"body_param": body_param}, mixed_param_query_body_and_path_params.MixedParamQueryBodyAndPathParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {"query_param": query_param},
                    mixed_param_query_body_and_path_params.MixedParamQueryBodyAndPathParams,
                ),
            ),
            cast_to=BasicSharedModelObject,
        )


class MixedParamsWithRawResponse:
    def __init__(self, mixed_params: MixedParams) -> None:
        self._mixed_params = mixed_params

        self.query_and_body = to_raw_response_wrapper(
            mixed_params.query_and_body,
        )
        self.query_body_and_path = to_raw_response_wrapper(
            mixed_params.query_body_and_path,
        )

    @cached_property
    def duplicates(self) -> DuplicatesWithRawResponse:
        return DuplicatesWithRawResponse(self._mixed_params.duplicates)


class AsyncMixedParamsWithRawResponse:
    def __init__(self, mixed_params: AsyncMixedParams) -> None:
        self._mixed_params = mixed_params

        self.query_and_body = async_to_raw_response_wrapper(
            mixed_params.query_and_body,
        )
        self.query_body_and_path = async_to_raw_response_wrapper(
            mixed_params.query_body_and_path,
        )

    @cached_property
    def duplicates(self) -> AsyncDuplicatesWithRawResponse:
        return AsyncDuplicatesWithRawResponse(self._mixed_params.duplicates)


class MixedParamsWithStreamingResponse:
    def __init__(self, mixed_params: MixedParams) -> None:
        self._mixed_params = mixed_params

        self.query_and_body = to_streamed_response_wrapper(
            mixed_params.query_and_body,
        )
        self.query_body_and_path = to_streamed_response_wrapper(
            mixed_params.query_body_and_path,
        )

    @cached_property
    def duplicates(self) -> DuplicatesWithStreamingResponse:
        return DuplicatesWithStreamingResponse(self._mixed_params.duplicates)


class AsyncMixedParamsWithStreamingResponse:
    def __init__(self, mixed_params: AsyncMixedParams) -> None:
        self._mixed_params = mixed_params

        self.query_and_body = async_to_streamed_response_wrapper(
            mixed_params.query_and_body,
        )
        self.query_body_and_path = async_to_streamed_response_wrapper(
            mixed_params.query_body_and_path,
        )

    @cached_property
    def duplicates(self) -> AsyncDuplicatesWithStreamingResponse:
        return AsyncDuplicatesWithStreamingResponse(self._mixed_params.duplicates)
