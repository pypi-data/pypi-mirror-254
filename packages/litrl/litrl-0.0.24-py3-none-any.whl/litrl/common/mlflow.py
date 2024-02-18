from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import mlflow

if TYPE_CHECKING:
    import pandas as pd
from loguru import logger


def get_mlflow_run_id(run_id: str | None = None) -> str:
    mlflow.set_tracking_uri(Path("temp", "mlruns"))
    if run_id is not None:
        run = mlflow.get_run(run_id)
        return run.info.run_id  # type: ignore[no-any-return]

    active_run = mlflow.active_run()
    if active_run is not None:
        return active_run.info.run_id  # type: ignore[no-any-return]

    run = mlflow.start_run()
    return run.info.run_id  # type: ignore[no-any-return]


def get_load_path(tags: dict[str, str], load: str | None) -> Path | None:
    if load is None:
        return None
    if load != "latest":
        return Path(load)
    return get_latest_path(tags)


def get_latest_path(tags: dict[str, str]) -> Path | None:
    filter_string = ""
    for i, (key, value) in enumerate(tags.items()):
        if i > 0:
            filter_string += " AND "
        filter_string += f"tags.{key} = '{value}'"
    filter_string += " AND metrics.epoch > 10"
    recent_run: pd.DataFrame = mlflow.search_runs(
        search_all_experiments=True,
        filter_string=filter_string,
        order_by=["metrics.end_time DESC"],
        max_results=1,
    )
    checkpoint_dir = get_checkpoint_dir(recent_run)
    if checkpoint_dir is None:
        return checkpoint_dir
    return get_load_path_from_dir(checkpoint_dir)


def get_checkpoint_dir(recent_run: pd.DataFrame) -> Path | None:
    if len(recent_run) == 0:
        return None
    if len(recent_run) > 1:
        msg = "More than one model found"
        raise ValueError(msg)
    info = recent_run.loc[0]
    tracking_uri = mlflow.get_tracking_uri().replace("file://", "")
    return Path(tracking_uri).joinpath(
        info["experiment_id"],
        info["run_id"],
        "checkpoints",
    )


def get_load_path_from_dir(checkpoint_dir: Path) -> Path | None:
    if not checkpoint_dir.exists():
        return None
    checkpoint_files = list(checkpoint_dir.glob("*.ckpt"))
    if len(checkpoint_files) == 0:
        return None
    if len(checkpoint_files) > 1:
        logger.warning("More than one checkpoint found")
    load_path = checkpoint_files[0]
    if not load_path.exists():
        logger.warning(f"Checkpoint file {load_path} does not exist")
        return None
    logger.debug(f"checkpoint to use at {load_path}")
    return load_path
