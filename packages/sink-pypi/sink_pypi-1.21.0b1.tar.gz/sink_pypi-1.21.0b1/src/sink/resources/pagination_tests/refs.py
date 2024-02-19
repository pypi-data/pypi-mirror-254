# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import MyModel
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import (
    SyncPageCursorSharedRef,
    AsyncPageCursorSharedRef,
    SyncPageCursorNestedObjectRef,
    AsyncPageCursorNestedObjectRef,
)
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.pagination_tests import ref_nested_object_ref_params, ref_with_shared_model_ref_params

__all__ = ["Refs", "AsyncRefs"]


class Refs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefsWithRawResponse:
        return RefsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefsWithStreamingResponse:
        return RefsWithStreamingResponse(self)

    def nested_object_ref(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        object_param: ref_nested_object_ref_params.ObjectParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageCursorNestedObjectRef[MyModel]:
        """
        Test case for pagination using an in-line nested object reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/nested_object_ref",
            page=SyncPageCursorNestedObjectRef[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "object_param": object_param,
                    },
                    ref_nested_object_ref_params.RefNestedObjectRefParams,
                ),
            ),
            model=MyModel,
        )

    def with_shared_model_ref(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageCursorSharedRef[MyModel]:
        """
        Test case for pagination using a shared model reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/with_shared_model_ref",
            page=SyncPageCursorSharedRef[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    ref_with_shared_model_ref_params.RefWithSharedModelRefParams,
                ),
            ),
            model=MyModel,
        )


class AsyncRefs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefsWithRawResponse:
        return AsyncRefsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefsWithStreamingResponse:
        return AsyncRefsWithStreamingResponse(self)

    def nested_object_ref(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        object_param: ref_nested_object_ref_params.ObjectParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageCursorNestedObjectRef[MyModel]]:
        """
        Test case for pagination using an in-line nested object reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/nested_object_ref",
            page=AsyncPageCursorNestedObjectRef[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "object_param": object_param,
                    },
                    ref_nested_object_ref_params.RefNestedObjectRefParams,
                ),
            ),
            model=MyModel,
        )

    def with_shared_model_ref(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MyModel, AsyncPageCursorSharedRef[MyModel]]:
        """
        Test case for pagination using a shared model reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/with_shared_model_ref",
            page=AsyncPageCursorSharedRef[MyModel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    ref_with_shared_model_ref_params.RefWithSharedModelRefParams,
                ),
            ),
            model=MyModel,
        )


class RefsWithRawResponse:
    def __init__(self, refs: Refs) -> None:
        self._refs = refs

        self.nested_object_ref = to_raw_response_wrapper(
            refs.nested_object_ref,
        )
        self.with_shared_model_ref = to_raw_response_wrapper(
            refs.with_shared_model_ref,
        )


class AsyncRefsWithRawResponse:
    def __init__(self, refs: AsyncRefs) -> None:
        self._refs = refs

        self.nested_object_ref = async_to_raw_response_wrapper(
            refs.nested_object_ref,
        )
        self.with_shared_model_ref = async_to_raw_response_wrapper(
            refs.with_shared_model_ref,
        )


class RefsWithStreamingResponse:
    def __init__(self, refs: Refs) -> None:
        self._refs = refs

        self.nested_object_ref = to_streamed_response_wrapper(
            refs.nested_object_ref,
        )
        self.with_shared_model_ref = to_streamed_response_wrapper(
            refs.with_shared_model_ref,
        )


class AsyncRefsWithStreamingResponse:
    def __init__(self, refs: AsyncRefs) -> None:
        self._refs = refs

        self.nested_object_ref = async_to_streamed_response_wrapper(
            refs.nested_object_ref,
        )
        self.with_shared_model_ref = async_to_streamed_response_wrapper(
            refs.with_shared_model_ref,
        )
