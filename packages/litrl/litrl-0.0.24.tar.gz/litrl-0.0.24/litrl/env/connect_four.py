from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING, Any, List, Literal

if TYPE_CHECKING:
    import sys

    if sys.version_info[:2] >= (3, 11):
        from typing import Self, TypeAlias
    else:
        from typing_extensions import Self, TypeAlias

from nptyping import Shape
from pettingzoo.classic.connect_four_v3 import raw_env as ConnectFourRaw

from litrl.env.typing import MaskedObs, MultiAgentEnv

if TYPE_CHECKING:
    from pettingzoo.utils import agent_selector

Board: TypeAlias = List[List[int]]
FlatBoard: TypeAlias = List[int]
ConnectFourActType: TypeAlias = int
ConnectFourObsShape: TypeAlias = Shape["7, 6"]
ConnectFourMaskShape: TypeAlias = Shape["7"]
ConnectFourMaskedObs: TypeAlias = MaskedObs[ConnectFourObsShape, ConnectFourMaskShape]
ConnectFourAgentID: TypeAlias = Literal["player_0", "player_1"]


def flatten_board(board: Board) -> FlatBoard:
    return [item for row in board for item in row]


class ConnectFour(ConnectFourRaw, MultiAgentEnv[ConnectFourMaskedObs, ConnectFourActType, ConnectFourAgentID]):  # type: ignore[misc]
    """PettingZoo ConnectFour has multiple issues (reproducibility, typing) that we fix here."""

    def __init__(self, render_mode: str | None = None, screen_scaling: int = 9) -> None:
        super().__init__(render_mode=render_mode, screen_scaling=screen_scaling)
        self._agent_selector: agent_selector
        self.agent_selection: ConnectFourAgentID
        self.board: FlatBoard
        self.possible_agents: list[ConnectFourAgentID]
        self.episode_steps: int

    @property
    def unwrapped(self) -> Self:  # type: ignore[override]
        """Wrappers override this function to return the underlying raw environment."""
        return self

    def observe(self, agent: ConnectFourAgentID) -> MaskedObs[ConnectFourObsShape, ConnectFourMaskShape]:
        return super().observe(agent)

    def step(self, action: int) -> None:
        self.episode_steps += 1
        return super().step(action)

    def copy(self) -> ConnectFour:
        new_env = deepcopy(self)
        # for some reason, deepcopy doesn't copy everything (e.g. agent_selection) as expected
        for key, val in self.__dict__.items():
            if key not in new_env.__dict__ or key == "board":
                setattr(new_env, key, deepcopy(val))
        return new_env

    def reset(
        self,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> None:
        super().reset(seed=seed, options=options)
        self.episode_steps = 0
        for agent_id in self.possible_agents:
            self.action_space(agent=agent_id).seed(seed=seed)
