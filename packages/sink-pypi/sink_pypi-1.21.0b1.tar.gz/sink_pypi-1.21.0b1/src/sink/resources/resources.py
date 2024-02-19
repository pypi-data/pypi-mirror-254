# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["Resources", "AsyncResources"]


class Resources(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesWithRawResponse:
        return ResourcesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesWithStreamingResponse:
        return ResourcesWithStreamingResponse(self)

    def foo(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Endpoint returning no response"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/no_response",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncResources(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesWithRawResponse:
        return AsyncResourcesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesWithStreamingResponse:
        return AsyncResourcesWithStreamingResponse(self)

    async def foo(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Endpoint returning no response"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/no_response",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class ResourcesWithRawResponse:
    def __init__(self, resources: Resources) -> None:
        self._resources = resources

        self.foo = to_raw_response_wrapper(
            resources.foo,
        )


class AsyncResourcesWithRawResponse:
    def __init__(self, resources: AsyncResources) -> None:
        self._resources = resources

        self.foo = async_to_raw_response_wrapper(
            resources.foo,
        )


class ResourcesWithStreamingResponse:
    def __init__(self, resources: Resources) -> None:
        self._resources = resources

        self.foo = to_streamed_response_wrapper(
            resources.foo,
        )


class AsyncResourcesWithStreamingResponse:
    def __init__(self, resources: AsyncResources) -> None:
        self._resources = resources

        self.foo = async_to_streamed_response_wrapper(
            resources.foo,
        )
