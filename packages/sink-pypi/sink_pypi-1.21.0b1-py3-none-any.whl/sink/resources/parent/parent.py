# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .child import (
    Child,
    AsyncChild,
    ChildWithRawResponse,
    AsyncChildWithRawResponse,
    ChildWithStreamingResponse,
    AsyncChildWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Parent", "AsyncParent"]


class Parent(SyncAPIResource):
    @cached_property
    def child(self) -> Child:
        return Child(self._client)

    @cached_property
    def with_raw_response(self) -> ParentWithRawResponse:
        return ParentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParentWithStreamingResponse:
        return ParentWithStreamingResponse(self)


class AsyncParent(AsyncAPIResource):
    @cached_property
    def child(self) -> AsyncChild:
        return AsyncChild(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncParentWithRawResponse:
        return AsyncParentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParentWithStreamingResponse:
        return AsyncParentWithStreamingResponse(self)


class ParentWithRawResponse:
    def __init__(self, parent: Parent) -> None:
        self._parent = parent

    @cached_property
    def child(self) -> ChildWithRawResponse:
        return ChildWithRawResponse(self._parent.child)


class AsyncParentWithRawResponse:
    def __init__(self, parent: AsyncParent) -> None:
        self._parent = parent

    @cached_property
    def child(self) -> AsyncChildWithRawResponse:
        return AsyncChildWithRawResponse(self._parent.child)


class ParentWithStreamingResponse:
    def __init__(self, parent: Parent) -> None:
        self._parent = parent

    @cached_property
    def child(self) -> ChildWithStreamingResponse:
        return ChildWithStreamingResponse(self._parent.child)


class AsyncParentWithStreamingResponse:
    def __init__(self, parent: AsyncParent) -> None:
        self._parent = parent

    @cached_property
    def child(self) -> AsyncChildWithStreamingResponse:
        return AsyncChildWithStreamingResponse(self._parent.child)
