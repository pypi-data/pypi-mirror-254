from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic

import numpy as np

from litrl.env.type_vars import EnvType
from litrl.env.typing import ActType, AgentID, MaskedObs, MaskShape, MultiAgentEnv, ObsShape, SingleAgentEnv


class Agent(ABC, Generic[EnvType, ActType]):
    def __init__(self, np_random: np.random.Generator | None = None) -> None:
        self._np_random = np_random if np_random is not None else np.random.default_rng()

    def seed(self, seed: int | None = None) -> None:
        self._np_random = np.random.default_rng(seed=seed)

    @abstractmethod
    def get_action(self, env: EnvType) -> ActType:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.__class__.__name__


class RandomAgent(
    Agent[SingleAgentEnv[ObsShape, ActType], ActType],
    Generic[ObsShape, ActType],
):
    def get_action(
        self,
        env: SingleAgentEnv[ObsShape, ActType],
    ) -> ActType:
        return env.action_space.sample()


class RandomMultiAgent(
    Agent[MultiAgentEnv[MaskedObs[ObsShape, MaskShape], ActType, AgentID], ActType],
    Generic[ActType, ObsShape, MaskShape, AgentID],
):
    def get_action(
        self,
        env: MultiAgentEnv[MaskedObs[ObsShape, MaskShape], ActType, AgentID],
    ) -> ActType:
        obs = env.observe(env.unwrapped.agent_selection)
        valid_actions = obs["action_mask"] == 1
        return self._np_random.choice(np.where(valid_actions)[0])  # type: ignore[no-any-return]
