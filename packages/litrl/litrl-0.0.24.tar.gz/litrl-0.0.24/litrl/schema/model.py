from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Type

if TYPE_CHECKING:
    import sys

    if sys.version_info[:2] >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self

from pydantic import field_validator
from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.env.type_vars import EnvType
from litrl.schema.env import EnvSchema  # noqa: TCH001


@pydantic_dataclass(frozen=True)
class BufferSchema:
    batch_size: int
    max_size: int


@pydantic_dataclass(frozen=True)
class ModelConfigSchema(Generic[EnvType]):
    seed: int
    lr: float
    gamma: float
    warm_start_steps: int
    hidden_size: int
    n_hidden_layers: int
    buffer: BufferSchema
    epsilon: float
    target_entropy: float
    tau: float
    env_fabric: EnvSchema[EnvType]
    val_env_fabric: EnvSchema[EnvType]

    @field_validator("lr")
    @classmethod
    def validate_lr(cls: Type[Self], lr: float) -> float:  # noqa: UP006
        if lr < 0:
            msg = f"'lr' can't be less than 0, got: {lr}"
            raise ValueError(msg)
        return lr
