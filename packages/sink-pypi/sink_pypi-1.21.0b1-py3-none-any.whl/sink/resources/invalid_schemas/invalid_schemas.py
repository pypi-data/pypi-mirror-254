# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .arrays import (
    Arrays,
    AsyncArrays,
    ArraysWithRawResponse,
    AsyncArraysWithRawResponse,
    ArraysWithStreamingResponse,
    AsyncArraysWithStreamingResponse,
)
from .objects import (
    Objects,
    AsyncObjects,
    ObjectsWithRawResponse,
    AsyncObjectsWithRawResponse,
    ObjectsWithStreamingResponse,
    AsyncObjectsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InvalidSchemas", "AsyncInvalidSchemas"]


class InvalidSchemas(SyncAPIResource):
    @cached_property
    def arrays(self) -> Arrays:
        return Arrays(self._client)

    @cached_property
    def objects(self) -> Objects:
        return Objects(self._client)

    @cached_property
    def with_raw_response(self) -> InvalidSchemasWithRawResponse:
        return InvalidSchemasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvalidSchemasWithStreamingResponse:
        return InvalidSchemasWithStreamingResponse(self)


class AsyncInvalidSchemas(AsyncAPIResource):
    @cached_property
    def arrays(self) -> AsyncArrays:
        return AsyncArrays(self._client)

    @cached_property
    def objects(self) -> AsyncObjects:
        return AsyncObjects(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInvalidSchemasWithRawResponse:
        return AsyncInvalidSchemasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvalidSchemasWithStreamingResponse:
        return AsyncInvalidSchemasWithStreamingResponse(self)


class InvalidSchemasWithRawResponse:
    def __init__(self, invalid_schemas: InvalidSchemas) -> None:
        self._invalid_schemas = invalid_schemas

    @cached_property
    def arrays(self) -> ArraysWithRawResponse:
        return ArraysWithRawResponse(self._invalid_schemas.arrays)

    @cached_property
    def objects(self) -> ObjectsWithRawResponse:
        return ObjectsWithRawResponse(self._invalid_schemas.objects)


class AsyncInvalidSchemasWithRawResponse:
    def __init__(self, invalid_schemas: AsyncInvalidSchemas) -> None:
        self._invalid_schemas = invalid_schemas

    @cached_property
    def arrays(self) -> AsyncArraysWithRawResponse:
        return AsyncArraysWithRawResponse(self._invalid_schemas.arrays)

    @cached_property
    def objects(self) -> AsyncObjectsWithRawResponse:
        return AsyncObjectsWithRawResponse(self._invalid_schemas.objects)


class InvalidSchemasWithStreamingResponse:
    def __init__(self, invalid_schemas: InvalidSchemas) -> None:
        self._invalid_schemas = invalid_schemas

    @cached_property
    def arrays(self) -> ArraysWithStreamingResponse:
        return ArraysWithStreamingResponse(self._invalid_schemas.arrays)

    @cached_property
    def objects(self) -> ObjectsWithStreamingResponse:
        return ObjectsWithStreamingResponse(self._invalid_schemas.objects)


class AsyncInvalidSchemasWithStreamingResponse:
    def __init__(self, invalid_schemas: AsyncInvalidSchemas) -> None:
        self._invalid_schemas = invalid_schemas

    @cached_property
    def arrays(self) -> AsyncArraysWithStreamingResponse:
        return AsyncArraysWithStreamingResponse(self._invalid_schemas.arrays)

    @cached_property
    def objects(self) -> AsyncObjectsWithStreamingResponse:
        return AsyncObjectsWithStreamingResponse(self._invalid_schemas.objects)
