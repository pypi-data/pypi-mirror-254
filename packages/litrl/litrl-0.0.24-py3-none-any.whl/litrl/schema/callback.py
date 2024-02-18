from lightning.pytorch.callbacks import Callback as LightningCallback
from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.schema.instantiator import InstantiatorClass


@pydantic_dataclass(frozen=True)
class CallbackSchema(InstantiatorClass[LightningCallback]):
    _target_: str
