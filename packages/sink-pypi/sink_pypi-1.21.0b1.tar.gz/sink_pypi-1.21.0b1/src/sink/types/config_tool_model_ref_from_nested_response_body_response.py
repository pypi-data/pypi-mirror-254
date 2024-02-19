# File generated from our OpenAPI spec by Stainless.



from .._models import BaseModel
from .model_from_nested_response_body_ref import ModelFromNestedResponseBodyRef

__all__ = ["ConfigToolModelRefFromNestedResponseBodyResponse", "Foo"]


class Foo(BaseModel):
    bar: ModelFromNestedResponseBodyRef


class ConfigToolModelRefFromNestedResponseBodyResponse(BaseModel):
    foo: Foo
