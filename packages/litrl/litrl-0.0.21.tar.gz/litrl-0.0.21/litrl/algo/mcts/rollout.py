from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Iterator

if TYPE_CHECKING:
    from litrl.algo.mcts.typing import MctsActionType
    from litrl.env.typing import MultiAgentEnv
from litrl.common.agent import Agent, RandomMultiAgent


class RolloutStrategy(ABC):
    @abstractmethod
    def rollout(self, env: MultiAgentEnv[Any, Any, Any], as_player: str) -> float:
        ...


class VanillaRollout(RolloutStrategy):
    def __init__(
        self,
        rollout_agent: Agent[MultiAgentEnv[Any, Any, Any], MctsActionType] | None = None,
    ) -> None:
        super().__init__()
        self.rollout_agent: Agent[MultiAgentEnv[Any, Any, Any], MctsActionType] = (
            rollout_agent if rollout_agent is not None else RandomMultiAgent[Any, Any, Any, Any]()
        )

    def rollout(self, env: MultiAgentEnv[Any, Any, Any], as_player: str) -> float:
        _, reward, terminated, truncated, _ = env.last()
        while not (terminated or truncated):
            action = self.rollout_agent.get_action(env)
            env.step(action)
            _, reward, terminated, truncated, _ = env.last()

        if env.unwrapped.agent_selection != as_player:
            reward = -reward
        return max(0, reward)


class HardcodedRolloutAgent(Agent[Any, Any]):
    def __init__(self, actions: Iterator[int]) -> None:
        super().__init__()
        self.actions = actions

    def get_action(self, env: MultiAgentEnv[Any, Any, Any]) -> int:
        del env
        return next(self.actions)
