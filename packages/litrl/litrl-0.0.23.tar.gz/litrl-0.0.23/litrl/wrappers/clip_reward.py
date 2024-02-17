import gymnasium as gym
from gymnasium.core import ActType, ObsType
from gymnasium.wrappers.transform_reward import TransformReward


class ClipRewardWrapper(TransformReward):
    def __init__(
        self,
        env: gym.Env[ObsType, ActType],
        min_reward: float = -float("inf"),
        max_reward: float = float("inf"),
    ) -> None:
        def transform_reward(reward: float) -> float:
            return max(min(reward, max_reward), min_reward)

        super().__init__(env, transform_reward)
