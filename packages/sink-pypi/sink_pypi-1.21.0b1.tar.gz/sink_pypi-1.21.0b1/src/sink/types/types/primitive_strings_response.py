# File generated from our OpenAPI spec by Stainless.



from ..._models import BaseModel
from .model_string import ModelString

__all__ = ["PrimitiveStringsResponse"]


class PrimitiveStringsResponse(BaseModel):
    string_prop: ModelString
