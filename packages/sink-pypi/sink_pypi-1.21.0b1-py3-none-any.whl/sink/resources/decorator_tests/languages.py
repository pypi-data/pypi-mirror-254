# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.shared import SimpleObject

__all__ = ["Languages", "AsyncLanguages"]


class Languages(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LanguagesWithRawResponse:
        return LanguagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguagesWithStreamingResponse:
        return LanguagesWithStreamingResponse(self)

    def skipped_for_node(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleObject:
        """Endpoint that returns a $ref to SimpleObject.

        This is used to test shared
        response models.
        """
        return self._get(
            "/responses/shared_simple_object",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleObject,
        )


class AsyncLanguages(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLanguagesWithRawResponse:
        return AsyncLanguagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguagesWithStreamingResponse:
        return AsyncLanguagesWithStreamingResponse(self)

    async def skipped_for_node(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleObject:
        """Endpoint that returns a $ref to SimpleObject.

        This is used to test shared
        response models.
        """
        return await self._get(
            "/responses/shared_simple_object",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleObject,
        )


class LanguagesWithRawResponse:
    def __init__(self, languages: Languages) -> None:
        self._languages = languages

        self.skipped_for_node = to_raw_response_wrapper(
            languages.skipped_for_node,
        )


class AsyncLanguagesWithRawResponse:
    def __init__(self, languages: AsyncLanguages) -> None:
        self._languages = languages

        self.skipped_for_node = async_to_raw_response_wrapper(
            languages.skipped_for_node,
        )


class LanguagesWithStreamingResponse:
    def __init__(self, languages: Languages) -> None:
        self._languages = languages

        self.skipped_for_node = to_streamed_response_wrapper(
            languages.skipped_for_node,
        )


class AsyncLanguagesWithStreamingResponse:
    def __init__(self, languages: AsyncLanguages) -> None:
        self._languages = languages

        self.skipped_for_node = async_to_streamed_response_wrapper(
            languages.skipped_for_node,
        )
