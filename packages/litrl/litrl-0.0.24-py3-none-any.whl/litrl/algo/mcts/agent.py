from __future__ import annotations

from typing import TYPE_CHECKING

from loguru import logger

from litrl.algo.mcts.backpropagate import VanillaBackpropagate
from litrl.algo.mcts.mcts import MCTS
from litrl.algo.mcts.mcts_config import MCTSConfig, MCTSConfigBuilder
from litrl.algo.mcts.select import VanillaSelection
from litrl.algo.mcts.typing import MultiAgentMctsEnv
from litrl.common.agent import Agent
from litrl.env.connect_four import ConnectFour

if TYPE_CHECKING:
    from litrl.algo.mcts.node import Root


class MCTSAgent(Agent[MultiAgentMctsEnv, int]):
    def __init__(
        self,
        cfg: MCTSConfig | None = None,
        *,
        prompt_action: bool = False,
    ) -> None:
        if cfg is None:
            cfg = MCTSConfigBuilder().build()
        super().__init__()
        self._cfg = cfg
        self._prompt_action = prompt_action
        self.mcts: MCTS | None = None
        self.game_root: Root | None = None

    def get_action(self, env: MultiAgentMctsEnv) -> int:
        logger.debug("MCTS get action called")
        # the env can be updated externally, which in turn updates the root's env.
        # them being equal does not guarantee consistency.
        # TODO make this cleaner
        if not isinstance(env, ConnectFour):
            raise NotImplementedError

        if self.mcts is None or env != self.mcts.root.env:
            logger.warning("MCTS is being reset")
            if self.mcts is None:
                logger.warning("self.mcts is None")
            else:
                logger.warning(f"{env != self.mcts.root.env} {self.mcts.root.depth} {env.episode_steps}")
            self.mcts = MCTS(env, self._cfg)

            # keep the original root in memory in case the environment is reset. Enables reuse the computations.
            if self.mcts.root.depth == 0:
                self.game_root = self.mcts.root

        action = self.mcts.get_action()
        if self._prompt_action:
            input("Opponent's turn, press enter to continue")
        logger.debug(f"action is: {action}")
        return action

    def __str__(self) -> str:
        return self.__class__.__name__ + "|" + str(self._cfg)

    def step(self, env: MultiAgentMctsEnv, action: int) -> None:
        """Update the tree with external changes to the environment."""
        env.step(action)
        logger.debug(f"informed of action {action}")
        if self.mcts is not None:
            logger.debug(f"root depth {self.mcts.root.depth}, visits {self.mcts.root.visits}")
            self.mcts.root = self.mcts.root.new_root(action, env)
            logger.debug(f"new root depth {self.mcts.root.depth}, new visits {self.mcts.root.visits}")
            if isinstance(self.mcts.cfg.selection_strategy, VanillaSelection):
                self.mcts.cfg.selection_strategy.root_depth = self.mcts.root.depth
            if isinstance(self.mcts.cfg.backpropagate_strategy, VanillaBackpropagate):
                self.mcts.cfg.backpropagate_strategy.root_depth = self.mcts.root.depth
            if len(self.mcts.root.edges) == 0:
                # was not expanded, probably small simulation count.
                self.mcts.cfg.expansion_strategy.expand(self.mcts.root.env, self.mcts.root)

    def reset(self, env: MultiAgentMctsEnv) -> None:
        """Update the tree with external changes to the environment."""
        env.reset()
        if self.mcts is not None and self.game_root is not None:
            self.mcts.root = self.game_root
