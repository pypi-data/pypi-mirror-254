# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.names.reserved_names import Export, method_export_params

__all__ = ["Methods", "AsyncMethods"]


class Methods(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MethodsWithRawResponse:
        return MethodsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MethodsWithStreamingResponse:
        return MethodsWithStreamingResponse(self)

    def export(
        self,
        class_: str,
        *,
        let: str | NotGiven = NOT_GIVEN,
        const: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Export:
        """
        Test reserved word in method name

        Args:
          let: test reserved word in query parameter

          const: test reserved word in body property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not class_:
            raise ValueError(f"Expected a non-empty value for `class_` but received {class_!r}")
        return self._post(
            f"/names/reserved_names/methods/export/{class_}",
            body=maybe_transform({"const": const}, method_export_params.MethodExportParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform({"let": let}, method_export_params.MethodExportParams),
            ),
            cast_to=Export,
        )


class AsyncMethods(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMethodsWithRawResponse:
        return AsyncMethodsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMethodsWithStreamingResponse:
        return AsyncMethodsWithStreamingResponse(self)

    async def export(
        self,
        class_: str,
        *,
        let: str | NotGiven = NOT_GIVEN,
        const: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Export:
        """
        Test reserved word in method name

        Args:
          let: test reserved word in query parameter

          const: test reserved word in body property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not class_:
            raise ValueError(f"Expected a non-empty value for `class_` but received {class_!r}")
        return await self._post(
            f"/names/reserved_names/methods/export/{class_}",
            body=maybe_transform({"const": const}, method_export_params.MethodExportParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform({"let": let}, method_export_params.MethodExportParams),
            ),
            cast_to=Export,
        )


class MethodsWithRawResponse:
    def __init__(self, methods: Methods) -> None:
        self._methods = methods

        self.export = to_raw_response_wrapper(
            methods.export,
        )


class AsyncMethodsWithRawResponse:
    def __init__(self, methods: AsyncMethods) -> None:
        self._methods = methods

        self.export = async_to_raw_response_wrapper(
            methods.export,
        )


class MethodsWithStreamingResponse:
    def __init__(self, methods: Methods) -> None:
        self._methods = methods

        self.export = to_streamed_response_wrapper(
            methods.export,
        )


class AsyncMethodsWithStreamingResponse:
    def __init__(self, methods: AsyncMethods) -> None:
        self._methods = methods

        self.export = async_to_streamed_response_wrapper(
            methods.export,
        )
