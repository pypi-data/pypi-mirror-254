from abc import ABC, abstractmethod

from litrl.algo.mcts.node import ChildNode
from litrl.algo.mcts.typing import AnyNode


class BackpropagateStrategy(ABC):
    @abstractmethod
    def backpropagate(self, node: AnyNode, reward: float) -> None:
        ...


N_PLAYERS = 2


class VanillaBackpropagate(BackpropagateStrategy):
    def __init__(self, root_depth: int = 0) -> None:
        super().__init__()
        self.root_depth = root_depth

    def backpropagate(self, node: AnyNode, reward: float) -> None:
        """Update the node statistics of the tree with the reward as observed by root's player turn."""
        if not isinstance(node, ChildNode):  # root node
            return

        if node.parent.depth % N_PLAYERS == self.root_depth % N_PLAYERS:  # see reward from root's perspective
            node.parent_edge.update(reward)
        else:
            node.parent_edge.update(1 - reward)
        self.backpropagate(node.parent, reward)
