# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import Address, EnvelopeWrappedArrayResponse, EnvelopeInlineResponseResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import DataWrapper, ItemsWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["Envelopes", "AsyncEnvelopes"]


class Envelopes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvelopesWithRawResponse:
        return EnvelopesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvelopesWithStreamingResponse:
        return EnvelopesWithStreamingResponse(self)

    def explicit(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """Endpoint with a response wrapped within a `data` property."""
        return self._get(
            "/envelopes/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper._unwrapper,
            ),
            cast_to=cast(Type[Address], DataWrapper[Address]),
        )

    def implicit(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """Endpoint with a response wrapped within a `items` property."""
        return self._get(
            "/envelopes/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper._unwrapper,
            ),
            cast_to=cast(Type[Address], ItemsWrapper[Address]),
        )

    def inline_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvelopeInlineResponseResponse:
        """
        Endpoint with a response wrapped within a `items` property that doesn't use a
        $ref.
        """
        return self._get(
            "/envelopes/items/inline_response",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper._unwrapper,
            ),
            cast_to=cast(Type[EnvelopeInlineResponseResponse], ItemsWrapper[EnvelopeInlineResponseResponse]),
        )

    def wrapped_array(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvelopeWrappedArrayResponse:
        """
        Endpoint with a response wrapped within a `items` property that is an array
        type.
        """
        return self._get(
            "/envelopes/items/wrapped_array",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper._unwrapper,
            ),
            cast_to=cast(Type[EnvelopeWrappedArrayResponse], ItemsWrapper[EnvelopeWrappedArrayResponse]),
        )


class AsyncEnvelopes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvelopesWithRawResponse:
        return AsyncEnvelopesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvelopesWithStreamingResponse:
        return AsyncEnvelopesWithStreamingResponse(self)

    async def explicit(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """Endpoint with a response wrapped within a `data` property."""
        return await self._get(
            "/envelopes/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper._unwrapper,
            ),
            cast_to=cast(Type[Address], DataWrapper[Address]),
        )

    async def implicit(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """Endpoint with a response wrapped within a `items` property."""
        return await self._get(
            "/envelopes/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper._unwrapper,
            ),
            cast_to=cast(Type[Address], ItemsWrapper[Address]),
        )

    async def inline_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvelopeInlineResponseResponse:
        """
        Endpoint with a response wrapped within a `items` property that doesn't use a
        $ref.
        """
        return await self._get(
            "/envelopes/items/inline_response",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper._unwrapper,
            ),
            cast_to=cast(Type[EnvelopeInlineResponseResponse], ItemsWrapper[EnvelopeInlineResponseResponse]),
        )

    async def wrapped_array(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvelopeWrappedArrayResponse:
        """
        Endpoint with a response wrapped within a `items` property that is an array
        type.
        """
        return await self._get(
            "/envelopes/items/wrapped_array",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ItemsWrapper._unwrapper,
            ),
            cast_to=cast(Type[EnvelopeWrappedArrayResponse], ItemsWrapper[EnvelopeWrappedArrayResponse]),
        )


class EnvelopesWithRawResponse:
    def __init__(self, envelopes: Envelopes) -> None:
        self._envelopes = envelopes

        self.explicit = to_raw_response_wrapper(
            envelopes.explicit,
        )
        self.implicit = to_raw_response_wrapper(
            envelopes.implicit,
        )
        self.inline_response = to_raw_response_wrapper(
            envelopes.inline_response,
        )
        self.wrapped_array = to_raw_response_wrapper(
            envelopes.wrapped_array,
        )


class AsyncEnvelopesWithRawResponse:
    def __init__(self, envelopes: AsyncEnvelopes) -> None:
        self._envelopes = envelopes

        self.explicit = async_to_raw_response_wrapper(
            envelopes.explicit,
        )
        self.implicit = async_to_raw_response_wrapper(
            envelopes.implicit,
        )
        self.inline_response = async_to_raw_response_wrapper(
            envelopes.inline_response,
        )
        self.wrapped_array = async_to_raw_response_wrapper(
            envelopes.wrapped_array,
        )


class EnvelopesWithStreamingResponse:
    def __init__(self, envelopes: Envelopes) -> None:
        self._envelopes = envelopes

        self.explicit = to_streamed_response_wrapper(
            envelopes.explicit,
        )
        self.implicit = to_streamed_response_wrapper(
            envelopes.implicit,
        )
        self.inline_response = to_streamed_response_wrapper(
            envelopes.inline_response,
        )
        self.wrapped_array = to_streamed_response_wrapper(
            envelopes.wrapped_array,
        )


class AsyncEnvelopesWithStreamingResponse:
    def __init__(self, envelopes: AsyncEnvelopes) -> None:
        self._envelopes = envelopes

        self.explicit = async_to_streamed_response_wrapper(
            envelopes.explicit,
        )
        self.implicit = async_to_streamed_response_wrapper(
            envelopes.implicit,
        )
        self.inline_response = async_to_streamed_response_wrapper(
            envelopes.inline_response,
        )
        self.wrapped_array = async_to_streamed_response_wrapper(
            envelopes.wrapped_array,
        )
