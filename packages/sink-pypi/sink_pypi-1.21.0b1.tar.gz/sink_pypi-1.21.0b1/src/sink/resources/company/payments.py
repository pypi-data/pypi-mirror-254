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
from ...types.company import CompanyPayment

__all__ = ["Payments", "AsyncPayments"]


class Payments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        return PaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsWithStreamingResponse:
        return PaymentsWithStreamingResponse(self)

    def retrieve(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyPayment:
        """
        Get a payment that the company made.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return self._get(
            f"/company/payments/{payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyPayment,
        )


class AsyncPayments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsWithRawResponse:
        return AsyncPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsWithStreamingResponse:
        return AsyncPaymentsWithStreamingResponse(self)

    async def retrieve(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyPayment:
        """
        Get a payment that the company made.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return await self._get(
            f"/company/payments/{payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyPayment,
        )


class PaymentsWithRawResponse:
    def __init__(self, payments: Payments) -> None:
        self._payments = payments

        self.retrieve = to_raw_response_wrapper(
            payments.retrieve,
        )


class AsyncPaymentsWithRawResponse:
    def __init__(self, payments: AsyncPayments) -> None:
        self._payments = payments

        self.retrieve = async_to_raw_response_wrapper(
            payments.retrieve,
        )


class PaymentsWithStreamingResponse:
    def __init__(self, payments: Payments) -> None:
        self._payments = payments

        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )


class AsyncPaymentsWithStreamingResponse:
    def __init__(self, payments: AsyncPayments) -> None:
        self._payments = payments

        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
