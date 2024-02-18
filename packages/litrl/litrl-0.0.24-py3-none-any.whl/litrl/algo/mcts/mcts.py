from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from litrl.algo.mcts.node import Root

if TYPE_CHECKING:
    from litrl.algo.mcts.typing import MultiAgentMctsEnv

from litrl.algo.mcts.backpropagate import VanillaBackpropagate
from litrl.algo.mcts.mcts_config import MCTSConfig, MCTSConfigBuilder
from litrl.algo.mcts.select import VanillaSelection


class MCTS:
    def __init__(
        self,
        env: MultiAgentMctsEnv,
        cfg: MCTSConfig | None = None,
    ) -> None:
        cfg = cfg if cfg is not None else MCTSConfigBuilder().build()
        self.cfg = cfg
        self._np_random = np.random.default_rng(seed=cfg.seed)
        self.root = Root(env)
        if isinstance(cfg.backpropagate_strategy, VanillaBackpropagate):
            cfg.backpropagate_strategy.root_depth = self.root.depth
        if isinstance(cfg.selection_strategy, VanillaSelection):
            cfg.selection_strategy.root_depth = self.root.depth
        self.cfg.expansion_strategy.expand(self.root.env, self.root)

    def simulate(self) -> None:
        temp_env = self.root.env.copy()
        node = self.cfg.selection_strategy.select_and_step(
            temp_env,
            self.root,
        )
        self.cfg.expansion_strategy.expand(temp_env, node)
        reward = self.cfg.rollout_strategy.rollout(
            temp_env,
            self.root.env.unwrapped.agent_selection,
        )
        self.cfg.backpropagate_strategy.backpropagate(node, reward)

    def get_action(self) -> int:
        for _ in range(self.cfg.simulations):
            self.simulate()

        return self.cfg.recommend_strategy.get_action(self.root)
