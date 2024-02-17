from __future__ import annotations

from typing import List

from lightning import Trainer
from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.schema.callback import CallbackSchema  # noqa: TCH001
from litrl.schema.instantiator import InstantiatorClass
from litrl.schema.logger import LoggerSchema  # noqa: TCH001


@pydantic_dataclass(frozen=True)
class TrainerSchema(InstantiatorClass[Trainer]):
    _target_: str
    log_every_n_steps: int
    limit_train_batches: int
    max_epochs: int
    num_sanity_val_steps: int
    logger: LoggerSchema
    callbacks: List[CallbackSchema]  # noqa: UP006
