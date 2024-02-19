# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .shared_responses import (
    SharedResponses,
    AsyncSharedResponses,
    SharedResponsesWithRawResponse,
    AsyncSharedResponsesWithRawResponse,
    SharedResponsesWithStreamingResponse,
    AsyncSharedResponsesWithStreamingResponse,
)

__all__ = ["Recursion", "AsyncRecursion"]


class Recursion(SyncAPIResource):
    @cached_property
    def shared_responses(self) -> SharedResponses:
        return SharedResponses(self._client)

    @cached_property
    def with_raw_response(self) -> RecursionWithRawResponse:
        return RecursionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecursionWithStreamingResponse:
        return RecursionWithStreamingResponse(self)


class AsyncRecursion(AsyncAPIResource):
    @cached_property
    def shared_responses(self) -> AsyncSharedResponses:
        return AsyncSharedResponses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRecursionWithRawResponse:
        return AsyncRecursionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecursionWithStreamingResponse:
        return AsyncRecursionWithStreamingResponse(self)


class RecursionWithRawResponse:
    def __init__(self, recursion: Recursion) -> None:
        self._recursion = recursion

    @cached_property
    def shared_responses(self) -> SharedResponsesWithRawResponse:
        return SharedResponsesWithRawResponse(self._recursion.shared_responses)


class AsyncRecursionWithRawResponse:
    def __init__(self, recursion: AsyncRecursion) -> None:
        self._recursion = recursion

    @cached_property
    def shared_responses(self) -> AsyncSharedResponsesWithRawResponse:
        return AsyncSharedResponsesWithRawResponse(self._recursion.shared_responses)


class RecursionWithStreamingResponse:
    def __init__(self, recursion: Recursion) -> None:
        self._recursion = recursion

    @cached_property
    def shared_responses(self) -> SharedResponsesWithStreamingResponse:
        return SharedResponsesWithStreamingResponse(self._recursion.shared_responses)


class AsyncRecursionWithStreamingResponse:
    def __init__(self, recursion: AsyncRecursion) -> None:
        self._recursion = recursion

    @cached_property
    def shared_responses(self) -> AsyncSharedResponsesWithStreamingResponse:
        return AsyncSharedResponsesWithStreamingResponse(self._recursion.shared_responses)
