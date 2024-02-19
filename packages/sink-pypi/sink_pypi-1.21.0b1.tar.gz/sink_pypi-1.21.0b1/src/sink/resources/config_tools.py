# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import (
    ConfigToolModelRefFromSchemasResponse,
    ConfigToolModelRefFromNestedResponseBodyResponse,
)
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

__all__ = ["ConfigTools", "AsyncConfigTools"]


class ConfigTools(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigToolsWithRawResponse:
        return ConfigToolsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigToolsWithStreamingResponse:
        return ConfigToolsWithStreamingResponse(self)

    def model_ref_from_nested_response_body(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigToolModelRefFromNestedResponseBodyResponse:
        return self._get(
            "/config_tools/model_refs/from_nested_response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigToolModelRefFromNestedResponseBodyResponse,
        )

    def model_ref_from_schemas(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigToolModelRefFromSchemasResponse:
        return self._get(
            "/config_tools/model_refs/from_schemas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigToolModelRefFromSchemasResponse,
        )


class AsyncConfigTools(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigToolsWithRawResponse:
        return AsyncConfigToolsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigToolsWithStreamingResponse:
        return AsyncConfigToolsWithStreamingResponse(self)

    async def model_ref_from_nested_response_body(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigToolModelRefFromNestedResponseBodyResponse:
        return await self._get(
            "/config_tools/model_refs/from_nested_response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigToolModelRefFromNestedResponseBodyResponse,
        )

    async def model_ref_from_schemas(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigToolModelRefFromSchemasResponse:
        return await self._get(
            "/config_tools/model_refs/from_schemas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigToolModelRefFromSchemasResponse,
        )


class ConfigToolsWithRawResponse:
    def __init__(self, config_tools: ConfigTools) -> None:
        self._config_tools = config_tools

        self.model_ref_from_nested_response_body = to_raw_response_wrapper(
            config_tools.model_ref_from_nested_response_body,
        )
        self.model_ref_from_schemas = to_raw_response_wrapper(
            config_tools.model_ref_from_schemas,
        )


class AsyncConfigToolsWithRawResponse:
    def __init__(self, config_tools: AsyncConfigTools) -> None:
        self._config_tools = config_tools

        self.model_ref_from_nested_response_body = async_to_raw_response_wrapper(
            config_tools.model_ref_from_nested_response_body,
        )
        self.model_ref_from_schemas = async_to_raw_response_wrapper(
            config_tools.model_ref_from_schemas,
        )


class ConfigToolsWithStreamingResponse:
    def __init__(self, config_tools: ConfigTools) -> None:
        self._config_tools = config_tools

        self.model_ref_from_nested_response_body = to_streamed_response_wrapper(
            config_tools.model_ref_from_nested_response_body,
        )
        self.model_ref_from_schemas = to_streamed_response_wrapper(
            config_tools.model_ref_from_schemas,
        )


class AsyncConfigToolsWithStreamingResponse:
    def __init__(self, config_tools: AsyncConfigTools) -> None:
        self._config_tools = config_tools

        self.model_ref_from_nested_response_body = async_to_streamed_response_wrapper(
            config_tools.model_ref_from_nested_response_body,
        )
        self.model_ref_from_schemas = async_to_streamed_response_wrapper(
            config_tools.model_ref_from_schemas,
        )
