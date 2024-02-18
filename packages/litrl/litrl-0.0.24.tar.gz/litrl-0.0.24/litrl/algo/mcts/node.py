from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, Optional, TypeVar

from litrl.algo.mcts.edge import Edge
from litrl.algo.mcts.value import ValueStrategy, Winrate

if TYPE_CHECKING:
    from litrl.algo.mcts.typing import AnyNode, MctsActionType, MultiAgentMctsEnv

EdgeType = TypeVar("EdgeType", Edge, None)


class Node(Generic[EdgeType], ABC):
    def __init__(
        self,
        parent_edge: EdgeType,
        depth: int,
        value_strategy: ValueStrategy | None = None,
        exploration_coef: float = 1,
    ) -> None:
        if value_strategy is None:
            value_strategy = Winrate()
        self.parent_edge: EdgeType = parent_edge
        self.edges: dict[MctsActionType, Edge] = {}
        self.exploration_coef = exploration_coef
        self.value_strategy = value_strategy
        self.depth = depth

    def add_child(self, action: MctsActionType) -> None:
        edge = Edge(parent=self)
        self.edges[action] = edge
        edge.child = ChildNode(parent_edge=edge, depth=self.depth + 1)

    @property
    def visits(self) -> float:
        return sum(edge.visits for edge in self.edges.values())

    @property
    def reward_sum(self) -> float:
        return sum(edge.reward_sum for edge in self.edges.values())

    @property
    @abstractmethod
    def parent(self) -> Optional[AnyNode]:  # noqa: UP007
        raise NotImplementedError

    @property
    def n_children(self) -> int:
        return len(self.edges)

    @property
    def children(self) -> dict[MctsActionType, ChildNode]:
        return {action: edge.child for action, edge in self.edges.items()}


class Root(Node[None]):
    def __init__(self, env: MultiAgentMctsEnv) -> None:
        super().__init__(parent_edge=None, depth=env.episode_steps)
        self.env = env

    @property
    def parent(self) -> None:
        return None

    def new_root(self, action: MctsActionType, env: MultiAgentMctsEnv) -> Root:
        new_root = Root(env)
        child = self.edges[action].child
        new_root.parent_edge = None
        new_root.edges = child.edges
        return new_root


class ChildNode(Node["Edge"]):
    @property
    def parent(self) -> AnyNode:
        return self.parent_edge.parent
