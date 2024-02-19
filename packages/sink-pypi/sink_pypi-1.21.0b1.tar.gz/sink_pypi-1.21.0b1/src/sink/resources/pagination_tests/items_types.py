# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

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
from ...pagination import SyncPagePageNumber, AsyncPagePageNumber
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.pagination_tests import items_type_list_unknown_params

__all__ = ["ItemsTypes", "AsyncItemsTypes"]


class ItemsTypes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsTypesWithRawResponse:
        return ItemsTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsTypesWithStreamingResponse:
        return ItemsTypesWithStreamingResponse(self)

    def list_unknown(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPagePageNumber[object]:
        """
        Test case for paginated items of `unknown` types with page_number pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/items_types/unknown",
            page=SyncPagePageNumber[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    items_type_list_unknown_params.ItemsTypeListUnknownParams,
                ),
            ),
            model=object,
        )


class AsyncItemsTypes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsTypesWithRawResponse:
        return AsyncItemsTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsTypesWithStreamingResponse:
        return AsyncItemsTypesWithStreamingResponse(self)

    def list_unknown(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncPagePageNumber[object]]:
        """
        Test case for paginated items of `unknown` types with page_number pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/items_types/unknown",
            page=AsyncPagePageNumber[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    items_type_list_unknown_params.ItemsTypeListUnknownParams,
                ),
            ),
            model=object,
        )


class ItemsTypesWithRawResponse:
    def __init__(self, items_types: ItemsTypes) -> None:
        self._items_types = items_types

        self.list_unknown = to_raw_response_wrapper(
            items_types.list_unknown,
        )


class AsyncItemsTypesWithRawResponse:
    def __init__(self, items_types: AsyncItemsTypes) -> None:
        self._items_types = items_types

        self.list_unknown = async_to_raw_response_wrapper(
            items_types.list_unknown,
        )


class ItemsTypesWithStreamingResponse:
    def __init__(self, items_types: ItemsTypes) -> None:
        self._items_types = items_types

        self.list_unknown = to_streamed_response_wrapper(
            items_types.list_unknown,
        )


class AsyncItemsTypesWithStreamingResponse:
    def __init__(self, items_types: AsyncItemsTypes) -> None:
        self._items_types = items_types

        self.list_unknown = async_to_streamed_response_wrapper(
            items_types.list_unknown,
        )
