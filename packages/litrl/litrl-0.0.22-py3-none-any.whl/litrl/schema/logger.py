from __future__ import annotations

from typing import Dict

from lightning.pytorch.loggers import Logger as LightningLogger
from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.schema.instantiator import InstantiatorClass


@pydantic_dataclass(frozen=True)
class LoggerSchema(InstantiatorClass[LightningLogger]):
    _target_: str
    log_model: bool
    tags: Dict[str, str]  # noqa: UP006
    run_id: str
    save_dir: str = "./temp/mlruns"
