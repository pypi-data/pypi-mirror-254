import sys
from dataclasses import dataclass
from typing import Any

if sys.version_info[:2] >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

import numpy as np

from litrl.algo.mcts.backpropagate import BackpropagateStrategy, VanillaBackpropagate
from litrl.algo.mcts.expansion import ExpansionStrategy, VanillaExpansion
from litrl.algo.mcts.recommend import RecommendStrategy, VanillaRecommend
from litrl.algo.mcts.rollout import RolloutStrategy, VanillaRollout
from litrl.algo.mcts.select import SelectionStrategy, VanillaSelection
from litrl.algo.mcts.typing import MctsActionType
from litrl.common.agent import RandomMultiAgent


@dataclass
class MCTSConfig:
    selection_strategy: SelectionStrategy
    rollout_strategy: RolloutStrategy
    backpropagate_strategy: BackpropagateStrategy
    expansion_strategy: ExpansionStrategy
    recommend_strategy: RecommendStrategy
    simulations: int
    seed: int

    def __str__(self) -> str:
        return f"simulations={self.simulations}, rollout_strategy={self.rollout_strategy!s}"


class MCTSConfigBuilder:
    def __init__(self) -> None:
        self._seed = 123
        self._simulations = 50
        self._selection_strategy: SelectionStrategy = VanillaSelection()
        self._rollout_strategy: RolloutStrategy = VanillaRollout(
            rollout_agent=RandomMultiAgent[Any, Any, MctsActionType, Any](np.random.default_rng(seed=self._seed)),
        )
        self._backpropagate_strategy: BackpropagateStrategy = VanillaBackpropagate()
        self._expansion_strategy: ExpansionStrategy = VanillaExpansion()
        self._recommend_strategy: RecommendStrategy = VanillaRecommend()

    def set_rollout_strategy(self, rollout_strategy: RolloutStrategy) -> Self:
        self._rollout_strategy = rollout_strategy
        return self

    def set_selection_strategy(self, selection_strategy: SelectionStrategy) -> Self:
        self._selection_strategy = selection_strategy
        return self

    def set_simulations(self, simulations: int) -> Self:
        self._simulations = simulations
        return self

    def build(self) -> MCTSConfig:
        return MCTSConfig(
            seed=self._seed,
            simulations=self._simulations,
            selection_strategy=self._selection_strategy,
            rollout_strategy=self._rollout_strategy,
            backpropagate_strategy=self._backpropagate_strategy,
            expansion_strategy=self._expansion_strategy,
            recommend_strategy=self._recommend_strategy,
        )
