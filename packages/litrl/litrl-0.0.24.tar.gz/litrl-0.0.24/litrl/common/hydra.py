from __future__ import annotations

import uuid
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pyrootutils
from hydra import compose, initialize
from loguru import logger
from omegaconf import DictConfig, OmegaConf

from litrl.common.mlflow import get_mlflow_run_id

if TYPE_CHECKING:
    from litrl.env.typing import ConfigEnvId
    from litrl.model.base_module import ModelId
from litrl.schema.config import ConfigSchema

VERSION_BASE: str = "1.3.2"


def register_resolvers() -> None:
    if not OmegaConf.has_resolver("uuid"):
        OmegaConf.register_new_resolver(
            name="uuid",
            resolver=lambda _: str(uuid.uuid4()),
        )

    if not OmegaConf.has_resolver("mlflow"):
        OmegaConf.register_new_resolver(
            name="mlflow",
            resolver=lambda run_id: get_mlflow_run_id(run_id),
        )


def omegaconf_to_schema(cfg: DictConfig) -> ConfigSchema[Any]:
    OmegaConf.resolve(cfg)
    logger.info(f"config is \n{OmegaConf.to_yaml(cfg)}")
    return ConfigSchema(**OmegaConf.to_container(cfg))  # type: ignore[arg-type]


def get_config(
    env: ConfigEnvId,
    model: ModelId,
    overrides: list[str] | None = None,
) -> ConfigSchema[Any]:
    # TODO make this compatible with Windows
    if overrides is None:
        overrides = []
    root_path = pyrootutils.find_root().absolute()
    path = Path(__file__)
    relative_path = ""
    while not path.parent.samefile(root_path):
        path = path.parent
        relative_path += "../"
    relative_path += "config"

    register_resolvers()
    with initialize(version_base=VERSION_BASE, config_path=relative_path):
        dict_config = compose(
            config_name="default",
            overrides=[f"model={model}", f"env={env}", *overrides],
        )
    return omegaconf_to_schema(cfg=dict_config)
