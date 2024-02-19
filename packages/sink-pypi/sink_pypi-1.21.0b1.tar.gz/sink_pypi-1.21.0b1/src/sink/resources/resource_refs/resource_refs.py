# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .parent import (
    Parent,
    AsyncParent,
    ParentWithRawResponse,
    AsyncParentWithRawResponse,
    ParentWithStreamingResponse,
    AsyncParentWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .parent.parent import Parent, AsyncParent

__all__ = ["ResourceRefs", "AsyncResourceRefs"]


class ResourceRefs(SyncAPIResource):
    @cached_property
    def parent(self) -> Parent:
        return Parent(self._client)

    @cached_property
    def with_raw_response(self) -> ResourceRefsWithRawResponse:
        return ResourceRefsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceRefsWithStreamingResponse:
        return ResourceRefsWithStreamingResponse(self)


class AsyncResourceRefs(AsyncAPIResource):
    @cached_property
    def parent(self) -> AsyncParent:
        return AsyncParent(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourceRefsWithRawResponse:
        return AsyncResourceRefsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceRefsWithStreamingResponse:
        return AsyncResourceRefsWithStreamingResponse(self)


class ResourceRefsWithRawResponse:
    def __init__(self, resource_refs: ResourceRefs) -> None:
        self._resource_refs = resource_refs

    @cached_property
    def parent(self) -> ParentWithRawResponse:
        return ParentWithRawResponse(self._resource_refs.parent)


class AsyncResourceRefsWithRawResponse:
    def __init__(self, resource_refs: AsyncResourceRefs) -> None:
        self._resource_refs = resource_refs

    @cached_property
    def parent(self) -> AsyncParentWithRawResponse:
        return AsyncParentWithRawResponse(self._resource_refs.parent)


class ResourceRefsWithStreamingResponse:
    def __init__(self, resource_refs: ResourceRefs) -> None:
        self._resource_refs = resource_refs

    @cached_property
    def parent(self) -> ParentWithStreamingResponse:
        return ParentWithStreamingResponse(self._resource_refs.parent)


class AsyncResourceRefsWithStreamingResponse:
    def __init__(self, resource_refs: AsyncResourceRefs) -> None:
        self._resource_refs = resource_refs

    @cached_property
    def parent(self) -> AsyncParentWithStreamingResponse:
        return AsyncParentWithStreamingResponse(self._resource_refs.parent)
