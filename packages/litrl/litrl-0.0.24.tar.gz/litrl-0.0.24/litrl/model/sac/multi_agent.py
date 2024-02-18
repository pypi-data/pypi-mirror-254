from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import numpy as np
import numpy.typing as npt
import onnxruntime
import scipy
from huggingface_hub import hf_hub_download

from litrl.common.agent import Agent
from litrl.common.observation import process_obs
from litrl.env.typing import MultiAgentEnv
from litrl.model.sac.model import ActionType as SacActionType
from litrl.model.sac.model import Actor

SacMultiAgentEnv = MultiAgentEnv[Any, SacActionType, Any]


class SacMultiAgent(Agent[SacMultiAgentEnv, SacActionType], ABC):
    def __init__(self, actor: Actor) -> None:
        super().__init__()
        self._actor = actor

    def update(self, actor: Actor) -> None:
        self._actor = actor

    @abstractmethod
    def get_action(self, env: SacMultiAgentEnv) -> SacActionType:
        raise NotImplementedError


class SacStochasticAgent(SacMultiAgent):
    def get_action(self, env: SacMultiAgentEnv) -> SacActionType:
        obs = env.observe(env.unwrapped.agent_selection)
        return np.int64(
            self._actor.get_action(
                process_obs(obs["observation"]),
                obs["action_mask"],
            ),
        )


class OnnxSacMultiAgent(SacMultiAgent, ABC):
    def __init__(self, onnx_path: Path | None = None) -> None:
        if onnx_path is None:
            onnx_path = Path(
                hf_hub_download(repo_id="c-gohlke/connect4SAC", filename="model.onnx"),
            )
        self.onnx_model = onnxruntime.InferenceSession(onnx_path)

    def get_logits(self, env: SacMultiAgentEnv) -> npt.NDArray[np.float64]:
        obs = env.observe(env.unwrapped.agent_selection)
        processed_obs = np.expand_dims(obs["observation"].flatten(), axis=0).astype(
            np.float32,
        )
        onnx_inputs = {self.onnx_model.get_inputs()[0].name: processed_obs}
        logits = np.array(self.onnx_model.run(None, onnx_inputs)).flatten()
        logits[~obs["action_mask"].astype(bool)] = -1e5
        return logits

    @abstractmethod
    def get_action(self, env: SacMultiAgentEnv) -> SacActionType:
        raise NotImplementedError


class OnnxSacDeterministicMultiAgent(OnnxSacMultiAgent):
    def get_action(self, env: SacMultiAgentEnv) -> SacActionType:
        logits = self.get_logits(env)
        return np.argmax(logits)


class OnnxSacStochasticMultiAgent(OnnxSacMultiAgent):
    def get_action(self, env: SacMultiAgentEnv) -> SacActionType:
        logits = self.get_logits(env)
        probabilities = scipy.special.softmax(logits, axis=-1)
        action = self._np_random.choice(len(probabilities), p=probabilities)
        return np.int64(action)
