from abc import ABC
from typing import TYPE_CHECKING, Any, Generic, Literal

from lightning import LightningModule

from litrl.type_vars.config import ModelConfigSchemaType

if TYPE_CHECKING:
    import torch
    from torchrl.data.replay_buffers.replay_buffers import TensorDictReplayBuffer
ModelId = Literal["sac", "rainbow"]


class LitRLModule(LightningModule, ABC, Generic[ModelConfigSchemaType]):
    default_config: "ModelConfigSchemaType"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.buffer: "TensorDictReplayBuffer"
        self.obs: "torch.Tensor"
        self.cfg: "ModelConfigSchemaType"
