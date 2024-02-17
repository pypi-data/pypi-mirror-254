from __future__ import annotations

from typing import Any, Optional

from pydantic.dataclasses import dataclass as pydantic_dataclass

from litrl.common.agent import Agent
from litrl.schema.instantiator import InstantiatorClass


@pydantic_dataclass(frozen=True)
class MCTSConfigSchema:
    simulations: int


@pydantic_dataclass(frozen=True)
class AgentSchema(InstantiatorClass[Agent[Any, Any]]):
    pass


@pydantic_dataclass(frozen=True)
class MCTSAgentSchema(InstantiatorClass[Agent[Any, Any]]):
    cfg: Optional[MCTSConfigSchema]  # noqa: UP007
