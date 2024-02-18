from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    import sys

    if sys.version_info[:2] >= (3, 11):
        from typing import Self, TypeAlias
    else:
        from typing_extensions import Self, TypeAlias

from litrl.algo.mcts.edge import Edge
from litrl.algo.mcts.node import Node
from litrl.env.typing import MultiAgentEnv

MctsActionType: TypeAlias = int
AnyNode: TypeAlias = Union[Node[Edge], Node[None]]


class MultiAgentMctsEnv(MultiAgentEnv[Any, Any, Any]):
    def copy(self) -> Self:
        return deepcopy(self)
