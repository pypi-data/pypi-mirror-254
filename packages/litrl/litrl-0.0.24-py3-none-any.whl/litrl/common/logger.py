from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from lightning.pytorch.loggers import MLFlowLogger
from loguru import logger


def is_windows_absolute_path(path: str) -> bool:
    # Pattern to match the start of a Windows absolute path
    windows_path_pattern = re.compile(r"([a-zA-Z]:\\)")
    return bool(windows_path_pattern.match(path))


class LitRLLogger(MLFlowLogger):
    def __init__(
        self,
        run_id: str | None = None,
        tags: dict[str, Any] | None = None,
        save_dir: str | Path | None = None,
        *,
        log_model: bool = True,
    ) -> None:
        if save_dir is None:
            save_dir = Path("temp", "mlruns").as_uri()
            logger.info(f"Save dir is {save_dir}")

        if is_windows_absolute_path(str(save_dir)):
            save_dir = Path(save_dir).as_uri()

        super().__init__(
            tracking_uri=str(save_dir),
            artifact_location=str(save_dir),
            save_dir=str(save_dir),
            tags=tags,
            log_model=log_model,
            run_id=run_id,
        )
        self._save_dir = str(save_dir)

    @property
    def save_dir(self) -> str:
        return self._save_dir
