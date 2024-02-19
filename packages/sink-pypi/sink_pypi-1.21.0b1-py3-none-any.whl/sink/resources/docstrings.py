# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import DocstringLeadingDoubleQuoteResponse, DocstringTrailingDoubleQuoteResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.shared import BasicSharedModelObject

__all__ = ["Docstrings", "AsyncDocstrings"]


class Docstrings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocstringsWithRawResponse:
        return DocstringsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocstringsWithStreamingResponse:
        return DocstringsWithStreamingResponse(self)

    def description_contains_js_doc(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """
        This is the method description.

        Hello _/ console.log('evil code') /_ Goodbye \"\"\" \"\"\"" \"\"\""" \"\"\"\"\"\"
        console.log('more evil code'); \"\"\" \
        these need stay (valid escapes)

        \'\"\\  \\ \n\r\t\b\f\v\x63\uFE63\U0000FE63\N{HYPHEN}\1\12\123\1234a

        these need be escaped in python (invalid escapes)

        \a\\gg\\**\\((\\&&\\@@\\x2z\\u11z1\\U1111z111\\N{HYPHEN#}

        Other text
        """
        return self._get(
            "/docstrings/description_contains_comments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )

    def description_contains_js_doc_end(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """
        This is the method description.

        In the middle it contains a \\**\\**/ Or ```

        Other text
        """
        return self._get(
            "/docstrings/description_contains_comment_enders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )

    def leading_double_quote(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocstringLeadingDoubleQuoteResponse:
        return self._get(
            "/docstrings/property_leading_double_quote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocstringLeadingDoubleQuoteResponse,
        )

    def trailing_double_quote(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocstringTrailingDoubleQuoteResponse:
        return self._get(
            "/docstrings/property_trailing_double_quote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocstringTrailingDoubleQuoteResponse,
        )


class AsyncDocstrings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocstringsWithRawResponse:
        return AsyncDocstringsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocstringsWithStreamingResponse:
        return AsyncDocstringsWithStreamingResponse(self)

    async def description_contains_js_doc(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """
        This is the method description.

        Hello _/ console.log('evil code') /_ Goodbye \"\"\" \"\"\"" \"\"\""" \"\"\"\"\"\"
        console.log('more evil code'); \"\"\" \
        these need stay (valid escapes)

        \'\"\\  \\ \n\r\t\b\f\v\x63\uFE63\U0000FE63\N{HYPHEN}\1\12\123\1234a

        these need be escaped in python (invalid escapes)

        \a\\gg\\**\\((\\&&\\@@\\x2z\\u11z1\\U1111z111\\N{HYPHEN#}

        Other text
        """
        return await self._get(
            "/docstrings/description_contains_comments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )

    async def description_contains_js_doc_end(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """
        This is the method description.

        In the middle it contains a \\**\\**/ Or ```

        Other text
        """
        return await self._get(
            "/docstrings/description_contains_comment_enders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )

    async def leading_double_quote(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocstringLeadingDoubleQuoteResponse:
        return await self._get(
            "/docstrings/property_leading_double_quote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocstringLeadingDoubleQuoteResponse,
        )

    async def trailing_double_quote(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocstringTrailingDoubleQuoteResponse:
        return await self._get(
            "/docstrings/property_trailing_double_quote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocstringTrailingDoubleQuoteResponse,
        )


class DocstringsWithRawResponse:
    def __init__(self, docstrings: Docstrings) -> None:
        self._docstrings = docstrings

        self.description_contains_js_doc = to_raw_response_wrapper(
            docstrings.description_contains_js_doc,
        )
        self.description_contains_js_doc_end = to_raw_response_wrapper(
            docstrings.description_contains_js_doc_end,
        )
        self.leading_double_quote = to_raw_response_wrapper(
            docstrings.leading_double_quote,
        )
        self.trailing_double_quote = to_raw_response_wrapper(
            docstrings.trailing_double_quote,
        )


class AsyncDocstringsWithRawResponse:
    def __init__(self, docstrings: AsyncDocstrings) -> None:
        self._docstrings = docstrings

        self.description_contains_js_doc = async_to_raw_response_wrapper(
            docstrings.description_contains_js_doc,
        )
        self.description_contains_js_doc_end = async_to_raw_response_wrapper(
            docstrings.description_contains_js_doc_end,
        )
        self.leading_double_quote = async_to_raw_response_wrapper(
            docstrings.leading_double_quote,
        )
        self.trailing_double_quote = async_to_raw_response_wrapper(
            docstrings.trailing_double_quote,
        )


class DocstringsWithStreamingResponse:
    def __init__(self, docstrings: Docstrings) -> None:
        self._docstrings = docstrings

        self.description_contains_js_doc = to_streamed_response_wrapper(
            docstrings.description_contains_js_doc,
        )
        self.description_contains_js_doc_end = to_streamed_response_wrapper(
            docstrings.description_contains_js_doc_end,
        )
        self.leading_double_quote = to_streamed_response_wrapper(
            docstrings.leading_double_quote,
        )
        self.trailing_double_quote = to_streamed_response_wrapper(
            docstrings.trailing_double_quote,
        )


class AsyncDocstringsWithStreamingResponse:
    def __init__(self, docstrings: AsyncDocstrings) -> None:
        self._docstrings = docstrings

        self.description_contains_js_doc = async_to_streamed_response_wrapper(
            docstrings.description_contains_js_doc,
        )
        self.description_contains_js_doc_end = async_to_streamed_response_wrapper(
            docstrings.description_contains_js_doc_end,
        )
        self.leading_double_quote = async_to_streamed_response_wrapper(
            docstrings.leading_double_quote,
        )
        self.trailing_double_quote = async_to_streamed_response_wrapper(
            docstrings.trailing_double_quote,
        )
