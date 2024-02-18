from __future__ import annotations

import warnings
from typing import Any, Generator

from torch.utils.data import DataLoader, Dataset


class DummyDataset(Dataset[Generator[None, None, None]]):
    def __getitem__(self, index: int) -> Generator[None, None, None]:
        del index
        yield None

    def __len__(self) -> int:
        return 1


class DummyLoader(DataLoader[Generator[None, None, None]]):
    def __init__(self) -> None:
        warnings.filterwarnings("ignore", message=".*does not have many workers.*")

        def do_nothing(x: Any) -> None:
            del x

        super().__init__(DummyDataset(), collate_fn=do_nothing)
