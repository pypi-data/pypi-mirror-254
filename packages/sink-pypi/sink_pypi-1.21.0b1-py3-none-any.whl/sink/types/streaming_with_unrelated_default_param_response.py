# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["StreamingWithUnrelatedDefaultParamResponse"]


class StreamingWithUnrelatedDefaultParamResponse(BaseModel):
    completion: str

    model: Optional[str] = None
