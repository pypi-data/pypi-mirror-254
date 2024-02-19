# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import json
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources as _resources, _constants, _exceptions
from ._qs import Querystring
from .types import APIStatus
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NoneType,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
    maybe_coerce_float,
    maybe_coerce_boolean,
    maybe_coerce_integer,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SinkError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "_resources",
    "Sink",
    "AsyncSink",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://demo.stainlessapi.com/",
    "sandbox": "https://demo-sanbox.stainlessapi.com/",
}


class Sink(SyncAPIClient):
    testing: _resources.Testing
    complex_queries: _resources.ComplexQueries
    casing: _resources.Casing
    default_req_options: _resources.DefaultReqOptions
    tools: _resources.Tools
    method_config: _resources.MethodConfig
    streaming: _resources.Streaming
    pagination_tests: _resources.PaginationTests
    docstrings: _resources.Docstrings
    invalid_schemas: _resources.InvalidSchemas
    resource_refs: _resources.ResourceRefs
    cards: _resources.Cards
    files: _resources.Files
    binaries: _resources.Binaries
    resources: _resources.Resources
    config_tools: _resources.ConfigTools
    company: _resources.CompanyResource
    openapi_formats: _resources.OpenapiFormats
    parent: _resources.Parent
    envelopes: _resources.Envelopes
    types: _resources.Types
    names: _resources.Names
    widgets: _resources.Widgets
    client_params: _resources.ClientParams
    responses: _resources.Responses
    path_params: _resources.PathParams
    positional_params: _resources.PositionalParams
    empty_body: _resources.EmptyBody
    query_params: _resources.QueryParams
    body_params: _resources.BodyParams
    header_params: _resources.HeaderParams
    mixed_params: _resources.MixedParams
    make_ambiguous_schemas_looser: _resources.MakeAmbiguousSchemasLooser
    make_ambiguous_schemas_explicit: _resources.MakeAmbiguousSchemasExplicit
    decorator_tests: _resources.DecoratorTests
    tests: _resources.Tests
    deeply_nested: _resources.DeeplyNested
    version_1_30_names: _resources.Version1_30Names
    recursion: _resources.Recursion
    shared_query_params: _resources.SharedQueryParams
    model_referenced_in_parent_and_child: _resources.ModelReferencedInParentAndChildResource
    only_custom_methods: _resources.OnlyCustomMethods
    with_raw_response: SinkWithRawResponse
    with_streaming_response: SinkWithStreamedResponse

    # client options
    user_token: str | None
    username: str
    client_id: str | None
    client_secret: str | None
    some_boolean_arg: bool | None
    some_integer_arg: int | None
    some_number_arg: float | None
    some_number_arg_required: float
    some_number_arg_required_no_default: float
    some_number_arg_required_no_default_no_env: float
    required_arg_no_env: str
    required_arg_no_env_with_default: str
    client_path_param: str | None
    camel_case_path: str | None
    client_query_param: str | None
    client_path_or_query_param: str | None

    # constants
    CONSTANT_WITH_NEWLINES = _constants.CONSTANT_WITH_NEWLINES

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        user_token: str | None = None,
        username: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        some_boolean_arg: bool | None = None,
        some_integer_arg: int | None = None,
        some_number_arg: float | None = None,
        some_number_arg_required: float | None = None,
        some_number_arg_required_no_default: float | None = None,
        some_number_arg_required_no_default_no_env: float,
        required_arg_no_env: str,
        required_arg_no_env_with_default: str | None = "hi!",
        client_path_param: str | None = None,
        camel_case_path: str | None = None,
        client_query_param: str | None = None,
        client_path_or_query_param: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous sink client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `user_token` from `SINK_CUSTOM_API_KEY_ENV`
        - `username` from `SINK_USER`
        - `client_id` from `SINK_CLIENT_ID`
        - `client_secret` from `SINK_CLIENT_SECRET`
        - `some_boolean_arg` from `SINK_SOME_BOOLEAN_ARG`
        - `some_integer_arg` from `SINK_SOME_INTEGER_ARG`
        - `some_number_arg` from `SINK_SOME_NUMBER_ARG`
        - `some_number_arg_required` from `SINK_SOME_NUMBER_ARG`
        - `some_number_arg_required_no_default` from `SINK_SOME_NUMBER_ARG`
        """
        if user_token is None:
            user_token = os.environ.get("SINK_CUSTOM_API_KEY_ENV")
        self.user_token = user_token

        if username is None:
            username = os.environ.get("SINK_USER")
        if username is None:
            raise SinkError(
                "The username client option must be set either by passing username to the client or by setting the SINK_USER environment variable"
            )
        self.username = username

        if client_id is None:
            client_id = os.environ.get("SINK_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("SINK_CLIENT_SECRET") or "hellosecret"
        self.client_secret = client_secret

        if some_boolean_arg is None:
            some_boolean_arg = maybe_coerce_boolean(os.environ.get("SINK_SOME_BOOLEAN_ARG")) or True
        self.some_boolean_arg = some_boolean_arg

        if some_integer_arg is None:
            some_integer_arg = maybe_coerce_integer(os.environ.get("SINK_SOME_INTEGER_ARG")) or 123
        self.some_integer_arg = some_integer_arg

        if some_number_arg is None:
            some_number_arg = maybe_coerce_float(os.environ.get("SINK_SOME_NUMBER_ARG")) or 1.2
        self.some_number_arg = some_number_arg

        if some_number_arg_required is None:
            some_number_arg_required = maybe_coerce_float(os.environ.get("SINK_SOME_NUMBER_ARG")) or 1.2
        self.some_number_arg_required = some_number_arg_required

        if some_number_arg_required_no_default is None:
            some_number_arg_required_no_default = maybe_coerce_float(os.environ.get("SINK_SOME_NUMBER_ARG"))
        if some_number_arg_required_no_default is None:
            raise SinkError(
                "The some_number_arg_required_no_default client option must be set either by passing some_number_arg_required_no_default to the client or by setting the SINK_SOME_NUMBER_ARG environment variable"
            )
        self.some_number_arg_required_no_default = some_number_arg_required_no_default

        self.some_number_arg_required_no_default_no_env = some_number_arg_required_no_default_no_env

        self.required_arg_no_env = required_arg_no_env

        if required_arg_no_env_with_default is None:
            required_arg_no_env_with_default = "hi!"
        self.required_arg_no_env_with_default = required_arg_no_env_with_default

        self.client_path_param = client_path_param

        self.camel_case_path = camel_case_path

        self.client_query_param = client_query_param

        self.client_path_or_query_param = client_path_or_query_param

        self._environment = environment

        base_url_env = os.environ.get("SINK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SINK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self._default_stream_cls = Stream

        self.testing = _resources.Testing(self)
        self.complex_queries = _resources.ComplexQueries(self)
        self.casing = _resources.Casing(self)
        self.default_req_options = _resources.DefaultReqOptions(self)
        self.tools = _resources.Tools(self)
        self.method_config = _resources.MethodConfig(self)
        self.streaming = _resources.Streaming(self)
        self.pagination_tests = _resources.PaginationTests(self)
        self.docstrings = _resources.Docstrings(self)
        self.invalid_schemas = _resources.InvalidSchemas(self)
        self.resource_refs = _resources.ResourceRefs(self)
        self.cards = _resources.Cards(self)
        self.files = _resources.Files(self)
        self.binaries = _resources.Binaries(self)
        self.resources = _resources.Resources(self)
        self.config_tools = _resources.ConfigTools(self)
        self.company = _resources.CompanyResource(self)
        self.openapi_formats = _resources.OpenapiFormats(self)
        self.parent = _resources.Parent(self)
        self.envelopes = _resources.Envelopes(self)
        self.types = _resources.Types(self)
        self.names = _resources.Names(self)
        self.widgets = _resources.Widgets(self)
        self.client_params = _resources.ClientParams(self)
        self.responses = _resources.Responses(self)
        self.path_params = _resources.PathParams(self)
        self.positional_params = _resources.PositionalParams(self)
        self.empty_body = _resources.EmptyBody(self)
        self.query_params = _resources.QueryParams(self)
        self.body_params = _resources.BodyParams(self)
        self.header_params = _resources.HeaderParams(self)
        self.mixed_params = _resources.MixedParams(self)
        self.make_ambiguous_schemas_looser = _resources.MakeAmbiguousSchemasLooser(self)
        self.make_ambiguous_schemas_explicit = _resources.MakeAmbiguousSchemasExplicit(self)
        self.decorator_tests = _resources.DecoratorTests(self)
        self.tests = _resources.Tests(self)
        self.deeply_nested = _resources.DeeplyNested(self)
        self.version_1_30_names = _resources.Version1_30Names(self)
        self.recursion = _resources.Recursion(self)
        self.shared_query_params = _resources.SharedQueryParams(self)
        self.model_referenced_in_parent_and_child = _resources.ModelReferencedInParentAndChildResource(self)
        self.only_custom_methods = _resources.OnlyCustomMethods(self)
        self.with_raw_response = SinkWithRawResponse(self)
        self.with_streaming_response = SinkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        user_token = self.user_token
        if user_token is None:
            return {}
        return {"Authorization": f"Bearer {user_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "My-Api-Version": "11",
            "X-Enable-Metrics": "1",
            "X-Client-UserName": self.username,
            "X-Client-Secret": self.client_secret if self.client_secret is not None else Omit(),
            "X-Integer": str(self.some_integer_arg) if self.some_integer_arg is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.user_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the user_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        user_token: str | None = None,
        username: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        some_boolean_arg: bool | None = None,
        some_integer_arg: int | None = None,
        some_number_arg: float | None = None,
        some_number_arg_required: float | None = None,
        some_number_arg_required_no_default: float | None = None,
        some_number_arg_required_no_default_no_env: float | None = None,
        required_arg_no_env: str | None = None,
        required_arg_no_env_with_default: str | None = None,
        client_path_param: str | None = None,
        camel_case_path: str | None = None,
        client_query_param: str | None = None,
        client_path_or_query_param: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            user_token=user_token or self.user_token,
            username=username or self.username,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            some_boolean_arg=some_boolean_arg or self.some_boolean_arg,
            some_integer_arg=some_integer_arg or self.some_integer_arg,
            some_number_arg=some_number_arg or self.some_number_arg,
            some_number_arg_required=some_number_arg_required or self.some_number_arg_required,
            some_number_arg_required_no_default=some_number_arg_required_no_default
            or self.some_number_arg_required_no_default,
            some_number_arg_required_no_default_no_env=some_number_arg_required_no_default_no_env
            or self.some_number_arg_required_no_default_no_env,
            required_arg_no_env=required_arg_no_env or self.required_arg_no_env,
            required_arg_no_env_with_default=required_arg_no_env_with_default or self.required_arg_no_env_with_default,
            client_path_param=client_path_param or self.client_path_param,
            camel_case_path=camel_case_path or self.camel_case_path,
            client_query_param=client_query_param or self.client_query_param,
            client_path_or_query_param=client_path_or_query_param or self.client_path_or_query_param,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def api_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIStatus:
        """API status check"""
        return self.get(
            "/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIStatus,
        )

    api_status_alias = api_status

    def create_no_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Endpoint returning no response"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self.post(
            "/no_response",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def get_auth_url(
        self,
        *,
        print_data: bool,
        redirect_uri: str,
        client_id: str,
    ) -> str:
        """A top level custom method on the sink customer."""
        if print_data:
            # used to test imports
            print(json.dumps("foo"))  # noqa: T201

        return str(
            httpx.URL(
                "http://localhost:8000/auth",
                params={
                    "client_id": client_id,
                    "redirect_uri": redirect_uri,
                },
            )
        )

    def _get_client_path_param_path_param(self) -> str:
        from_client = self.client_path_param
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing client_path_param argument; Please provide it at the client level, e.g. Sink(client_path_param='abcd') or per method."
        )

    def _get_camel_case_path_path_param(self) -> str:
        from_client = self.camel_case_path
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing camel_case_path argument; Please provide it at the client level, e.g. Sink(camel_case_path='abcd') or per method."
        )

    def _get_client_path_or_query_param_path_param(self) -> str:
        from_client = self.client_path_or_query_param
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing client_path_or_query_param argument; Please provide it at the client level, e.g. Sink(client_path_or_query_param='abcd') or per method."
        )

    def _get_client_query_param_query_param(self) -> str | None:
        return self.client_query_param

    def _get_client_path_or_query_param_query_param(self) -> str | None:
        return self.client_path_or_query_param

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSink(AsyncAPIClient):
    testing: _resources.AsyncTesting
    complex_queries: _resources.AsyncComplexQueries
    casing: _resources.AsyncCasing
    default_req_options: _resources.AsyncDefaultReqOptions
    tools: _resources.AsyncTools
    method_config: _resources.AsyncMethodConfig
    streaming: _resources.AsyncStreaming
    pagination_tests: _resources.AsyncPaginationTests
    docstrings: _resources.AsyncDocstrings
    invalid_schemas: _resources.AsyncInvalidSchemas
    resource_refs: _resources.AsyncResourceRefs
    cards: _resources.AsyncCards
    files: _resources.AsyncFiles
    binaries: _resources.AsyncBinaries
    resources: _resources.AsyncResources
    config_tools: _resources.AsyncConfigTools
    company: _resources.AsyncCompanyResource
    openapi_formats: _resources.AsyncOpenapiFormats
    parent: _resources.AsyncParent
    envelopes: _resources.AsyncEnvelopes
    types: _resources.AsyncTypes
    names: _resources.AsyncNames
    widgets: _resources.AsyncWidgets
    client_params: _resources.AsyncClientParams
    responses: _resources.AsyncResponses
    path_params: _resources.AsyncPathParams
    positional_params: _resources.AsyncPositionalParams
    empty_body: _resources.AsyncEmptyBody
    query_params: _resources.AsyncQueryParams
    body_params: _resources.AsyncBodyParams
    header_params: _resources.AsyncHeaderParams
    mixed_params: _resources.AsyncMixedParams
    make_ambiguous_schemas_looser: _resources.AsyncMakeAmbiguousSchemasLooser
    make_ambiguous_schemas_explicit: _resources.AsyncMakeAmbiguousSchemasExplicit
    decorator_tests: _resources.AsyncDecoratorTests
    tests: _resources.AsyncTests
    deeply_nested: _resources.AsyncDeeplyNested
    version_1_30_names: _resources.AsyncVersion1_30Names
    recursion: _resources.AsyncRecursion
    shared_query_params: _resources.AsyncSharedQueryParams
    model_referenced_in_parent_and_child: _resources.AsyncModelReferencedInParentAndChildResource
    only_custom_methods: _resources.AsyncOnlyCustomMethods
    with_raw_response: AsyncSinkWithRawResponse
    with_streaming_response: AsyncSinkWithStreamedResponse

    # client options
    user_token: str | None
    username: str
    client_id: str | None
    client_secret: str | None
    some_boolean_arg: bool | None
    some_integer_arg: int | None
    some_number_arg: float | None
    some_number_arg_required: float
    some_number_arg_required_no_default: float
    some_number_arg_required_no_default_no_env: float
    required_arg_no_env: str
    required_arg_no_env_with_default: str
    client_path_param: str | None
    camel_case_path: str | None
    client_query_param: str | None
    client_path_or_query_param: str | None

    # constants
    CONSTANT_WITH_NEWLINES = _constants.CONSTANT_WITH_NEWLINES

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        user_token: str | None = None,
        username: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        some_boolean_arg: bool | None = None,
        some_integer_arg: int | None = None,
        some_number_arg: float | None = None,
        some_number_arg_required: float | None = None,
        some_number_arg_required_no_default: float | None = None,
        some_number_arg_required_no_default_no_env: float,
        required_arg_no_env: str,
        required_arg_no_env_with_default: str | None = "hi!",
        client_path_param: str | None = None,
        camel_case_path: str | None = None,
        client_query_param: str | None = None,
        client_path_or_query_param: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async sink client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `user_token` from `SINK_CUSTOM_API_KEY_ENV`
        - `username` from `SINK_USER`
        - `client_id` from `SINK_CLIENT_ID`
        - `client_secret` from `SINK_CLIENT_SECRET`
        - `some_boolean_arg` from `SINK_SOME_BOOLEAN_ARG`
        - `some_integer_arg` from `SINK_SOME_INTEGER_ARG`
        - `some_number_arg` from `SINK_SOME_NUMBER_ARG`
        - `some_number_arg_required` from `SINK_SOME_NUMBER_ARG`
        - `some_number_arg_required_no_default` from `SINK_SOME_NUMBER_ARG`
        """
        if user_token is None:
            user_token = os.environ.get("SINK_CUSTOM_API_KEY_ENV")
        self.user_token = user_token

        if username is None:
            username = os.environ.get("SINK_USER")
        if username is None:
            raise SinkError(
                "The username client option must be set either by passing username to the client or by setting the SINK_USER environment variable"
            )
        self.username = username

        if client_id is None:
            client_id = os.environ.get("SINK_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("SINK_CLIENT_SECRET") or "hellosecret"
        self.client_secret = client_secret

        if some_boolean_arg is None:
            some_boolean_arg = maybe_coerce_boolean(os.environ.get("SINK_SOME_BOOLEAN_ARG")) or True
        self.some_boolean_arg = some_boolean_arg

        if some_integer_arg is None:
            some_integer_arg = maybe_coerce_integer(os.environ.get("SINK_SOME_INTEGER_ARG")) or 123
        self.some_integer_arg = some_integer_arg

        if some_number_arg is None:
            some_number_arg = maybe_coerce_float(os.environ.get("SINK_SOME_NUMBER_ARG")) or 1.2
        self.some_number_arg = some_number_arg

        if some_number_arg_required is None:
            some_number_arg_required = maybe_coerce_float(os.environ.get("SINK_SOME_NUMBER_ARG")) or 1.2
        self.some_number_arg_required = some_number_arg_required

        if some_number_arg_required_no_default is None:
            some_number_arg_required_no_default = maybe_coerce_float(os.environ.get("SINK_SOME_NUMBER_ARG"))
        if some_number_arg_required_no_default is None:
            raise SinkError(
                "The some_number_arg_required_no_default client option must be set either by passing some_number_arg_required_no_default to the client or by setting the SINK_SOME_NUMBER_ARG environment variable"
            )
        self.some_number_arg_required_no_default = some_number_arg_required_no_default

        self.some_number_arg_required_no_default_no_env = some_number_arg_required_no_default_no_env

        self.required_arg_no_env = required_arg_no_env

        if required_arg_no_env_with_default is None:
            required_arg_no_env_with_default = "hi!"
        self.required_arg_no_env_with_default = required_arg_no_env_with_default

        self.client_path_param = client_path_param

        self.camel_case_path = camel_case_path

        self.client_query_param = client_query_param

        self.client_path_or_query_param = client_path_or_query_param

        self._environment = environment

        base_url_env = os.environ.get("SINK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SINK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self._default_stream_cls = AsyncStream

        self.testing = _resources.AsyncTesting(self)
        self.complex_queries = _resources.AsyncComplexQueries(self)
        self.casing = _resources.AsyncCasing(self)
        self.default_req_options = _resources.AsyncDefaultReqOptions(self)
        self.tools = _resources.AsyncTools(self)
        self.method_config = _resources.AsyncMethodConfig(self)
        self.streaming = _resources.AsyncStreaming(self)
        self.pagination_tests = _resources.AsyncPaginationTests(self)
        self.docstrings = _resources.AsyncDocstrings(self)
        self.invalid_schemas = _resources.AsyncInvalidSchemas(self)
        self.resource_refs = _resources.AsyncResourceRefs(self)
        self.cards = _resources.AsyncCards(self)
        self.files = _resources.AsyncFiles(self)
        self.binaries = _resources.AsyncBinaries(self)
        self.resources = _resources.AsyncResources(self)
        self.config_tools = _resources.AsyncConfigTools(self)
        self.company = _resources.AsyncCompanyResource(self)
        self.openapi_formats = _resources.AsyncOpenapiFormats(self)
        self.parent = _resources.AsyncParent(self)
        self.envelopes = _resources.AsyncEnvelopes(self)
        self.types = _resources.AsyncTypes(self)
        self.names = _resources.AsyncNames(self)
        self.widgets = _resources.AsyncWidgets(self)
        self.client_params = _resources.AsyncClientParams(self)
        self.responses = _resources.AsyncResponses(self)
        self.path_params = _resources.AsyncPathParams(self)
        self.positional_params = _resources.AsyncPositionalParams(self)
        self.empty_body = _resources.AsyncEmptyBody(self)
        self.query_params = _resources.AsyncQueryParams(self)
        self.body_params = _resources.AsyncBodyParams(self)
        self.header_params = _resources.AsyncHeaderParams(self)
        self.mixed_params = _resources.AsyncMixedParams(self)
        self.make_ambiguous_schemas_looser = _resources.AsyncMakeAmbiguousSchemasLooser(self)
        self.make_ambiguous_schemas_explicit = _resources.AsyncMakeAmbiguousSchemasExplicit(self)
        self.decorator_tests = _resources.AsyncDecoratorTests(self)
        self.tests = _resources.AsyncTests(self)
        self.deeply_nested = _resources.AsyncDeeplyNested(self)
        self.version_1_30_names = _resources.AsyncVersion1_30Names(self)
        self.recursion = _resources.AsyncRecursion(self)
        self.shared_query_params = _resources.AsyncSharedQueryParams(self)
        self.model_referenced_in_parent_and_child = _resources.AsyncModelReferencedInParentAndChildResource(self)
        self.only_custom_methods = _resources.AsyncOnlyCustomMethods(self)
        self.with_raw_response = AsyncSinkWithRawResponse(self)
        self.with_streaming_response = AsyncSinkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        user_token = self.user_token
        if user_token is None:
            return {}
        return {"Authorization": f"Bearer {user_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "My-Api-Version": "11",
            "X-Enable-Metrics": "1",
            "X-Client-UserName": self.username,
            "X-Client-Secret": self.client_secret if self.client_secret is not None else Omit(),
            "X-Integer": str(self.some_integer_arg) if self.some_integer_arg is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.user_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the user_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        user_token: str | None = None,
        username: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        some_boolean_arg: bool | None = None,
        some_integer_arg: int | None = None,
        some_number_arg: float | None = None,
        some_number_arg_required: float | None = None,
        some_number_arg_required_no_default: float | None = None,
        some_number_arg_required_no_default_no_env: float | None = None,
        required_arg_no_env: str | None = None,
        required_arg_no_env_with_default: str | None = None,
        client_path_param: str | None = None,
        camel_case_path: str | None = None,
        client_query_param: str | None = None,
        client_path_or_query_param: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            user_token=user_token or self.user_token,
            username=username or self.username,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            some_boolean_arg=some_boolean_arg or self.some_boolean_arg,
            some_integer_arg=some_integer_arg or self.some_integer_arg,
            some_number_arg=some_number_arg or self.some_number_arg,
            some_number_arg_required=some_number_arg_required or self.some_number_arg_required,
            some_number_arg_required_no_default=some_number_arg_required_no_default
            or self.some_number_arg_required_no_default,
            some_number_arg_required_no_default_no_env=some_number_arg_required_no_default_no_env
            or self.some_number_arg_required_no_default_no_env,
            required_arg_no_env=required_arg_no_env or self.required_arg_no_env,
            required_arg_no_env_with_default=required_arg_no_env_with_default or self.required_arg_no_env_with_default,
            client_path_param=client_path_param or self.client_path_param,
            camel_case_path=camel_case_path or self.camel_case_path,
            client_query_param=client_query_param or self.client_query_param,
            client_path_or_query_param=client_path_or_query_param or self.client_path_or_query_param,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def api_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIStatus:
        """API status check"""
        return await self.get(
            "/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIStatus,
        )

    api_status_alias = api_status

    async def create_no_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Endpoint returning no response"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self.post(
            "/no_response",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def get_auth_url(
        self,
        *,
        print_data: bool,
        redirect_uri: str,
        client_id: str,
    ) -> str:
        """A top level custom method on the sink customer."""
        if print_data:
            # used to test imports
            print(json.dumps("foo"))  # noqa: T201

        return str(
            httpx.URL(
                "http://localhost:8000/auth",
                params={
                    "client_id": client_id,
                    "redirect_uri": redirect_uri,
                },
            )
        )

    def _get_client_path_param_path_param(self) -> str:
        from_client = self.client_path_param
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing client_path_param argument; Please provide it at the client level, e.g. AsyncSink(client_path_param='abcd') or per method."
        )

    def _get_camel_case_path_path_param(self) -> str:
        from_client = self.camel_case_path
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing camel_case_path argument; Please provide it at the client level, e.g. AsyncSink(camel_case_path='abcd') or per method."
        )

    def _get_client_path_or_query_param_path_param(self) -> str:
        from_client = self.client_path_or_query_param
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing client_path_or_query_param argument; Please provide it at the client level, e.g. AsyncSink(client_path_or_query_param='abcd') or per method."
        )

    def _get_client_query_param_query_param(self) -> str | None:
        return self.client_query_param

    def _get_client_path_or_query_param_query_param(self) -> str | None:
        return self.client_path_or_query_param

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SinkWithRawResponse:
    def __init__(self, client: Sink) -> None:
        self.testing = _resources.TestingWithRawResponse(client.testing)
        self.complex_queries = _resources.ComplexQueriesWithRawResponse(client.complex_queries)
        self.casing = _resources.CasingWithRawResponse(client.casing)
        self.default_req_options = _resources.DefaultReqOptionsWithRawResponse(client.default_req_options)
        self.tools = _resources.ToolsWithRawResponse(client.tools)
        self.method_config = _resources.MethodConfigWithRawResponse(client.method_config)
        self.streaming = _resources.StreamingWithRawResponse(client.streaming)
        self.pagination_tests = _resources.PaginationTestsWithRawResponse(client.pagination_tests)
        self.docstrings = _resources.DocstringsWithRawResponse(client.docstrings)
        self.invalid_schemas = _resources.InvalidSchemasWithRawResponse(client.invalid_schemas)
        self.resource_refs = _resources.ResourceRefsWithRawResponse(client.resource_refs)
        self.cards = _resources.CardsWithRawResponse(client.cards)
        self.files = _resources.FilesWithRawResponse(client.files)
        self.binaries = _resources.BinariesWithRawResponse(client.binaries)
        self.resources = _resources.ResourcesWithRawResponse(client.resources)
        self.config_tools = _resources.ConfigToolsWithRawResponse(client.config_tools)
        self.company = _resources.CompanyResourceWithRawResponse(client.company)
        self.openapi_formats = _resources.OpenapiFormatsWithRawResponse(client.openapi_formats)
        self.parent = _resources.ParentWithRawResponse(client.parent)
        self.envelopes = _resources.EnvelopesWithRawResponse(client.envelopes)
        self.types = _resources.TypesWithRawResponse(client.types)
        self.names = _resources.NamesWithRawResponse(client.names)
        self.widgets = _resources.WidgetsWithRawResponse(client.widgets)
        self.client_params = _resources.ClientParamsWithRawResponse(client.client_params)
        self.responses = _resources.ResponsesWithRawResponse(client.responses)
        self.path_params = _resources.PathParamsWithRawResponse(client.path_params)
        self.positional_params = _resources.PositionalParamsWithRawResponse(client.positional_params)
        self.empty_body = _resources.EmptyBodyWithRawResponse(client.empty_body)
        self.query_params = _resources.QueryParamsWithRawResponse(client.query_params)
        self.body_params = _resources.BodyParamsWithRawResponse(client.body_params)
        self.header_params = _resources.HeaderParamsWithRawResponse(client.header_params)
        self.mixed_params = _resources.MixedParamsWithRawResponse(client.mixed_params)
        self.make_ambiguous_schemas_looser = _resources.MakeAmbiguousSchemasLooserWithRawResponse(
            client.make_ambiguous_schemas_looser
        )
        self.make_ambiguous_schemas_explicit = _resources.MakeAmbiguousSchemasExplicitWithRawResponse(
            client.make_ambiguous_schemas_explicit
        )
        self.decorator_tests = _resources.DecoratorTestsWithRawResponse(client.decorator_tests)
        self.tests = _resources.TestsWithRawResponse(client.tests)
        self.deeply_nested = _resources.DeeplyNestedWithRawResponse(client.deeply_nested)
        self.version_1_30_names = _resources.Version1_30NamesWithRawResponse(client.version_1_30_names)
        self.recursion = _resources.RecursionWithRawResponse(client.recursion)
        self.shared_query_params = _resources.SharedQueryParamsWithRawResponse(client.shared_query_params)
        self.model_referenced_in_parent_and_child = _resources.ModelReferencedInParentAndChildResourceWithRawResponse(
            client.model_referenced_in_parent_and_child
        )

        self.api_status = to_raw_response_wrapper(
            client.api_status,
        )
        self.api_status_alias = to_raw_response_wrapper(
            client.api_status_alias,
        )
        self.create_no_response = to_raw_response_wrapper(
            client.create_no_response,
        )


class AsyncSinkWithRawResponse:
    def __init__(self, client: AsyncSink) -> None:
        self.testing = _resources.AsyncTestingWithRawResponse(client.testing)
        self.complex_queries = _resources.AsyncComplexQueriesWithRawResponse(client.complex_queries)
        self.casing = _resources.AsyncCasingWithRawResponse(client.casing)
        self.default_req_options = _resources.AsyncDefaultReqOptionsWithRawResponse(client.default_req_options)
        self.tools = _resources.AsyncToolsWithRawResponse(client.tools)
        self.method_config = _resources.AsyncMethodConfigWithRawResponse(client.method_config)
        self.streaming = _resources.AsyncStreamingWithRawResponse(client.streaming)
        self.pagination_tests = _resources.AsyncPaginationTestsWithRawResponse(client.pagination_tests)
        self.docstrings = _resources.AsyncDocstringsWithRawResponse(client.docstrings)
        self.invalid_schemas = _resources.AsyncInvalidSchemasWithRawResponse(client.invalid_schemas)
        self.resource_refs = _resources.AsyncResourceRefsWithRawResponse(client.resource_refs)
        self.cards = _resources.AsyncCardsWithRawResponse(client.cards)
        self.files = _resources.AsyncFilesWithRawResponse(client.files)
        self.binaries = _resources.AsyncBinariesWithRawResponse(client.binaries)
        self.resources = _resources.AsyncResourcesWithRawResponse(client.resources)
        self.config_tools = _resources.AsyncConfigToolsWithRawResponse(client.config_tools)
        self.company = _resources.AsyncCompanyResourceWithRawResponse(client.company)
        self.openapi_formats = _resources.AsyncOpenapiFormatsWithRawResponse(client.openapi_formats)
        self.parent = _resources.AsyncParentWithRawResponse(client.parent)
        self.envelopes = _resources.AsyncEnvelopesWithRawResponse(client.envelopes)
        self.types = _resources.AsyncTypesWithRawResponse(client.types)
        self.names = _resources.AsyncNamesWithRawResponse(client.names)
        self.widgets = _resources.AsyncWidgetsWithRawResponse(client.widgets)
        self.client_params = _resources.AsyncClientParamsWithRawResponse(client.client_params)
        self.responses = _resources.AsyncResponsesWithRawResponse(client.responses)
        self.path_params = _resources.AsyncPathParamsWithRawResponse(client.path_params)
        self.positional_params = _resources.AsyncPositionalParamsWithRawResponse(client.positional_params)
        self.empty_body = _resources.AsyncEmptyBodyWithRawResponse(client.empty_body)
        self.query_params = _resources.AsyncQueryParamsWithRawResponse(client.query_params)
        self.body_params = _resources.AsyncBodyParamsWithRawResponse(client.body_params)
        self.header_params = _resources.AsyncHeaderParamsWithRawResponse(client.header_params)
        self.mixed_params = _resources.AsyncMixedParamsWithRawResponse(client.mixed_params)
        self.make_ambiguous_schemas_looser = _resources.AsyncMakeAmbiguousSchemasLooserWithRawResponse(
            client.make_ambiguous_schemas_looser
        )
        self.make_ambiguous_schemas_explicit = _resources.AsyncMakeAmbiguousSchemasExplicitWithRawResponse(
            client.make_ambiguous_schemas_explicit
        )
        self.decorator_tests = _resources.AsyncDecoratorTestsWithRawResponse(client.decorator_tests)
        self.tests = _resources.AsyncTestsWithRawResponse(client.tests)
        self.deeply_nested = _resources.AsyncDeeplyNestedWithRawResponse(client.deeply_nested)
        self.version_1_30_names = _resources.AsyncVersion1_30NamesWithRawResponse(client.version_1_30_names)
        self.recursion = _resources.AsyncRecursionWithRawResponse(client.recursion)
        self.shared_query_params = _resources.AsyncSharedQueryParamsWithRawResponse(client.shared_query_params)
        self.model_referenced_in_parent_and_child = (
            _resources.AsyncModelReferencedInParentAndChildResourceWithRawResponse(
                client.model_referenced_in_parent_and_child
            )
        )

        self.api_status = async_to_raw_response_wrapper(
            client.api_status,
        )
        self.api_status_alias = async_to_raw_response_wrapper(
            client.api_status_alias,
        )
        self.create_no_response = async_to_raw_response_wrapper(
            client.create_no_response,
        )


class SinkWithStreamedResponse:
    def __init__(self, client: Sink) -> None:
        self.testing = _resources.TestingWithStreamingResponse(client.testing)
        self.complex_queries = _resources.ComplexQueriesWithStreamingResponse(client.complex_queries)
        self.casing = _resources.CasingWithStreamingResponse(client.casing)
        self.default_req_options = _resources.DefaultReqOptionsWithStreamingResponse(client.default_req_options)
        self.tools = _resources.ToolsWithStreamingResponse(client.tools)
        self.method_config = _resources.MethodConfigWithStreamingResponse(client.method_config)
        self.streaming = _resources.StreamingWithStreamingResponse(client.streaming)
        self.pagination_tests = _resources.PaginationTestsWithStreamingResponse(client.pagination_tests)
        self.docstrings = _resources.DocstringsWithStreamingResponse(client.docstrings)
        self.invalid_schemas = _resources.InvalidSchemasWithStreamingResponse(client.invalid_schemas)
        self.resource_refs = _resources.ResourceRefsWithStreamingResponse(client.resource_refs)
        self.cards = _resources.CardsWithStreamingResponse(client.cards)
        self.files = _resources.FilesWithStreamingResponse(client.files)
        self.binaries = _resources.BinariesWithStreamingResponse(client.binaries)
        self.resources = _resources.ResourcesWithStreamingResponse(client.resources)
        self.config_tools = _resources.ConfigToolsWithStreamingResponse(client.config_tools)
        self.company = _resources.CompanyResourceWithStreamingResponse(client.company)
        self.openapi_formats = _resources.OpenapiFormatsWithStreamingResponse(client.openapi_formats)
        self.parent = _resources.ParentWithStreamingResponse(client.parent)
        self.envelopes = _resources.EnvelopesWithStreamingResponse(client.envelopes)
        self.types = _resources.TypesWithStreamingResponse(client.types)
        self.names = _resources.NamesWithStreamingResponse(client.names)
        self.widgets = _resources.WidgetsWithStreamingResponse(client.widgets)
        self.client_params = _resources.ClientParamsWithStreamingResponse(client.client_params)
        self.responses = _resources.ResponsesWithStreamingResponse(client.responses)
        self.path_params = _resources.PathParamsWithStreamingResponse(client.path_params)
        self.positional_params = _resources.PositionalParamsWithStreamingResponse(client.positional_params)
        self.empty_body = _resources.EmptyBodyWithStreamingResponse(client.empty_body)
        self.query_params = _resources.QueryParamsWithStreamingResponse(client.query_params)
        self.body_params = _resources.BodyParamsWithStreamingResponse(client.body_params)
        self.header_params = _resources.HeaderParamsWithStreamingResponse(client.header_params)
        self.mixed_params = _resources.MixedParamsWithStreamingResponse(client.mixed_params)
        self.make_ambiguous_schemas_looser = _resources.MakeAmbiguousSchemasLooserWithStreamingResponse(
            client.make_ambiguous_schemas_looser
        )
        self.make_ambiguous_schemas_explicit = _resources.MakeAmbiguousSchemasExplicitWithStreamingResponse(
            client.make_ambiguous_schemas_explicit
        )
        self.decorator_tests = _resources.DecoratorTestsWithStreamingResponse(client.decorator_tests)
        self.tests = _resources.TestsWithStreamingResponse(client.tests)
        self.deeply_nested = _resources.DeeplyNestedWithStreamingResponse(client.deeply_nested)
        self.version_1_30_names = _resources.Version1_30NamesWithStreamingResponse(client.version_1_30_names)
        self.recursion = _resources.RecursionWithStreamingResponse(client.recursion)
        self.shared_query_params = _resources.SharedQueryParamsWithStreamingResponse(client.shared_query_params)
        self.model_referenced_in_parent_and_child = (
            _resources.ModelReferencedInParentAndChildResourceWithStreamingResponse(
                client.model_referenced_in_parent_and_child
            )
        )

        self.api_status = to_streamed_response_wrapper(
            client.api_status,
        )
        self.api_status_alias = to_streamed_response_wrapper(
            client.api_status_alias,
        )
        self.create_no_response = to_streamed_response_wrapper(
            client.create_no_response,
        )


class AsyncSinkWithStreamedResponse:
    def __init__(self, client: AsyncSink) -> None:
        self.testing = _resources.AsyncTestingWithStreamingResponse(client.testing)
        self.complex_queries = _resources.AsyncComplexQueriesWithStreamingResponse(client.complex_queries)
        self.casing = _resources.AsyncCasingWithStreamingResponse(client.casing)
        self.default_req_options = _resources.AsyncDefaultReqOptionsWithStreamingResponse(client.default_req_options)
        self.tools = _resources.AsyncToolsWithStreamingResponse(client.tools)
        self.method_config = _resources.AsyncMethodConfigWithStreamingResponse(client.method_config)
        self.streaming = _resources.AsyncStreamingWithStreamingResponse(client.streaming)
        self.pagination_tests = _resources.AsyncPaginationTestsWithStreamingResponse(client.pagination_tests)
        self.docstrings = _resources.AsyncDocstringsWithStreamingResponse(client.docstrings)
        self.invalid_schemas = _resources.AsyncInvalidSchemasWithStreamingResponse(client.invalid_schemas)
        self.resource_refs = _resources.AsyncResourceRefsWithStreamingResponse(client.resource_refs)
        self.cards = _resources.AsyncCardsWithStreamingResponse(client.cards)
        self.files = _resources.AsyncFilesWithStreamingResponse(client.files)
        self.binaries = _resources.AsyncBinariesWithStreamingResponse(client.binaries)
        self.resources = _resources.AsyncResourcesWithStreamingResponse(client.resources)
        self.config_tools = _resources.AsyncConfigToolsWithStreamingResponse(client.config_tools)
        self.company = _resources.AsyncCompanyResourceWithStreamingResponse(client.company)
        self.openapi_formats = _resources.AsyncOpenapiFormatsWithStreamingResponse(client.openapi_formats)
        self.parent = _resources.AsyncParentWithStreamingResponse(client.parent)
        self.envelopes = _resources.AsyncEnvelopesWithStreamingResponse(client.envelopes)
        self.types = _resources.AsyncTypesWithStreamingResponse(client.types)
        self.names = _resources.AsyncNamesWithStreamingResponse(client.names)
        self.widgets = _resources.AsyncWidgetsWithStreamingResponse(client.widgets)
        self.client_params = _resources.AsyncClientParamsWithStreamingResponse(client.client_params)
        self.responses = _resources.AsyncResponsesWithStreamingResponse(client.responses)
        self.path_params = _resources.AsyncPathParamsWithStreamingResponse(client.path_params)
        self.positional_params = _resources.AsyncPositionalParamsWithStreamingResponse(client.positional_params)
        self.empty_body = _resources.AsyncEmptyBodyWithStreamingResponse(client.empty_body)
        self.query_params = _resources.AsyncQueryParamsWithStreamingResponse(client.query_params)
        self.body_params = _resources.AsyncBodyParamsWithStreamingResponse(client.body_params)
        self.header_params = _resources.AsyncHeaderParamsWithStreamingResponse(client.header_params)
        self.mixed_params = _resources.AsyncMixedParamsWithStreamingResponse(client.mixed_params)
        self.make_ambiguous_schemas_looser = _resources.AsyncMakeAmbiguousSchemasLooserWithStreamingResponse(
            client.make_ambiguous_schemas_looser
        )
        self.make_ambiguous_schemas_explicit = _resources.AsyncMakeAmbiguousSchemasExplicitWithStreamingResponse(
            client.make_ambiguous_schemas_explicit
        )
        self.decorator_tests = _resources.AsyncDecoratorTestsWithStreamingResponse(client.decorator_tests)
        self.tests = _resources.AsyncTestsWithStreamingResponse(client.tests)
        self.deeply_nested = _resources.AsyncDeeplyNestedWithStreamingResponse(client.deeply_nested)
        self.version_1_30_names = _resources.AsyncVersion1_30NamesWithStreamingResponse(client.version_1_30_names)
        self.recursion = _resources.AsyncRecursionWithStreamingResponse(client.recursion)
        self.shared_query_params = _resources.AsyncSharedQueryParamsWithStreamingResponse(client.shared_query_params)
        self.model_referenced_in_parent_and_child = (
            _resources.AsyncModelReferencedInParentAndChildResourceWithStreamingResponse(
                client.model_referenced_in_parent_and_child
            )
        )

        self.api_status = async_to_streamed_response_wrapper(
            client.api_status,
        )
        self.api_status_alias = async_to_streamed_response_wrapper(
            client.api_status_alias,
        )
        self.create_no_response = async_to_streamed_response_wrapper(
            client.create_no_response,
        )


Client = Sink

AsyncClient = AsyncSink
