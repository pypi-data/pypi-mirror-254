from typing import Any

import numpy.typing as npt
import torch


def process_obs(obs: npt.NDArray[Any]) -> torch.Tensor:
    return torch.tensor(obs.flatten(), dtype=torch.float32).unsqueeze(0)  # type: ignore[no-any-return]
