from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from litrl.algo.mcts.edge import Edge


class ValueStrategy(ABC):
    @abstractmethod
    def value(self, edge: Edge) -> float | None:
        ...


class Winrate(ValueStrategy):
    def value(self, edge: Edge) -> float | None:
        if edge.visits == 0:
            return None
        return edge.reward_sum / edge.visits


class Minmax(ValueStrategy):
    def __init__(self, value_strategy: ValueStrategy | None = None) -> None:
        super().__init__()
        self.value_strategy = value_strategy if value_strategy is not None else Winrate()

    def value(self, edge: Edge) -> float | None:
        """Find the winrate based on the opponent's best play."""
        child = edge.child
        if len(child.edges) == 0:
            return None

        child_values_optional = [self.value_strategy.value(edge) for edge in child.edges.values()]
        child_values = [cv for cv in child_values_optional if cv is not None]
        if len(child_values) == 0:
            return None
        return min(child_values)
