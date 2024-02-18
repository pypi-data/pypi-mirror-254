from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Dict, Generic, Literal, Optional

from pydantic import field_validator
from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.env.type_vars import EnvType
from litrl.model.base_module import LitRLModule
from litrl.schema.instantiator import InstantiatorClass
from litrl.schema.model import ModelConfigSchema
from litrl.schema.trainer import TrainerSchema  # noqa: TCH001

if TYPE_CHECKING:
    import sys

    if sys.version_info[:2] >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


@pydantic_dataclass(frozen=True)
class ModelSchema(
    InstantiatorClass[LitRLModule[ModelConfigSchema[EnvType]]],
    Generic[EnvType],
):
    _target_: str
    cfg: ModelConfigSchema[EnvType]
    _recursive_: Literal[False] = False


@pydantic_dataclass
class ConfigSchema(Generic[EnvType]):
    model: ModelSchema[EnvType]
    trainer: TrainerSchema
    tags: Dict[str, str]  # noqa: UP006
    load_path: Optional[str]  # noqa: UP007
    run_id: str
    _recursive_: Literal[False] = False

    @field_validator("load_path")
    @classmethod
    def ensure_exists(cls: type[Self], load_path: str | None = None) -> str | None:
        if not (load_path is None or load_path == "latest" or Path(load_path).exists()):
            msg: str = f"Path {load_path} does not exist"
            raise ValueError(msg)
        return load_path
