# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .payments import (
    Payments,
    AsyncPayments,
    PaymentsWithRawResponse,
    AsyncPaymentsWithRawResponse,
    PaymentsWithStreamingResponse,
    AsyncPaymentsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CompanyResource", "AsyncCompanyResource"]


class CompanyResource(SyncAPIResource):
    @cached_property
    def payments(self) -> Payments:
        return Payments(self._client)

    @cached_property
    def with_raw_response(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self)


class AsyncCompanyResource(AsyncAPIResource):
    @cached_property
    def payments(self) -> AsyncPayments:
        return AsyncPayments(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self)


class CompanyResourceWithRawResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

    @cached_property
    def payments(self) -> PaymentsWithRawResponse:
        return PaymentsWithRawResponse(self._company.payments)


class AsyncCompanyResourceWithRawResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

    @cached_property
    def payments(self) -> AsyncPaymentsWithRawResponse:
        return AsyncPaymentsWithRawResponse(self._company.payments)


class CompanyResourceWithStreamingResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

    @cached_property
    def payments(self) -> PaymentsWithStreamingResponse:
        return PaymentsWithStreamingResponse(self._company.payments)


class AsyncCompanyResourceWithStreamingResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

    @cached_property
    def payments(self) -> AsyncPaymentsWithStreamingResponse:
        return AsyncPaymentsWithStreamingResponse(self._company.payments)
