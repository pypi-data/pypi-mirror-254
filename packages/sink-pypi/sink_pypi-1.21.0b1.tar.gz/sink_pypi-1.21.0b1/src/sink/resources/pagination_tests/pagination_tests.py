# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .refs import (
    Refs,
    AsyncRefs,
    RefsWithRawResponse,
    AsyncRefsWithRawResponse,
    RefsWithStreamingResponse,
    AsyncRefsWithStreamingResponse,
)
from .cursor import (
    Cursor,
    AsyncCursor,
    CursorWithRawResponse,
    AsyncCursorWithRawResponse,
    CursorWithStreamingResponse,
    AsyncCursorWithStreamingResponse,
)
from .offset import (
    Offset,
    AsyncOffset,
    OffsetWithRawResponse,
    AsyncOffsetWithRawResponse,
    OffsetWithStreamingResponse,
    AsyncOffsetWithStreamingResponse,
)
from ..._compat import cached_property
from .cursor_id import (
    CursorID,
    AsyncCursorID,
    CursorIDWithRawResponse,
    AsyncCursorIDWithRawResponse,
    CursorIDWithStreamingResponse,
    AsyncCursorIDWithStreamingResponse,
)
from .fake_pages import (
    FakePages,
    AsyncFakePages,
    FakePagesWithRawResponse,
    AsyncFakePagesWithRawResponse,
    FakePagesWithStreamingResponse,
    AsyncFakePagesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .items_types import (
    ItemsTypes,
    AsyncItemsTypes,
    ItemsTypesWithRawResponse,
    AsyncItemsTypesWithRawResponse,
    ItemsTypesWithStreamingResponse,
    AsyncItemsTypesWithStreamingResponse,
)
from .page_number import (
    PageNumber,
    AsyncPageNumber,
    PageNumberWithRawResponse,
    AsyncPageNumberWithRawResponse,
    PageNumberWithStreamingResponse,
    AsyncPageNumberWithStreamingResponse,
)
from .response_headers import (
    ResponseHeaders,
    AsyncResponseHeaders,
    ResponseHeadersWithRawResponse,
    AsyncResponseHeadersWithRawResponse,
    ResponseHeadersWithStreamingResponse,
    AsyncResponseHeadersWithStreamingResponse,
)
from .top_level_arrays import (
    TopLevelArrays,
    AsyncTopLevelArrays,
    TopLevelArraysWithRawResponse,
    AsyncTopLevelArraysWithRawResponse,
    TopLevelArraysWithStreamingResponse,
    AsyncTopLevelArraysWithStreamingResponse,
)

__all__ = ["PaginationTests", "AsyncPaginationTests"]


class PaginationTests(SyncAPIResource):
    @cached_property
    def items_types(self) -> ItemsTypes:
        return ItemsTypes(self._client)

    @cached_property
    def page_number(self) -> PageNumber:
        return PageNumber(self._client)

    @cached_property
    def refs(self) -> Refs:
        return Refs(self._client)

    @cached_property
    def response_headers(self) -> ResponseHeaders:
        return ResponseHeaders(self._client)

    @cached_property
    def top_level_arrays(self) -> TopLevelArrays:
        return TopLevelArrays(self._client)

    @cached_property
    def cursor(self) -> Cursor:
        return Cursor(self._client)

    @cached_property
    def cursor_id(self) -> CursorID:
        return CursorID(self._client)

    @cached_property
    def offset(self) -> Offset:
        return Offset(self._client)

    @cached_property
    def fake_pages(self) -> FakePages:
        return FakePages(self._client)

    @cached_property
    def with_raw_response(self) -> PaginationTestsWithRawResponse:
        return PaginationTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaginationTestsWithStreamingResponse:
        return PaginationTestsWithStreamingResponse(self)


class AsyncPaginationTests(AsyncAPIResource):
    @cached_property
    def items_types(self) -> AsyncItemsTypes:
        return AsyncItemsTypes(self._client)

    @cached_property
    def page_number(self) -> AsyncPageNumber:
        return AsyncPageNumber(self._client)

    @cached_property
    def refs(self) -> AsyncRefs:
        return AsyncRefs(self._client)

    @cached_property
    def response_headers(self) -> AsyncResponseHeaders:
        return AsyncResponseHeaders(self._client)

    @cached_property
    def top_level_arrays(self) -> AsyncTopLevelArrays:
        return AsyncTopLevelArrays(self._client)

    @cached_property
    def cursor(self) -> AsyncCursor:
        return AsyncCursor(self._client)

    @cached_property
    def cursor_id(self) -> AsyncCursorID:
        return AsyncCursorID(self._client)

    @cached_property
    def offset(self) -> AsyncOffset:
        return AsyncOffset(self._client)

    @cached_property
    def fake_pages(self) -> AsyncFakePages:
        return AsyncFakePages(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPaginationTestsWithRawResponse:
        return AsyncPaginationTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaginationTestsWithStreamingResponse:
        return AsyncPaginationTestsWithStreamingResponse(self)


class PaginationTestsWithRawResponse:
    def __init__(self, pagination_tests: PaginationTests) -> None:
        self._pagination_tests = pagination_tests

    @cached_property
    def items_types(self) -> ItemsTypesWithRawResponse:
        return ItemsTypesWithRawResponse(self._pagination_tests.items_types)

    @cached_property
    def page_number(self) -> PageNumberWithRawResponse:
        return PageNumberWithRawResponse(self._pagination_tests.page_number)

    @cached_property
    def refs(self) -> RefsWithRawResponse:
        return RefsWithRawResponse(self._pagination_tests.refs)

    @cached_property
    def response_headers(self) -> ResponseHeadersWithRawResponse:
        return ResponseHeadersWithRawResponse(self._pagination_tests.response_headers)

    @cached_property
    def top_level_arrays(self) -> TopLevelArraysWithRawResponse:
        return TopLevelArraysWithRawResponse(self._pagination_tests.top_level_arrays)

    @cached_property
    def cursor(self) -> CursorWithRawResponse:
        return CursorWithRawResponse(self._pagination_tests.cursor)

    @cached_property
    def cursor_id(self) -> CursorIDWithRawResponse:
        return CursorIDWithRawResponse(self._pagination_tests.cursor_id)

    @cached_property
    def offset(self) -> OffsetWithRawResponse:
        return OffsetWithRawResponse(self._pagination_tests.offset)

    @cached_property
    def fake_pages(self) -> FakePagesWithRawResponse:
        return FakePagesWithRawResponse(self._pagination_tests.fake_pages)


class AsyncPaginationTestsWithRawResponse:
    def __init__(self, pagination_tests: AsyncPaginationTests) -> None:
        self._pagination_tests = pagination_tests

    @cached_property
    def items_types(self) -> AsyncItemsTypesWithRawResponse:
        return AsyncItemsTypesWithRawResponse(self._pagination_tests.items_types)

    @cached_property
    def page_number(self) -> AsyncPageNumberWithRawResponse:
        return AsyncPageNumberWithRawResponse(self._pagination_tests.page_number)

    @cached_property
    def refs(self) -> AsyncRefsWithRawResponse:
        return AsyncRefsWithRawResponse(self._pagination_tests.refs)

    @cached_property
    def response_headers(self) -> AsyncResponseHeadersWithRawResponse:
        return AsyncResponseHeadersWithRawResponse(self._pagination_tests.response_headers)

    @cached_property
    def top_level_arrays(self) -> AsyncTopLevelArraysWithRawResponse:
        return AsyncTopLevelArraysWithRawResponse(self._pagination_tests.top_level_arrays)

    @cached_property
    def cursor(self) -> AsyncCursorWithRawResponse:
        return AsyncCursorWithRawResponse(self._pagination_tests.cursor)

    @cached_property
    def cursor_id(self) -> AsyncCursorIDWithRawResponse:
        return AsyncCursorIDWithRawResponse(self._pagination_tests.cursor_id)

    @cached_property
    def offset(self) -> AsyncOffsetWithRawResponse:
        return AsyncOffsetWithRawResponse(self._pagination_tests.offset)

    @cached_property
    def fake_pages(self) -> AsyncFakePagesWithRawResponse:
        return AsyncFakePagesWithRawResponse(self._pagination_tests.fake_pages)


class PaginationTestsWithStreamingResponse:
    def __init__(self, pagination_tests: PaginationTests) -> None:
        self._pagination_tests = pagination_tests

    @cached_property
    def items_types(self) -> ItemsTypesWithStreamingResponse:
        return ItemsTypesWithStreamingResponse(self._pagination_tests.items_types)

    @cached_property
    def page_number(self) -> PageNumberWithStreamingResponse:
        return PageNumberWithStreamingResponse(self._pagination_tests.page_number)

    @cached_property
    def refs(self) -> RefsWithStreamingResponse:
        return RefsWithStreamingResponse(self._pagination_tests.refs)

    @cached_property
    def response_headers(self) -> ResponseHeadersWithStreamingResponse:
        return ResponseHeadersWithStreamingResponse(self._pagination_tests.response_headers)

    @cached_property
    def top_level_arrays(self) -> TopLevelArraysWithStreamingResponse:
        return TopLevelArraysWithStreamingResponse(self._pagination_tests.top_level_arrays)

    @cached_property
    def cursor(self) -> CursorWithStreamingResponse:
        return CursorWithStreamingResponse(self._pagination_tests.cursor)

    @cached_property
    def cursor_id(self) -> CursorIDWithStreamingResponse:
        return CursorIDWithStreamingResponse(self._pagination_tests.cursor_id)

    @cached_property
    def offset(self) -> OffsetWithStreamingResponse:
        return OffsetWithStreamingResponse(self._pagination_tests.offset)

    @cached_property
    def fake_pages(self) -> FakePagesWithStreamingResponse:
        return FakePagesWithStreamingResponse(self._pagination_tests.fake_pages)


class AsyncPaginationTestsWithStreamingResponse:
    def __init__(self, pagination_tests: AsyncPaginationTests) -> None:
        self._pagination_tests = pagination_tests

    @cached_property
    def items_types(self) -> AsyncItemsTypesWithStreamingResponse:
        return AsyncItemsTypesWithStreamingResponse(self._pagination_tests.items_types)

    @cached_property
    def page_number(self) -> AsyncPageNumberWithStreamingResponse:
        return AsyncPageNumberWithStreamingResponse(self._pagination_tests.page_number)

    @cached_property
    def refs(self) -> AsyncRefsWithStreamingResponse:
        return AsyncRefsWithStreamingResponse(self._pagination_tests.refs)

    @cached_property
    def response_headers(self) -> AsyncResponseHeadersWithStreamingResponse:
        return AsyncResponseHeadersWithStreamingResponse(self._pagination_tests.response_headers)

    @cached_property
    def top_level_arrays(self) -> AsyncTopLevelArraysWithStreamingResponse:
        return AsyncTopLevelArraysWithStreamingResponse(self._pagination_tests.top_level_arrays)

    @cached_property
    def cursor(self) -> AsyncCursorWithStreamingResponse:
        return AsyncCursorWithStreamingResponse(self._pagination_tests.cursor)

    @cached_property
    def cursor_id(self) -> AsyncCursorIDWithStreamingResponse:
        return AsyncCursorIDWithStreamingResponse(self._pagination_tests.cursor_id)

    @cached_property
    def offset(self) -> AsyncOffsetWithStreamingResponse:
        return AsyncOffsetWithStreamingResponse(self._pagination_tests.offset)

    @cached_property
    def fake_pages(self) -> AsyncFakePagesWithStreamingResponse:
        return AsyncFakePagesWithStreamingResponse(self._pagination_tests.fake_pages)
