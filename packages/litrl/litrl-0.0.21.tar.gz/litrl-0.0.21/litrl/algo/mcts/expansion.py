from abc import ABC, abstractmethod

import numpy as np

from litrl.algo.mcts.typing import AnyNode, MultiAgentMctsEnv


class ExpansionStrategy(ABC):
    @abstractmethod
    def expand(self, env: MultiAgentMctsEnv, node: AnyNode) -> None:
        ...


class VanillaExpansion(ExpansionStrategy):
    def __init__(self) -> None:
        super().__init__()

    def expand(self, env: MultiAgentMctsEnv, node: AnyNode) -> None:
        legal_actions = env.observe(env.unwrapped.agent_selection)["action_mask"]
        actions = np.nonzero(legal_actions)[0]
        for action in actions:
            node.add_child(action)
