# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Union, cast, overload
from datetime import date

import httpx

from .params import (
    Params,
    AsyncParams,
    ParamsWithRawResponse,
    AsyncParamsWithRawResponse,
    ParamsWithStreamingResponse,
    AsyncParamsWithStreamingResponse,
)
from .unions import (
    Unions,
    AsyncUnions,
    UnionsWithRawResponse,
    AsyncUnionsWithRawResponse,
    UnionsWithStreamingResponse,
    AsyncUnionsWithStreamingResponse,
)
from ...types import (
    NameChildPropImportClashResponse,
    NameResponseShadowsPydanticResponse,
    NamePropertiesCommonConflictsResponse,
    NameResponsePropertyClashesModelImportResponse,
    NamePropertiesIllegalJavascriptIdentifiersResponse,
    name_properties_common_conflicts_params,
    name_properties_illegal_javascript_identifiers_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .renaming import (
    Renaming,
    AsyncRenaming,
    RenamingWithRawResponse,
    AsyncRenamingWithRawResponse,
    RenamingWithStreamingResponse,
    AsyncRenamingWithStreamingResponse,
)
from ..._compat import cached_property
from .documents import (
    Documents,
    AsyncDocuments,
    DocumentsWithRawResponse,
    AsyncDocumentsWithRawResponse,
    DocumentsWithStreamingResponse,
    AsyncDocumentsWithStreamingResponse,
)
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
from ...types.shared import BasicSharedModelObject
from .reserved_names import (
    ReservedNames,
    AsyncReservedNames,
    ReservedNamesWithRawResponse,
    AsyncReservedNamesWithRawResponse,
    ReservedNamesWithStreamingResponse,
    AsyncReservedNamesWithStreamingResponse,
)
from .reserved_names.reserved_names import ReservedNames, AsyncReservedNames

__all__ = ["Names", "AsyncNames"]


class Names(SyncAPIResource):
    @cached_property
    def unions(self) -> Unions:
        return Unions(self._client)

    @cached_property
    def renaming(self) -> Renaming:
        return Renaming(self._client)

    @cached_property
    def documents(self) -> Documents:
        return Documents(self._client)

    @cached_property
    def reserved_names(self) -> ReservedNames:
        return ReservedNames(self._client)

    @cached_property
    def params(self) -> Params:
        return Params(self._client)

    @cached_property
    def with_raw_response(self) -> NamesWithRawResponse:
        return NamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamesWithStreamingResponse:
        return NamesWithStreamingResponse(self)

    def child_prop_import_clash(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NameChildPropImportClashResponse:
        """
        Endpoint with request & response properties that could cause clashes due to
        imports.
        """
        return self._post(
            "/names/child_prop_import_clash",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NameChildPropImportClashResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """Endpoint with the name `get` in the config."""
        return self._get(
            "/names/method_name_get",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )

    def properties_common_conflicts(
        self,
        *,
        _1_digit_leading_underscore: str,
        _leading_underscore: str,
        _leading_underscore_mixed_case: str,
        bool: bool,
        bool_2: bool,
        date: Union[str, date],
        date_2: Union[str, date],
        float: float,
        float_2: float,
        int: int,
        int_2: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesCommonConflictsResponse:
        """
        Endpoint with request & response properties that are likely to cause name
        conflicts.

        Args:
          _1_digit_leading_underscore: In certain languages the leading underscore in combination with this property
              name may cause issues

          _leading_underscore: In certain languages the leading underscore in this property name may cause
              issues

          _leading_underscore_mixed_case: In certain languages the leading underscore in this property name may cause
              issues alongside a case change

          bool_2: In certain languages the type declaration for this prop can shadow the `bool`
              property declaration.

          date: This shadows the stdlib `datetime.date` type in Python & causes type errors.

          date_2: In certain languages the type declaration for this prop can shadow the `date`
              property declaration.

          float_2: In certain languages the type declaration for this prop can shadow the `float`
              property declaration.

          int_2: In certain languages the type declaration for this prop can shadow the `int`
              property declaration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/names/properties_common_conflicts",
            body=maybe_transform(
                {
                    "_1_digit_leading_underscore": _1_digit_leading_underscore,
                    "_leading_underscore": _leading_underscore,
                    "_leading_underscore_mixed_case": _leading_underscore_mixed_case,
                    "bool": bool,
                    "bool_2": bool_2,
                    "date": date,
                    "date_2": date_2,
                    "float": float,
                    "float_2": float_2,
                    "int": int,
                    "int_2": int_2,
                },
                name_properties_common_conflicts_params.NamePropertiesCommonConflictsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NamePropertiesCommonConflictsResponse,
        )

    @overload
    def properties_illegal_javascript_identifiers(
        self,
        *,
        irrelevant: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesIllegalJavascriptIdentifiersResponse:
        """
        Endpoint with request & response properties with names that aren't legal
        javascript identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def properties_illegal_javascript_identifiers(
        self,
        *,
        body: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesIllegalJavascriptIdentifiersResponse:
        """
        Endpoint with request & response properties with names that aren't legal
        javascript identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    def properties_illegal_javascript_identifiers(
        self,
        *,
        irrelevant: float | NotGiven = NOT_GIVEN,
        body: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesIllegalJavascriptIdentifiersResponse:
        return cast(
            NamePropertiesIllegalJavascriptIdentifiersResponse,
            self._post(
                "/names/properties_illegal_javascript_identifiers",
                body=maybe_transform(
                    {
                        "irrelevant": irrelevant,
                        "body": body,
                    },
                    name_properties_illegal_javascript_identifiers_params.NamePropertiesIllegalJavascriptIdentifiersParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, NamePropertiesIllegalJavascriptIdentifiersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def response_property_clashes_model_import(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameResponsePropertyClashesModelImportResponse:
        """
        Endpoint with a response model property that can cause clashes with a model
        import.
        """
        return self._get(
            "/names/response_property_clashes_model_import",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameResponsePropertyClashesModelImportResponse,
        )

    def response_shadows_pydantic(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameResponseShadowsPydanticResponse:
        """Endpoint with a response model property that would clash with pydantic."""
        return self._get(
            "/names/response_property_shadows_pydantic",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameResponseShadowsPydanticResponse,
        )


class AsyncNames(AsyncAPIResource):
    @cached_property
    def unions(self) -> AsyncUnions:
        return AsyncUnions(self._client)

    @cached_property
    def renaming(self) -> AsyncRenaming:
        return AsyncRenaming(self._client)

    @cached_property
    def documents(self) -> AsyncDocuments:
        return AsyncDocuments(self._client)

    @cached_property
    def reserved_names(self) -> AsyncReservedNames:
        return AsyncReservedNames(self._client)

    @cached_property
    def params(self) -> AsyncParams:
        return AsyncParams(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamesWithRawResponse:
        return AsyncNamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamesWithStreamingResponse:
        return AsyncNamesWithStreamingResponse(self)

    async def child_prop_import_clash(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NameChildPropImportClashResponse:
        """
        Endpoint with request & response properties that could cause clashes due to
        imports.
        """
        return await self._post(
            "/names/child_prop_import_clash",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NameChildPropImportClashResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicSharedModelObject:
        """Endpoint with the name `get` in the config."""
        return await self._get(
            "/names/method_name_get",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicSharedModelObject,
        )

    async def properties_common_conflicts(
        self,
        *,
        _1_digit_leading_underscore: str,
        _leading_underscore: str,
        _leading_underscore_mixed_case: str,
        bool: bool,
        bool_2: bool,
        date: Union[str, date],
        date_2: Union[str, date],
        float: float,
        float_2: float,
        int: int,
        int_2: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesCommonConflictsResponse:
        """
        Endpoint with request & response properties that are likely to cause name
        conflicts.

        Args:
          _1_digit_leading_underscore: In certain languages the leading underscore in combination with this property
              name may cause issues

          _leading_underscore: In certain languages the leading underscore in this property name may cause
              issues

          _leading_underscore_mixed_case: In certain languages the leading underscore in this property name may cause
              issues alongside a case change

          bool_2: In certain languages the type declaration for this prop can shadow the `bool`
              property declaration.

          date: This shadows the stdlib `datetime.date` type in Python & causes type errors.

          date_2: In certain languages the type declaration for this prop can shadow the `date`
              property declaration.

          float_2: In certain languages the type declaration for this prop can shadow the `float`
              property declaration.

          int_2: In certain languages the type declaration for this prop can shadow the `int`
              property declaration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/names/properties_common_conflicts",
            body=maybe_transform(
                {
                    "_1_digit_leading_underscore": _1_digit_leading_underscore,
                    "_leading_underscore": _leading_underscore,
                    "_leading_underscore_mixed_case": _leading_underscore_mixed_case,
                    "bool": bool,
                    "bool_2": bool_2,
                    "date": date,
                    "date_2": date_2,
                    "float": float,
                    "float_2": float_2,
                    "int": int,
                    "int_2": int_2,
                },
                name_properties_common_conflicts_params.NamePropertiesCommonConflictsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NamePropertiesCommonConflictsResponse,
        )

    @overload
    async def properties_illegal_javascript_identifiers(
        self,
        *,
        irrelevant: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesIllegalJavascriptIdentifiersResponse:
        """
        Endpoint with request & response properties with names that aren't legal
        javascript identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def properties_illegal_javascript_identifiers(
        self,
        *,
        body: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesIllegalJavascriptIdentifiersResponse:
        """
        Endpoint with request & response properties with names that aren't legal
        javascript identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    async def properties_illegal_javascript_identifiers(
        self,
        *,
        irrelevant: float | NotGiven = NOT_GIVEN,
        body: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> NamePropertiesIllegalJavascriptIdentifiersResponse:
        return cast(
            NamePropertiesIllegalJavascriptIdentifiersResponse,
            await self._post(
                "/names/properties_illegal_javascript_identifiers",
                body=maybe_transform(
                    {
                        "irrelevant": irrelevant,
                        "body": body,
                    },
                    name_properties_illegal_javascript_identifiers_params.NamePropertiesIllegalJavascriptIdentifiersParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, NamePropertiesIllegalJavascriptIdentifiersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def response_property_clashes_model_import(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameResponsePropertyClashesModelImportResponse:
        """
        Endpoint with a response model property that can cause clashes with a model
        import.
        """
        return await self._get(
            "/names/response_property_clashes_model_import",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameResponsePropertyClashesModelImportResponse,
        )

    async def response_shadows_pydantic(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NameResponseShadowsPydanticResponse:
        """Endpoint with a response model property that would clash with pydantic."""
        return await self._get(
            "/names/response_property_shadows_pydantic",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NameResponseShadowsPydanticResponse,
        )


class NamesWithRawResponse:
    def __init__(self, names: Names) -> None:
        self._names = names

        self.child_prop_import_clash = to_raw_response_wrapper(
            names.child_prop_import_clash,
        )
        self.get = to_raw_response_wrapper(
            names.get,
        )
        self.properties_common_conflicts = to_raw_response_wrapper(
            names.properties_common_conflicts,
        )
        self.properties_illegal_javascript_identifiers = to_raw_response_wrapper(
            names.properties_illegal_javascript_identifiers,
        )
        self.response_property_clashes_model_import = to_raw_response_wrapper(
            names.response_property_clashes_model_import,
        )
        self.response_shadows_pydantic = to_raw_response_wrapper(
            names.response_shadows_pydantic,
        )

    @cached_property
    def unions(self) -> UnionsWithRawResponse:
        return UnionsWithRawResponse(self._names.unions)

    @cached_property
    def renaming(self) -> RenamingWithRawResponse:
        return RenamingWithRawResponse(self._names.renaming)

    @cached_property
    def documents(self) -> DocumentsWithRawResponse:
        return DocumentsWithRawResponse(self._names.documents)

    @cached_property
    def reserved_names(self) -> ReservedNamesWithRawResponse:
        return ReservedNamesWithRawResponse(self._names.reserved_names)

    @cached_property
    def params(self) -> ParamsWithRawResponse:
        return ParamsWithRawResponse(self._names.params)


class AsyncNamesWithRawResponse:
    def __init__(self, names: AsyncNames) -> None:
        self._names = names

        self.child_prop_import_clash = async_to_raw_response_wrapper(
            names.child_prop_import_clash,
        )
        self.get = async_to_raw_response_wrapper(
            names.get,
        )
        self.properties_common_conflicts = async_to_raw_response_wrapper(
            names.properties_common_conflicts,
        )
        self.properties_illegal_javascript_identifiers = async_to_raw_response_wrapper(
            names.properties_illegal_javascript_identifiers,
        )
        self.response_property_clashes_model_import = async_to_raw_response_wrapper(
            names.response_property_clashes_model_import,
        )
        self.response_shadows_pydantic = async_to_raw_response_wrapper(
            names.response_shadows_pydantic,
        )

    @cached_property
    def unions(self) -> AsyncUnionsWithRawResponse:
        return AsyncUnionsWithRawResponse(self._names.unions)

    @cached_property
    def renaming(self) -> AsyncRenamingWithRawResponse:
        return AsyncRenamingWithRawResponse(self._names.renaming)

    @cached_property
    def documents(self) -> AsyncDocumentsWithRawResponse:
        return AsyncDocumentsWithRawResponse(self._names.documents)

    @cached_property
    def reserved_names(self) -> AsyncReservedNamesWithRawResponse:
        return AsyncReservedNamesWithRawResponse(self._names.reserved_names)

    @cached_property
    def params(self) -> AsyncParamsWithRawResponse:
        return AsyncParamsWithRawResponse(self._names.params)


class NamesWithStreamingResponse:
    def __init__(self, names: Names) -> None:
        self._names = names

        self.child_prop_import_clash = to_streamed_response_wrapper(
            names.child_prop_import_clash,
        )
        self.get = to_streamed_response_wrapper(
            names.get,
        )
        self.properties_common_conflicts = to_streamed_response_wrapper(
            names.properties_common_conflicts,
        )
        self.properties_illegal_javascript_identifiers = to_streamed_response_wrapper(
            names.properties_illegal_javascript_identifiers,
        )
        self.response_property_clashes_model_import = to_streamed_response_wrapper(
            names.response_property_clashes_model_import,
        )
        self.response_shadows_pydantic = to_streamed_response_wrapper(
            names.response_shadows_pydantic,
        )

    @cached_property
    def unions(self) -> UnionsWithStreamingResponse:
        return UnionsWithStreamingResponse(self._names.unions)

    @cached_property
    def renaming(self) -> RenamingWithStreamingResponse:
        return RenamingWithStreamingResponse(self._names.renaming)

    @cached_property
    def documents(self) -> DocumentsWithStreamingResponse:
        return DocumentsWithStreamingResponse(self._names.documents)

    @cached_property
    def reserved_names(self) -> ReservedNamesWithStreamingResponse:
        return ReservedNamesWithStreamingResponse(self._names.reserved_names)

    @cached_property
    def params(self) -> ParamsWithStreamingResponse:
        return ParamsWithStreamingResponse(self._names.params)


class AsyncNamesWithStreamingResponse:
    def __init__(self, names: AsyncNames) -> None:
        self._names = names

        self.child_prop_import_clash = async_to_streamed_response_wrapper(
            names.child_prop_import_clash,
        )
        self.get = async_to_streamed_response_wrapper(
            names.get,
        )
        self.properties_common_conflicts = async_to_streamed_response_wrapper(
            names.properties_common_conflicts,
        )
        self.properties_illegal_javascript_identifiers = async_to_streamed_response_wrapper(
            names.properties_illegal_javascript_identifiers,
        )
        self.response_property_clashes_model_import = async_to_streamed_response_wrapper(
            names.response_property_clashes_model_import,
        )
        self.response_shadows_pydantic = async_to_streamed_response_wrapper(
            names.response_shadows_pydantic,
        )

    @cached_property
    def unions(self) -> AsyncUnionsWithStreamingResponse:
        return AsyncUnionsWithStreamingResponse(self._names.unions)

    @cached_property
    def renaming(self) -> AsyncRenamingWithStreamingResponse:
        return AsyncRenamingWithStreamingResponse(self._names.renaming)

    @cached_property
    def documents(self) -> AsyncDocumentsWithStreamingResponse:
        return AsyncDocumentsWithStreamingResponse(self._names.documents)

    @cached_property
    def reserved_names(self) -> AsyncReservedNamesWithStreamingResponse:
        return AsyncReservedNamesWithStreamingResponse(self._names.reserved_names)

    @cached_property
    def params(self) -> AsyncParamsWithStreamingResponse:
        return AsyncParamsWithStreamingResponse(self._names.params)
