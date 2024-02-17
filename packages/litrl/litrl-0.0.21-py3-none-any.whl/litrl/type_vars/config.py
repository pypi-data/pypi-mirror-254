from typing import Any, TypeVar

from litrl.schema.model import ModelConfigSchema

ModelConfigSchemaType = TypeVar("ModelConfigSchemaType", bound=ModelConfigSchema[Any])
