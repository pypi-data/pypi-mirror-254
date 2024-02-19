# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

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
from ...types.types import WriteOnlyResponseSimpleResponse
from ..._base_client import (
    make_request_options,
)

__all__ = ["WriteOnlyResponses", "AsyncWriteOnlyResponses"]


class WriteOnlyResponses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WriteOnlyResponsesWithRawResponse:
        return WriteOnlyResponsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WriteOnlyResponsesWithStreamingResponse:
        return WriteOnlyResponsesWithStreamingResponse(self)

    def simple(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WriteOnlyResponseSimpleResponse:
        """Endpoint with a response schema object that contains a `writeOnly` property."""
        return self._get(
            "/types/write_only_responses/simple",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WriteOnlyResponseSimpleResponse,
        )


class AsyncWriteOnlyResponses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWriteOnlyResponsesWithRawResponse:
        return AsyncWriteOnlyResponsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWriteOnlyResponsesWithStreamingResponse:
        return AsyncWriteOnlyResponsesWithStreamingResponse(self)

    async def simple(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WriteOnlyResponseSimpleResponse:
        """Endpoint with a response schema object that contains a `writeOnly` property."""
        return await self._get(
            "/types/write_only_responses/simple",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WriteOnlyResponseSimpleResponse,
        )


class WriteOnlyResponsesWithRawResponse:
    def __init__(self, write_only_responses: WriteOnlyResponses) -> None:
        self._write_only_responses = write_only_responses

        self.simple = to_raw_response_wrapper(
            write_only_responses.simple,
        )


class AsyncWriteOnlyResponsesWithRawResponse:
    def __init__(self, write_only_responses: AsyncWriteOnlyResponses) -> None:
        self._write_only_responses = write_only_responses

        self.simple = async_to_raw_response_wrapper(
            write_only_responses.simple,
        )


class WriteOnlyResponsesWithStreamingResponse:
    def __init__(self, write_only_responses: WriteOnlyResponses) -> None:
        self._write_only_responses = write_only_responses

        self.simple = to_streamed_response_wrapper(
            write_only_responses.simple,
        )


class AsyncWriteOnlyResponsesWithStreamingResponse:
    def __init__(self, write_only_responses: AsyncWriteOnlyResponses) -> None:
        self._write_only_responses = write_only_responses

        self.simple = async_to_streamed_response_wrapper(
            write_only_responses.simple,
        )
