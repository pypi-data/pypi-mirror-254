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
from ...types.types import (
    ObjectMixedKnownAndUnknownResponse,
    ObjectMultiplePropertiesSameRefResponse,
    ObjectMultiplePropertiesSameModelResponse,
    ObjectMultipleArrayPropertiesSameRefResponse,
    ObjectTwoDimensionalArrayPrimitivePropertyResponse,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Objects", "AsyncObjects"]


class Objects(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectsWithRawResponse:
        return ObjectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsWithStreamingResponse:
        return ObjectsWithStreamingResponse(self)

    def mixed_known_and_unknown(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMixedKnownAndUnknownResponse:
        """
        Endpoint with a response schema object that contains a mix of known & unknown
        properties with the same value types.
        """
        return self._get(
            "/types/object/mixed_known_and_unknown",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMixedKnownAndUnknownResponse,
        )

    def multiple_array_properties_same_ref(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMultipleArrayPropertiesSameRefResponse:
        """
        Endpoint with a response schema object that contains multiple properties that
        reference the same $ref in array items that is _not_ a model in the config.
        Three child types should be generated, one for each property.
        """
        return self._get(
            "/types/object/multiple_array_properties_same_ref",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMultipleArrayPropertiesSameRefResponse,
        )

    def multiple_properties_same_model(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMultiplePropertiesSameModelResponse:
        """
        Endpoint with a response schema object that contains multiple properties that
        reference the same model.
        """
        return self._get(
            "/types/object/multiple_properties_same_model",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMultiplePropertiesSameModelResponse,
        )

    def multiple_properties_same_ref(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMultiplePropertiesSameRefResponse:
        """
        Endpoint with a response schema object that contains multiple properties that
        reference the same $ref that is _not_ a model in the config. Three child types
        should be generated. One for each property.
        """
        return self._get(
            "/types/object/multiple_properties_same_ref",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMultiplePropertiesSameRefResponse,
        )

    def two_dimensional_array_primitive_property(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectTwoDimensionalArrayPrimitivePropertyResponse:
        """
        Endpoint with a response schema object that contains properties that are
        primitive 2d arrays
        """
        return self._get(
            "/types/object/2d_array_primitive_properties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTwoDimensionalArrayPrimitivePropertyResponse,
        )


class AsyncObjects(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectsWithRawResponse:
        return AsyncObjectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsWithStreamingResponse:
        return AsyncObjectsWithStreamingResponse(self)

    async def mixed_known_and_unknown(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMixedKnownAndUnknownResponse:
        """
        Endpoint with a response schema object that contains a mix of known & unknown
        properties with the same value types.
        """
        return await self._get(
            "/types/object/mixed_known_and_unknown",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMixedKnownAndUnknownResponse,
        )

    async def multiple_array_properties_same_ref(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMultipleArrayPropertiesSameRefResponse:
        """
        Endpoint with a response schema object that contains multiple properties that
        reference the same $ref in array items that is _not_ a model in the config.
        Three child types should be generated, one for each property.
        """
        return await self._get(
            "/types/object/multiple_array_properties_same_ref",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMultipleArrayPropertiesSameRefResponse,
        )

    async def multiple_properties_same_model(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMultiplePropertiesSameModelResponse:
        """
        Endpoint with a response schema object that contains multiple properties that
        reference the same model.
        """
        return await self._get(
            "/types/object/multiple_properties_same_model",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMultiplePropertiesSameModelResponse,
        )

    async def multiple_properties_same_ref(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectMultiplePropertiesSameRefResponse:
        """
        Endpoint with a response schema object that contains multiple properties that
        reference the same $ref that is _not_ a model in the config. Three child types
        should be generated. One for each property.
        """
        return await self._get(
            "/types/object/multiple_properties_same_ref",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectMultiplePropertiesSameRefResponse,
        )

    async def two_dimensional_array_primitive_property(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectTwoDimensionalArrayPrimitivePropertyResponse:
        """
        Endpoint with a response schema object that contains properties that are
        primitive 2d arrays
        """
        return await self._get(
            "/types/object/2d_array_primitive_properties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTwoDimensionalArrayPrimitivePropertyResponse,
        )


class ObjectsWithRawResponse:
    def __init__(self, objects: Objects) -> None:
        self._objects = objects

        self.mixed_known_and_unknown = to_raw_response_wrapper(
            objects.mixed_known_and_unknown,
        )
        self.multiple_array_properties_same_ref = to_raw_response_wrapper(
            objects.multiple_array_properties_same_ref,
        )
        self.multiple_properties_same_model = to_raw_response_wrapper(
            objects.multiple_properties_same_model,
        )
        self.multiple_properties_same_ref = to_raw_response_wrapper(
            objects.multiple_properties_same_ref,
        )
        self.two_dimensional_array_primitive_property = to_raw_response_wrapper(
            objects.two_dimensional_array_primitive_property,
        )


class AsyncObjectsWithRawResponse:
    def __init__(self, objects: AsyncObjects) -> None:
        self._objects = objects

        self.mixed_known_and_unknown = async_to_raw_response_wrapper(
            objects.mixed_known_and_unknown,
        )
        self.multiple_array_properties_same_ref = async_to_raw_response_wrapper(
            objects.multiple_array_properties_same_ref,
        )
        self.multiple_properties_same_model = async_to_raw_response_wrapper(
            objects.multiple_properties_same_model,
        )
        self.multiple_properties_same_ref = async_to_raw_response_wrapper(
            objects.multiple_properties_same_ref,
        )
        self.two_dimensional_array_primitive_property = async_to_raw_response_wrapper(
            objects.two_dimensional_array_primitive_property,
        )


class ObjectsWithStreamingResponse:
    def __init__(self, objects: Objects) -> None:
        self._objects = objects

        self.mixed_known_and_unknown = to_streamed_response_wrapper(
            objects.mixed_known_and_unknown,
        )
        self.multiple_array_properties_same_ref = to_streamed_response_wrapper(
            objects.multiple_array_properties_same_ref,
        )
        self.multiple_properties_same_model = to_streamed_response_wrapper(
            objects.multiple_properties_same_model,
        )
        self.multiple_properties_same_ref = to_streamed_response_wrapper(
            objects.multiple_properties_same_ref,
        )
        self.two_dimensional_array_primitive_property = to_streamed_response_wrapper(
            objects.two_dimensional_array_primitive_property,
        )


class AsyncObjectsWithStreamingResponse:
    def __init__(self, objects: AsyncObjects) -> None:
        self._objects = objects

        self.mixed_known_and_unknown = async_to_streamed_response_wrapper(
            objects.mixed_known_and_unknown,
        )
        self.multiple_array_properties_same_ref = async_to_streamed_response_wrapper(
            objects.multiple_array_properties_same_ref,
        )
        self.multiple_properties_same_model = async_to_streamed_response_wrapper(
            objects.multiple_properties_same_model,
        )
        self.multiple_properties_same_ref = async_to_streamed_response_wrapper(
            objects.multiple_properties_same_ref,
        )
        self.two_dimensional_array_primitive_property = async_to_streamed_response_wrapper(
            objects.two_dimensional_array_primitive_property,
        )
