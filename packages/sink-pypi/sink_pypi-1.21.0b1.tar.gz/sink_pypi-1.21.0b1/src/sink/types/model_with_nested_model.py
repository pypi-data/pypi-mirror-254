# File generated from our OpenAPI spec by Stainless.



from .._models import BaseModel
from .model_from_nested_path import ModelFromNestedPath

__all__ = ["ModelWithNestedModel"]


class ModelWithNestedModel(BaseModel):
    email: str
    """Someone's email address."""

    preferences: ModelFromNestedPath
