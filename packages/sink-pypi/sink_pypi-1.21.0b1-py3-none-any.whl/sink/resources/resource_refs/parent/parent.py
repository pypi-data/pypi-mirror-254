# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .child import (
    Child,
    AsyncChild,
    ChildWithRawResponse,
    AsyncChildWithRawResponse,
    ChildWithStreamingResponse,
    AsyncChildWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.resource_refs import ParentModelWithChildRef

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

    def returns_parent_model_with_child_ref(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParentModelWithChildRef:
        """endpoint that returns a model that has a nested reference to a child model"""
        return self._get(
            "/resource_refs/parent_with_child_ref",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParentModelWithChildRef,
        )


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

    async def returns_parent_model_with_child_ref(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParentModelWithChildRef:
        """endpoint that returns a model that has a nested reference to a child model"""
        return await self._get(
            "/resource_refs/parent_with_child_ref",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParentModelWithChildRef,
        )


class ParentWithRawResponse:
    def __init__(self, parent: Parent) -> None:
        self._parent = parent

        self.returns_parent_model_with_child_ref = to_raw_response_wrapper(
            parent.returns_parent_model_with_child_ref,
        )

    @cached_property
    def child(self) -> ChildWithRawResponse:
        return ChildWithRawResponse(self._parent.child)


class AsyncParentWithRawResponse:
    def __init__(self, parent: AsyncParent) -> None:
        self._parent = parent

        self.returns_parent_model_with_child_ref = async_to_raw_response_wrapper(
            parent.returns_parent_model_with_child_ref,
        )

    @cached_property
    def child(self) -> AsyncChildWithRawResponse:
        return AsyncChildWithRawResponse(self._parent.child)


class ParentWithStreamingResponse:
    def __init__(self, parent: Parent) -> None:
        self._parent = parent

        self.returns_parent_model_with_child_ref = to_streamed_response_wrapper(
            parent.returns_parent_model_with_child_ref,
        )

    @cached_property
    def child(self) -> ChildWithStreamingResponse:
        return ChildWithStreamingResponse(self._parent.child)


class AsyncParentWithStreamingResponse:
    def __init__(self, parent: AsyncParent) -> None:
        self._parent = parent

        self.returns_parent_model_with_child_ref = async_to_streamed_response_wrapper(
            parent.returns_parent_model_with_child_ref,
        )

    @cached_property
    def child(self) -> AsyncChildWithStreamingResponse:
        return AsyncChildWithStreamingResponse(self._parent.child)
