# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from .level_one import (
    LevelOne,
    AsyncLevelOne,
    LevelOneWithRawResponse,
    AsyncLevelOneWithRawResponse,
    LevelOneWithStreamingResponse,
    AsyncLevelOneWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .level_one.level_one import LevelOne, AsyncLevelOne

__all__ = ["DeeplyNested", "AsyncDeeplyNested"]


class DeeplyNested(SyncAPIResource):
    @cached_property
    def level_one(self) -> LevelOne:
        return LevelOne(self._client)

    @cached_property
    def with_raw_response(self) -> DeeplyNestedWithRawResponse:
        return DeeplyNestedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeeplyNestedWithStreamingResponse:
        return DeeplyNestedWithStreamingResponse(self)


class AsyncDeeplyNested(AsyncAPIResource):
    @cached_property
    def level_one(self) -> AsyncLevelOne:
        return AsyncLevelOne(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeeplyNestedWithRawResponse:
        return AsyncDeeplyNestedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeeplyNestedWithStreamingResponse:
        return AsyncDeeplyNestedWithStreamingResponse(self)


class DeeplyNestedWithRawResponse:
    def __init__(self, deeply_nested: DeeplyNested) -> None:
        self._deeply_nested = deeply_nested

    @cached_property
    def level_one(self) -> LevelOneWithRawResponse:
        return LevelOneWithRawResponse(self._deeply_nested.level_one)


class AsyncDeeplyNestedWithRawResponse:
    def __init__(self, deeply_nested: AsyncDeeplyNested) -> None:
        self._deeply_nested = deeply_nested

    @cached_property
    def level_one(self) -> AsyncLevelOneWithRawResponse:
        return AsyncLevelOneWithRawResponse(self._deeply_nested.level_one)


class DeeplyNestedWithStreamingResponse:
    def __init__(self, deeply_nested: DeeplyNested) -> None:
        self._deeply_nested = deeply_nested

    @cached_property
    def level_one(self) -> LevelOneWithStreamingResponse:
        return LevelOneWithStreamingResponse(self._deeply_nested.level_one)


class AsyncDeeplyNestedWithStreamingResponse:
    def __init__(self, deeply_nested: AsyncDeeplyNested) -> None:
        self._deeply_nested = deeply_nested

    @cached_property
    def level_one(self) -> AsyncLevelOneWithStreamingResponse:
        return AsyncLevelOneWithStreamingResponse(self._deeply_nested.level_one)
