# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....types import Card
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .level_two import (
    LevelTwo,
    AsyncLevelTwo,
    LevelTwoWithRawResponse,
    AsyncLevelTwoWithRawResponse,
    LevelTwoWithStreamingResponse,
    AsyncLevelTwoWithStreamingResponse,
)
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
from .level_two.level_two import LevelTwo, AsyncLevelTwo

__all__ = ["LevelOne", "AsyncLevelOne"]


class LevelOne(SyncAPIResource):
    @cached_property
    def level_two(self) -> LevelTwo:
        return LevelTwo(self._client)

    @cached_property
    def with_raw_response(self) -> LevelOneWithRawResponse:
        return LevelOneWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LevelOneWithStreamingResponse:
        return LevelOneWithStreamingResponse(self)

    def method_level_1(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._get(
            f"/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )


class AsyncLevelOne(AsyncAPIResource):
    @cached_property
    def level_two(self) -> AsyncLevelTwo:
        return AsyncLevelTwo(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLevelOneWithRawResponse:
        return AsyncLevelOneWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLevelOneWithStreamingResponse:
        return AsyncLevelOneWithStreamingResponse(self)

    async def method_level_1(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._get(
            f"/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )


class LevelOneWithRawResponse:
    def __init__(self, level_one: LevelOne) -> None:
        self._level_one = level_one

        self.method_level_1 = to_raw_response_wrapper(
            level_one.method_level_1,
        )

    @cached_property
    def level_two(self) -> LevelTwoWithRawResponse:
        return LevelTwoWithRawResponse(self._level_one.level_two)


class AsyncLevelOneWithRawResponse:
    def __init__(self, level_one: AsyncLevelOne) -> None:
        self._level_one = level_one

        self.method_level_1 = async_to_raw_response_wrapper(
            level_one.method_level_1,
        )

    @cached_property
    def level_two(self) -> AsyncLevelTwoWithRawResponse:
        return AsyncLevelTwoWithRawResponse(self._level_one.level_two)


class LevelOneWithStreamingResponse:
    def __init__(self, level_one: LevelOne) -> None:
        self._level_one = level_one

        self.method_level_1 = to_streamed_response_wrapper(
            level_one.method_level_1,
        )

    @cached_property
    def level_two(self) -> LevelTwoWithStreamingResponse:
        return LevelTwoWithStreamingResponse(self._level_one.level_two)


class AsyncLevelOneWithStreamingResponse:
    def __init__(self, level_one: AsyncLevelOne) -> None:
        self._level_one = level_one

        self.method_level_1 = async_to_streamed_response_wrapper(
            level_one.method_level_1,
        )

    @cached_property
    def level_two(self) -> AsyncLevelTwoWithStreamingResponse:
        return AsyncLevelTwoWithStreamingResponse(self._level_one.level_two)
