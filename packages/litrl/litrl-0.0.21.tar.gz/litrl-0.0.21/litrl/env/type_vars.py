from __future__ import annotations

from typing import Any, TypeVar, Union

from litrl.env.typing import MultiAgentEnv, SingleAgentEnv

EnvType = TypeVar(  # TODO move somewhere else.
    "EnvType",
    bound=Union[SingleAgentEnv[Any, Any], MultiAgentEnv[Any, Any, Any]],
)
