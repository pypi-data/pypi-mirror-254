from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar, Union

import numpy as np
from pettingzoo.utils.wrappers import BaseWrapper

from litrl.common.agent import Agent, RandomMultiAgent
from litrl.env.typing import ActType, MaskedInfo, MultiAgentEnv, ObsType

if TYPE_CHECKING:
    from gymnasium.spaces import Space
AgentID = str
AgentType = TypeVar(
    "AgentType",
    bound=Union[Agent[Any, Any], RandomMultiAgent[Any, Any, Any, Any]],
)


class StaticOpponentWrapper(
    BaseWrapper[AgentID, ObsType, ActType],  # type: ignore[misc]
    Generic[ObsType, ActType, AgentType],
):
    """Used to use MultiAgent environments (e.g. connect4) with the same API as farama's gym."""

    def __init__(
        self,
        env: MultiAgentEnv[Any, Any, AgentID],
        opponent: AgentType | None = None,
    ) -> None:
        super().__init__(env=env)
        self._opponent: AgentType = opponent if opponent is not None else RandomMultiAgent()
        self._agent_started: bool
        self._np_random: np.random.Generator

    def get_wrapper_attr(self, name: str) -> Any:
        """Gymnasium wrappers and pettingzoo wrappers have different APIs, this serves as an adapter."""
        if name in self.__dir__():
            return getattr(self, name)
        try:
            return self.env.get_wrapper_attr(name)
        except AttributeError as e:
            message = f"wrapper {self.class_name()} has no attribute {name!r}"
            raise AttributeError(message) from e

    @property
    def opponent(self) -> AgentType:
        return self._opponent

    def set_opponent(self, opponent: AgentType) -> None:
        """Not a property setter for opponent because gymnasium wrappers create problems."""
        self._opponent = opponent

    @property
    def _opponent_name(self) -> str:
        return "player_1" if self._agent_started else "player_0"

    @property
    def _agent_name(self) -> str:
        return "player_0" if self._agent_started else "player_1"

    @property
    def action_space(self) -> Space[ActType]:
        return self.env.action_space(self._agent_name)  # type: ignore[no-any-return]

    @property
    def observation_space(self) -> Space[ObsType]:
        return self.env.observation_space(self._agent_name)["observation"]  # type: ignore[no-any-return]

    def step(
        self,
        action: ActType,
    ) -> tuple[ObsType, float, bool, bool, MaskedInfo[Any]]:
        super().step(action)
        terminated = self.terminations[self._agent_name]
        truncated = self.truncations[self._agent_name]
        if not (terminated or truncated):
            self._opponent_step()
            terminated = terminated or self.terminations[self._opponent_name]
            truncated = truncated or self.truncations[self._opponent_name]
        info = self.infos[self.agent_selection]
        observation = self.observe(self._agent_name)
        info["action_mask"] = observation["action_mask"]
        return (
            observation["observation"],
            self._cumulative_rewards[self._agent_name],
            terminated,
            truncated,
            info,
        )

    def _opponent_step(self) -> None:
        action = self._opponent.get_action(self.unwrapped)
        super().step(action)
        if self.render_mode is not None:
            self.render()

    def reset(
        self,
        seed: int | None = None,
        options: dict[Any, Any] | None = None,
    ) -> tuple[ObsType, MaskedInfo[Any]]:
        if seed is not None:
            self._np_random = np.random.default_rng(seed)

        super().reset(seed, options)
        self._agent_started = self._np_random.choice([True, False])
        if seed is not None:
            self.env.action_space(self._agent_name).seed(seed)
            self.env.action_space(self._opponent_name).seed(seed)

        if not self._agent_started:
            self._opponent_step()
        observation = self.observe(self._agent_name)
        return observation["observation"], {"action_mask": observation["action_mask"]}
