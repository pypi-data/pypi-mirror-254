# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .eeoc import (
    EEOCResource,
    AsyncEEOCResource,
    EEOCResourceWithRawResponse,
    AsyncEEOCResourceWithRawResponse,
    EEOCResourceWithStreamingResponse,
    AsyncEEOCResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Casing", "AsyncCasing"]


class Casing(SyncAPIResource):
    @cached_property
    def eeoc(self) -> EEOCResource:
        return EEOCResource(self._client)

    @cached_property
    def with_raw_response(self) -> CasingWithRawResponse:
        return CasingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasingWithStreamingResponse:
        return CasingWithStreamingResponse(self)


class AsyncCasing(AsyncAPIResource):
    @cached_property
    def eeoc(self) -> AsyncEEOCResource:
        return AsyncEEOCResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCasingWithRawResponse:
        return AsyncCasingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasingWithStreamingResponse:
        return AsyncCasingWithStreamingResponse(self)


class CasingWithRawResponse:
    def __init__(self, casing: Casing) -> None:
        self._casing = casing

    @cached_property
    def eeoc(self) -> EEOCResourceWithRawResponse:
        return EEOCResourceWithRawResponse(self._casing.eeoc)


class AsyncCasingWithRawResponse:
    def __init__(self, casing: AsyncCasing) -> None:
        self._casing = casing

    @cached_property
    def eeoc(self) -> AsyncEEOCResourceWithRawResponse:
        return AsyncEEOCResourceWithRawResponse(self._casing.eeoc)


class CasingWithStreamingResponse:
    def __init__(self, casing: Casing) -> None:
        self._casing = casing

    @cached_property
    def eeoc(self) -> EEOCResourceWithStreamingResponse:
        return EEOCResourceWithStreamingResponse(self._casing.eeoc)


class AsyncCasingWithStreamingResponse:
    def __init__(self, casing: AsyncCasing) -> None:
        self._casing = casing

    @cached_property
    def eeoc(self) -> AsyncEEOCResourceWithStreamingResponse:
        return AsyncEEOCResourceWithStreamingResponse(self._casing.eeoc)
