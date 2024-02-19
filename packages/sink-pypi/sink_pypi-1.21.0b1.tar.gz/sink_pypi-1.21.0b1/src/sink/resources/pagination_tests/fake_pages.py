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
from ...pagination import SyncFakePage, AsyncFakePage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.shared import SimpleObject
from ...types.pagination_tests import fake_page_list_params

__all__ = ["FakePages", "AsyncFakePages"]


class FakePages(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FakePagesWithRawResponse:
        return FakePagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FakePagesWithStreamingResponse:
        return FakePagesWithStreamingResponse(self)

    def list(
        self,
        *,
        my_fake_page_param: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncFakePage[SimpleObject]:
        """
        Endpoint that returns a top-level array that is transformed into a fake_page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/fake_page",
            page=SyncFakePage[SimpleObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"my_fake_page_param": my_fake_page_param}, fake_page_list_params.FakePageListParams
                ),
            ),
            model=SimpleObject,
        )


class AsyncFakePages(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFakePagesWithRawResponse:
        return AsyncFakePagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFakePagesWithStreamingResponse:
        return AsyncFakePagesWithStreamingResponse(self)

    def list(
        self,
        *,
        my_fake_page_param: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SimpleObject, AsyncFakePage[SimpleObject]]:
        """
        Endpoint that returns a top-level array that is transformed into a fake_page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/fake_page",
            page=AsyncFakePage[SimpleObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"my_fake_page_param": my_fake_page_param}, fake_page_list_params.FakePageListParams
                ),
            ),
            model=SimpleObject,
        )


class FakePagesWithRawResponse:
    def __init__(self, fake_pages: FakePages) -> None:
        self._fake_pages = fake_pages

        self.list = to_raw_response_wrapper(
            fake_pages.list,
        )


class AsyncFakePagesWithRawResponse:
    def __init__(self, fake_pages: AsyncFakePages) -> None:
        self._fake_pages = fake_pages

        self.list = async_to_raw_response_wrapper(
            fake_pages.list,
        )


class FakePagesWithStreamingResponse:
    def __init__(self, fake_pages: FakePages) -> None:
        self._fake_pages = fake_pages

        self.list = to_streamed_response_wrapper(
            fake_pages.list,
        )


class AsyncFakePagesWithStreamingResponse:
    def __init__(self, fake_pages: AsyncFakePages) -> None:
        self._fake_pages = fake_pages

        self.list = async_to_streamed_response_wrapper(
            fake_pages.list,
        )
