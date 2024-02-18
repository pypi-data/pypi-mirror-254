from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterator

from litrl.algo.mcts.expansion import VanillaExpansion
from litrl.algo.mcts.node import Root

if TYPE_CHECKING:
    from litrl.algo.mcts.typing import AnyNode, MultiAgentMctsEnv


class SelectionStrategy(ABC):
    @abstractmethod
    def select_and_step(self, env: MultiAgentMctsEnv, node: AnyNode) -> AnyNode:
        ...


def ucb_select_and_step(env: MultiAgentMctsEnv, node: AnyNode) -> AnyNode:
    ucb_scores = {
        action: edge.ucb(value_strategy=node.value_strategy, exploration_coef=node.exploration_coef)
        for action, edge in node.edges.items()
    }
    action = max(ucb_scores, key=lambda action: ucb_scores[action])
    child = node.children[action]
    env.step(action)
    return child


class VanillaOpponentSelection(SelectionStrategy):
    def __init__(self) -> None:
        super().__init__()

    def select_and_step(self, env: MultiAgentMctsEnv, node: AnyNode) -> AnyNode:
        _, _, terminated, truncated, _ = env.last()
        if terminated or truncated or node.visits == 0:
            return node
        return ucb_select_and_step(env, node)


class VanillaSelection(SelectionStrategy):
    def __init__(
        self,
        opponent_selection: SelectionStrategy | None = None,
    ) -> None:
        super().__init__()
        self.opponent_selection = opponent_selection if opponent_selection is not None else VanillaOpponentSelection()
        self.root_depth: int

    def select_and_step(self, env: MultiAgentMctsEnv, node: AnyNode) -> AnyNode:
        if isinstance(node, Root):
            self.root_depth = node.depth
        _, _, terminated, truncated, _ = env.last()
        # stop the recursion
        if terminated or truncated or node.n_children == 0:
            return node

        child = ucb_select_and_step(env, node)

        if child.depth % 2 != self.root_depth % 2:
            child = self.opponent_selection.select_and_step(env, child)
        return self.select_and_step(env, child)


class HardcodedSelectionStrategy(SelectionStrategy):
    def __init__(self, actions: Iterator[int]) -> None:
        self.actions = actions
        self.expansion = VanillaExpansion()

    def select_and_step(self, env: MultiAgentMctsEnv, node: AnyNode) -> AnyNode:
        try:
            while True:
                action = next(self.actions)
                env.step(action)
                node = node.children[action]
                if len(node.children) == 0:
                    self.expansion.expand(env, node)
        except StopIteration:
            pass
        return node
