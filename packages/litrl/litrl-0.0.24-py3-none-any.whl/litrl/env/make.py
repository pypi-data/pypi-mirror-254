from __future__ import annotations

from typing import Any

import gymnasium as gym
import stable_baselines3.common.atari_wrappers as sb3_wrappers
from gymnasium.wrappers.frame_stack import FrameStack
from gymnasium.wrappers.gray_scale_observation import GrayScaleObservation
from gymnasium.wrappers.record_episode_statistics import RecordEpisodeStatistics
from gymnasium.wrappers.resize_observation import ResizeObservation
from loguru import logger
from stable_baselines3.common.atari_wrappers import ClipRewardEnv, EpisodicLifeEnv, MaxAndSkipEnv, NoopResetEnv

from litrl.env.connect_four import ConnectFour
from litrl.env.typing import GYM_IDS, MULTI_AGENT_IDS, ConfigMultiAgentId, GymId
from litrl.wrappers import ClipRewardWrapper, StaticOpponentWrapper, ValidationWrapper


def make_multiagent(
    id: ConfigMultiAgentId,  # noqa: A002
    **kwargs: Any,
) -> ConnectFour:
    if id not in MULTI_AGENT_IDS:
        msg = f"Unsupported multiagent environment: {id}"
        raise NotImplementedError(msg)
    return ConnectFour(**kwargs)


def make(
    id: GymId | ConfigMultiAgentId,  # noqa: A002
    *,
    val: bool = False,
    **kwargs: Any,
) -> gym.Env[Any, Any]:
    if id not in [*GYM_IDS, *MULTI_AGENT_IDS]:
        msg = f"Unsupported multiagent environment: {id}"
        raise NotImplementedError(msg)
    logger.debug(f"Creating environment: {id}")
    render_mode = "rgb_array" if val else kwargs.pop("render_mode", None)
    render_each_n_episodes = kwargs.pop("render_each_n_episodes", 1)
    opponent = kwargs.pop("opponent", None)
    env: gym.Env[Any, Any]
    if id == "CartPole-v1":
        env = gym.make(id="CartPole-v1", render_mode=render_mode, **kwargs)
    elif id == "BreakoutNoFrameskip-v4":
        env = gym.make("BreakoutNoFrameskip-v4", render_mode=render_mode, **kwargs)
        env = NoopResetEnv(env, noop_max=30)
        env = MaxAndSkipEnv(env, skip=4)
        env = EpisodicLifeEnv(env)
        if "FIRE" in env.unwrapped.get_action_meanings():  # type: ignore[attr-defined]
            env = sb3_wrappers.FireResetEnv(env)
        env = ClipRewardEnv(env)
        env = ResizeObservation(env, (84, 84))
        env = GrayScaleObservation(env)
        env = FrameStack(env, 4)
    elif id == "connect_four":
        env = StaticOpponentWrapper(
            make_multiagent("connect_four", render_mode=render_mode, **kwargs),
            opponent=opponent,
        )
    elif id == "LunarLander-v2":
        env = ClipRewardWrapper(
            env=gym.make(id="LunarLander-v2", render_mode=render_mode, **kwargs),
            min_reward=-1,
        )
    else:
        message = f"Unsupported environment: {id}"
        raise ValueError(message)
    env = RecordEpisodeStatistics(env=env)
    if val:
        env = ValidationWrapper(env=env, render_each_n_episodes=render_each_n_episodes)
    return env
