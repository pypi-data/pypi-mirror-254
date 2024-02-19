# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import MakeAmbiguousSchemasLooserMakeAmbiguousSchemasLooserResponse
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

__all__ = ["MakeAmbiguousSchemasLooser", "AsyncMakeAmbiguousSchemasLooser"]


class MakeAmbiguousSchemasLooser(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MakeAmbiguousSchemasLooserWithRawResponse:
        return MakeAmbiguousSchemasLooserWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MakeAmbiguousSchemasLooserWithStreamingResponse:
        return MakeAmbiguousSchemasLooserWithStreamingResponse(self)

    def make_ambiguous_schemas_looser(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MakeAmbiguousSchemasLooserMakeAmbiguousSchemasLooserResponse:
        """Test case for makeAmbiguousSchemasLooser"""
        return self._get(
            "/make-ambiguous-schemas-looser",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MakeAmbiguousSchemasLooserMakeAmbiguousSchemasLooserResponse,
        )


class AsyncMakeAmbiguousSchemasLooser(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMakeAmbiguousSchemasLooserWithRawResponse:
        return AsyncMakeAmbiguousSchemasLooserWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMakeAmbiguousSchemasLooserWithStreamingResponse:
        return AsyncMakeAmbiguousSchemasLooserWithStreamingResponse(self)

    async def make_ambiguous_schemas_looser(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MakeAmbiguousSchemasLooserMakeAmbiguousSchemasLooserResponse:
        """Test case for makeAmbiguousSchemasLooser"""
        return await self._get(
            "/make-ambiguous-schemas-looser",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MakeAmbiguousSchemasLooserMakeAmbiguousSchemasLooserResponse,
        )


class MakeAmbiguousSchemasLooserWithRawResponse:
    def __init__(self, make_ambiguous_schemas_looser: MakeAmbiguousSchemasLooser) -> None:
        self._make_ambiguous_schemas_looser = make_ambiguous_schemas_looser

        self.make_ambiguous_schemas_looser = to_raw_response_wrapper(
            make_ambiguous_schemas_looser.make_ambiguous_schemas_looser,
        )


class AsyncMakeAmbiguousSchemasLooserWithRawResponse:
    def __init__(self, make_ambiguous_schemas_looser: AsyncMakeAmbiguousSchemasLooser) -> None:
        self._make_ambiguous_schemas_looser = make_ambiguous_schemas_looser

        self.make_ambiguous_schemas_looser = async_to_raw_response_wrapper(
            make_ambiguous_schemas_looser.make_ambiguous_schemas_looser,
        )


class MakeAmbiguousSchemasLooserWithStreamingResponse:
    def __init__(self, make_ambiguous_schemas_looser: MakeAmbiguousSchemasLooser) -> None:
        self._make_ambiguous_schemas_looser = make_ambiguous_schemas_looser

        self.make_ambiguous_schemas_looser = to_streamed_response_wrapper(
            make_ambiguous_schemas_looser.make_ambiguous_schemas_looser,
        )


class AsyncMakeAmbiguousSchemasLooserWithStreamingResponse:
    def __init__(self, make_ambiguous_schemas_looser: AsyncMakeAmbiguousSchemasLooser) -> None:
        self._make_ambiguous_schemas_looser = make_ambiguous_schemas_looser

        self.make_ambiguous_schemas_looser = async_to_streamed_response_wrapper(
            make_ambiguous_schemas_looser.make_ambiguous_schemas_looser,
        )
