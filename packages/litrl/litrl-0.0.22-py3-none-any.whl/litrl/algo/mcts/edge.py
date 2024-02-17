from math import log, sqrt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from litrl.algo.mcts.node import ChildNode
    from litrl.algo.mcts.typing import AnyNode
    from litrl.algo.mcts.value import ValueStrategy


class Edge:
    def __init__(self, parent: "AnyNode") -> None:
        self.parent = parent
        self.visits = 0
        self.reward_sum = 0.0
        self.child: "ChildNode"

    @property
    def _uncertainty(self) -> float:
        if self.visits == 0:
            return float("inf")
        return sqrt(log(self.parent.visits) / self.visits)

    def update(self, reward: float) -> None:
        self.visits += 1
        self.reward_sum += reward

    def ucb(self, value_strategy: "ValueStrategy", exploration_coef: float) -> float:
        if self.visits == 0:
            return float("inf")
        value = value_strategy.value(self)
        if value is None:
            value = 0
        return value + exploration_coef * self._uncertainty
