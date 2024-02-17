from __future__ import annotations

from copy import deepcopy
from typing import Any

from loguru import logger

from litrl.common.agent import RandomAgent
from litrl.env.typing import OpponentEnv
from litrl.model.sac.model import Sac
from litrl.model.sac.multi_agent import SacMultiAgent, SacStochasticAgent
from litrl.schema.model import ModelConfigSchema

EnvType = OpponentEnv[Any, Any]


class MultiagentConfigSchema(ModelConfigSchema[EnvType]):
    update_opponent_score: float


class MaSac(Sac[MultiagentConfigSchema]):
    def __init__(
        self,
        cfg: MultiagentConfigSchema,
    ) -> None:
        super().__init__(cfg)

    def get_opponent(self, env: EnvType) -> SacMultiAgent | RandomAgent[Any, Any]:
        return env.get_wrapper_attr("opponent")  # type: ignore[no-any-return]

    def update_actor(self, env: EnvType) -> None:
        opponent = self.get_opponent(env)
        if isinstance(opponent, RandomAgent):
            logger.info("updating random opponent to SAC agent")
            env.get_wrapper_attr("set_opponent")(
                SacStochasticAgent(deepcopy(self.actor)),
            )
            return
        logger.info("Updating the opponent")
        opponent.update(deepcopy(self.actor))

    def update_train_opponent_if_good_training_performance(self) -> None:
        score = self.train_reward_metric.compute()
        if (
            score > self.cfg.update_opponent_score
            and self.train_reward_metric._num_vals_seen >= self.train_reward_metric.window  # noqa: SLF001
        ):
            logger.debug(
                f"Running training {score} > {self.cfg.update_opponent_score}, updating training opponent",
            )
            self.update_actor(self.env)
            self.train_reward_metric.reset()

    def on_train_epoch_end(self) -> None:
        self.update_train_opponent_if_good_training_performance()
        super().on_train_epoch_end()

    def on_validation_epoch_end(self) -> None:
        super().on_validation_epoch_end()
