# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .....types import Card
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from .level_three import (
    LevelThree,
    AsyncLevelThree,
    LevelThreeWithRawResponse,
    AsyncLevelThreeWithRawResponse,
    LevelThreeWithStreamingResponse,
    AsyncLevelThreeWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import (
    make_request_options,
)

__all__ = ["LevelTwo", "AsyncLevelTwo"]


class LevelTwo(SyncAPIResource):
    @cached_property
    def level_three(self) -> LevelThree:
        return LevelThree(self._client)

    @cached_property
    def with_raw_response(self) -> LevelTwoWithRawResponse:
        return LevelTwoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LevelTwoWithStreamingResponse:
        return LevelTwoWithStreamingResponse(self)

    def method_level_2(
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


class AsyncLevelTwo(AsyncAPIResource):
    @cached_property
    def level_three(self) -> AsyncLevelThree:
        return AsyncLevelThree(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLevelTwoWithRawResponse:
        return AsyncLevelTwoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLevelTwoWithStreamingResponse:
        return AsyncLevelTwoWithStreamingResponse(self)

    async def method_level_2(
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


class LevelTwoWithRawResponse:
    def __init__(self, level_two: LevelTwo) -> None:
        self._level_two = level_two

        self.method_level_2 = to_raw_response_wrapper(
            level_two.method_level_2,
        )

    @cached_property
    def level_three(self) -> LevelThreeWithRawResponse:
        return LevelThreeWithRawResponse(self._level_two.level_three)


class AsyncLevelTwoWithRawResponse:
    def __init__(self, level_two: AsyncLevelTwo) -> None:
        self._level_two = level_two

        self.method_level_2 = async_to_raw_response_wrapper(
            level_two.method_level_2,
        )

    @cached_property
    def level_three(self) -> AsyncLevelThreeWithRawResponse:
        return AsyncLevelThreeWithRawResponse(self._level_two.level_three)


class LevelTwoWithStreamingResponse:
    def __init__(self, level_two: LevelTwo) -> None:
        self._level_two = level_two

        self.method_level_2 = to_streamed_response_wrapper(
            level_two.method_level_2,
        )

    @cached_property
    def level_three(self) -> LevelThreeWithStreamingResponse:
        return LevelThreeWithStreamingResponse(self._level_two.level_three)


class AsyncLevelTwoWithStreamingResponse:
    def __init__(self, level_two: AsyncLevelTwo) -> None:
        self._level_two = level_two

        self.method_level_2 = async_to_streamed_response_wrapper(
            level_two.method_level_2,
        )

    @cached_property
    def level_three(self) -> AsyncLevelThreeWithStreamingResponse:
        return AsyncLevelThreeWithStreamingResponse(self._level_two.level_three)
