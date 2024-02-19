# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import (
    FileCreateMultipartResponse,
    FileWithOptionalParamResponse,
    FileEverythingMultipartResponse,
    file_create_multipart_params,
    file_with_optional_param_params,
    file_everything_multipart_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal
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

__all__ = ["Files", "AsyncFiles"]


class Files(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesWithRawResponse:
        return FilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesWithStreamingResponse:
        return FilesWithStreamingResponse(self)

    def create_multipart(
        self,
        *,
        file: FileTypes,
        purpose: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileCreateMultipartResponse:
        """
        Endpoint for testing file uploads

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "purpose": purpose,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/multipart",
            body=maybe_transform(body, file_create_multipart_params.FileCreateMultipartParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileCreateMultipartResponse,
        )

    def everything_multipart(
        self,
        *,
        b: bool,
        e: Literal["a", "b", "c"],
        file: FileTypes,
        i: int,
        n: float,
        purpose: str,
        s: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileEverythingMultipartResponse:
        """
        Endpoint for testing file uploads with all kinds of properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "b": b,
                "e": e,
                "file": file,
                "i": i,
                "n": n,
                "purpose": purpose,
                "s": s,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/multipart_everything",
            body=maybe_transform(body, file_everything_multipart_params.FileEverythingMultipartParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileEverythingMultipartResponse,
        )

    def with_optional_param(
        self,
        *,
        image: FileTypes,
        prompt: str,
        mask: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileWithOptionalParamResponse:
        """
        Multipart request with a required and an optional file request param.

        Args:
          image: The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask
              is not provided, image must have transparency, which will be used as the mask.

          prompt: A text description of the desired image(s). The maximum length is 1000
              characters.

          mask: An additional image whose fully transparent areas (e.g. where alpha is zero)
              indicate where `image` should be edited. Must be a valid PNG file, less than
              4MB, and have the same dimensions as `image`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "image": image,
                "prompt": prompt,
                "mask": mask,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"], ["mask"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/with_optional_param",
            body=maybe_transform(body, file_with_optional_param_params.FileWithOptionalParamParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileWithOptionalParamResponse,
        )


class AsyncFiles(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesWithRawResponse:
        return AsyncFilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesWithStreamingResponse:
        return AsyncFilesWithStreamingResponse(self)

    async def create_multipart(
        self,
        *,
        file: FileTypes,
        purpose: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileCreateMultipartResponse:
        """
        Endpoint for testing file uploads

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "purpose": purpose,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files/multipart",
            body=maybe_transform(body, file_create_multipart_params.FileCreateMultipartParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileCreateMultipartResponse,
        )

    async def everything_multipart(
        self,
        *,
        b: bool,
        e: Literal["a", "b", "c"],
        file: FileTypes,
        i: int,
        n: float,
        purpose: str,
        s: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileEverythingMultipartResponse:
        """
        Endpoint for testing file uploads with all kinds of properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "b": b,
                "e": e,
                "file": file,
                "i": i,
                "n": n,
                "purpose": purpose,
                "s": s,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files/multipart_everything",
            body=maybe_transform(body, file_everything_multipart_params.FileEverythingMultipartParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileEverythingMultipartResponse,
        )

    async def with_optional_param(
        self,
        *,
        image: FileTypes,
        prompt: str,
        mask: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileWithOptionalParamResponse:
        """
        Multipart request with a required and an optional file request param.

        Args:
          image: The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask
              is not provided, image must have transparency, which will be used as the mask.

          prompt: A text description of the desired image(s). The maximum length is 1000
              characters.

          mask: An additional image whose fully transparent areas (e.g. where alpha is zero)
              indicate where `image` should be edited. Must be a valid PNG file, less than
              4MB, and have the same dimensions as `image`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "image": image,
                "prompt": prompt,
                "mask": mask,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"], ["mask"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files/with_optional_param",
            body=maybe_transform(body, file_with_optional_param_params.FileWithOptionalParamParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileWithOptionalParamResponse,
        )


class FilesWithRawResponse:
    def __init__(self, files: Files) -> None:
        self._files = files

        self.create_multipart = to_raw_response_wrapper(
            files.create_multipart,
        )
        self.everything_multipart = to_raw_response_wrapper(
            files.everything_multipart,
        )
        self.with_optional_param = to_raw_response_wrapper(
            files.with_optional_param,
        )


class AsyncFilesWithRawResponse:
    def __init__(self, files: AsyncFiles) -> None:
        self._files = files

        self.create_multipart = async_to_raw_response_wrapper(
            files.create_multipart,
        )
        self.everything_multipart = async_to_raw_response_wrapper(
            files.everything_multipart,
        )
        self.with_optional_param = async_to_raw_response_wrapper(
            files.with_optional_param,
        )


class FilesWithStreamingResponse:
    def __init__(self, files: Files) -> None:
        self._files = files

        self.create_multipart = to_streamed_response_wrapper(
            files.create_multipart,
        )
        self.everything_multipart = to_streamed_response_wrapper(
            files.everything_multipart,
        )
        self.with_optional_param = to_streamed_response_wrapper(
            files.with_optional_param,
        )


class AsyncFilesWithStreamingResponse:
    def __init__(self, files: AsyncFiles) -> None:
        self._files = files

        self.create_multipart = async_to_streamed_response_wrapper(
            files.create_multipart,
        )
        self.everything_multipart = async_to_streamed_response_wrapper(
            files.everything_multipart,
        )
        self.with_optional_param = async_to_streamed_response_wrapper(
            files.with_optional_param,
        )
