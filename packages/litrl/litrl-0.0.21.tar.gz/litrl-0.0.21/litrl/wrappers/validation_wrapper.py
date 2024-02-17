from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Generic

from dateutil import tz
from gymnasium.core import Wrapper, WrapperActType, WrapperObsType
from gymnasium.wrappers.record_video import RecordVideo

from litrl.env.typing import ActType, ObsType
from litrl.wrappers.static_opponent_wrapper import AgentType, StaticOpponentWrapper

if TYPE_CHECKING:
    import gymnasium as gym


class ValidationWrapper(
    Wrapper[WrapperObsType, WrapperActType, ObsType, ActType],
    Generic[AgentType, WrapperObsType, WrapperActType, ObsType, ActType],
):
    def __init__(
        self,
        env: gym.Env[ObsType, ActType] | StaticOpponentWrapper[ObsType, ActType, AgentType],
        render_each_n_episodes: int,
        video_folder: str | None = None,
    ) -> None:
        self.render_each_n_episodes = render_each_n_episodes
        self.video_folder = (
            video_folder
            if video_folder is not None
            else Path(
                "temp",
                "videos",
                str(env.unwrapped.__class__.__name__),
                datetime.now(tz.UTC).strftime("%Y-%m-%d_%H-%M-%S-%Z"),
            )
        )

        def episode_trigger(episode: int) -> bool:
            return episode % self.render_each_n_episodes == 0

        super().__init__(
            RecordVideo(
                env=env,
                video_folder=str(self.video_folder),
                episode_trigger=episode_trigger,
                disable_logger=True,
            ),
        )
