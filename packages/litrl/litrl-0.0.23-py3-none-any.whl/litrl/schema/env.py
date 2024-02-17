from __future__ import annotations

from typing import Generic, Optional, Union

from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.env.type_vars import EnvType
from litrl.schema.agent import AgentSchema, MCTSAgentSchema  # noqa: TCH001
from litrl.schema.instantiator import InstantiatorClass


@pydantic_dataclass(frozen=True)
class EnvSchema(InstantiatorClass[EnvType], Generic[EnvType]):
    id: str  # noqa: A003
    opponent: Optional[Union[AgentSchema, MCTSAgentSchema]] = None  # noqa: UP007
    val: Optional[bool] = None  # noqa: UP007
