from __future__ import annotations

import uuid
import warnings
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

import git
import torch
import yaml
from huggingface_hub import CommitOperationAdd, HfApi, hf_hub_download, metadata_eval_result
from huggingface_hub.repocard import metadata_save
from huggingface_hub.utils._errors import RepositoryNotFoundError
from hydra.core.hydra_config import HydraConfig
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.loggers import MLFlowLogger
from loguru import logger
from moviepy.editor import VideoFileClip
from pydantic import RootModel
from requests.exceptions import ConnectionError

from litrl import _version as litrl_version

if TYPE_CHECKING:
    from hydra.conf import HydraConf
    from lightning import Trainer

    from litrl.model.base_module import LitRLModule

MODEL_REPO = "c-gohlke/litrl"
DATASET_REPO = "c-gohlke/litrl"

MODEL_REPO_TYPE = "model"
DATASET_REPO_TYPE = "dataset"


class DummyInputNotFoundWarning(Warning):
    pass


class ModelNotFoundWarning(Warning):
    pass


class NoBufferFoundWarning(Warning):
    pass


class HuggingfaceCallback(ModelCheckpoint):
    def __init__(  # noqa: PLR0913
        self,
        mode: Literal["min", "max"] = "max",
        monitor: Literal["val_reward"] = "val_reward",
        filename: str = "{val_reward:.2f}-{step}",
        model_name: str = "actor",
        local_path: Path | None = None,
        *,
        upload_model: bool = True,
        upload_dataset: bool = True,
        upload_space: bool = True,
        **kwargs: Any,
    ) -> None:
        super().__init__(mode=mode, monitor=monitor, filename=filename, **kwargs)
        self.model_name = model_name
        self.model_operations: list[CommitOperationAdd] = []
        self.dataset_operations: list[CommitOperationAdd] = []
        self.upload_model = upload_model
        self.upload_dataset = upload_dataset
        self.upload_space = upload_space
        self.local_path = local_path

        self.hf_model_run_dir: str
        self.hf_model_dir: str
        self.hf_env_dir: str
        self.run_id: str
        self.best_model_path: str
        self.hf_api: HfApi
        self.model: torch.nn.Module | None
        self.dummy_input: torch.Tensor | None
        self.tempdir: Path
        self.mp4_dir: Path | None

    def get_run_id(self, trainer: Trainer) -> str:
        if isinstance(trainer.logger, MLFlowLogger):
            if trainer.logger.run_id is None:
                msg = "MLFlowLogger has no run_id"
                raise ValueError(msg)
            return trainer.logger.run_id
        return str(uuid.uuid4())

    def on_train_start(self, trainer: Trainer, pl_module: LitRLModule[Any]) -> None:  # type: ignore[override]
        if trainer.logger is None or trainer.logger.save_dir is None:
            msg = "trainer.logger.save_dir is None"
            raise ValueError(msg)
        super().on_train_start(trainer=trainer, pl_module=pl_module)
        self.cfg = pl_module.cfg
        self.run_id = self.get_run_id(trainer)
        self.env_identifier = self.cfg.env_fabric.id
        self.model_identifier = pl_module.__class__.__name__
        self.hf_env_dir = f"models/{self.env_identifier}"
        self.hf_model_dir = self.hf_env_dir + f"/{self.model_identifier}"
        self.hf_model_run_dir = self.hf_model_dir + f"/{self.run_id}"

        self.log_dir = Path(trainer.logger.save_dir)

        self.hf_data_dir: str = f"datasets/{self.env_identifier}/{self.model_identifier}/{self.run_id}"
        self.tempdir = (
            Path.cwd().joinpath("temp", "huggingface", self.run_id) if self.local_path is None else self.local_path
        )
        self.tempdir.mkdir(parents=True, exist_ok=True)
        try:
            self.mp4_dir = Path(pl_module.val_env.video_folder)
        except AttributeError:
            self.mp4_dir = None

        try:
            self.model = getattr(pl_module, self.model_name)
        except AttributeError:
            warnings.warn(ModelNotFoundWarning(), stacklevel=1)
            self.model = None
        try:
            self.dummy_input = pl_module.obs
        except AttributeError:
            warnings.warn(DummyInputNotFoundWarning(), stacklevel=1)
            self.dummy_input = None
        try:
            self.buffer = pl_module.buffer
        except AttributeError:
            warnings.warn(NoBufferFoundWarning(), stacklevel=1)
            self.buffer = None

    def on_exception(  # type: ignore[override]
        self,
        trainer: Trainer,
        pl_module: LitRLModule[Any],
        exception: BaseException,
    ) -> None:
        self._upload_run()
        return super().on_exception(trainer, pl_module, exception)

    def on_fit_end(self, trainer: Trainer, pl_module: LitRLModule[Any]) -> None:  # type: ignore[override]
        super().on_fit_end(trainer, pl_module)
        if self.best_model_score is None:
            logger.debug(f"No model to upload: {self.best_model_score}")
            return

        try:
            self.hf_api = HfApi()
        except ConnectionError as e:
            logger.error(f"Can't connect to huggingface! {e}")
            return
        self._upload_run()

    def _upload_run(self) -> None:
        if self.upload_model:
            self._update_env_results()
            self._update_model_results()
            self._update_onnx_model()
            self._update_model()
            self._update_readme()
            self._update_cfg()
            self._update_hydra()
            self._update_mp4()
            self._update_logs()
            try:
                files = self.hf_api.list_repo_files(
                    MODEL_REPO,
                    repo_type=MODEL_REPO_TYPE,
                )
                del files
            except RepositoryNotFoundError:
                self.hf_api.create_repo(MODEL_REPO, repo_type=MODEL_REPO_TYPE)

            try:
                self.hf_api.create_commit(
                    repo_id=MODEL_REPO,
                    repo_type=MODEL_REPO_TYPE,
                    operations=self.model_operations,
                    commit_message="Upload new model run",
                )
            except RuntimeError as e:
                logger.error(f"Can't upload model to huggingface! {e}")

        if self.upload_dataset:
            try:
                files = self.hf_api.list_repo_files(
                    DATASET_REPO,
                    repo_type=DATASET_REPO_TYPE,
                )
                del files
            except RepositoryNotFoundError:
                self.hf_api.create_repo(DATASET_REPO, repo_type=DATASET_REPO_TYPE)

            self._update_dataset()
            try:
                self.hf_api.create_commit(
                    repo_id=DATASET_REPO,
                    repo_type=DATASET_REPO_TYPE,
                    operations=self.dataset_operations,
                    commit_message="Upload dataset",
                )
            except RuntimeError as e:
                logger.error(f"Can't upload dataset to huggingface! {e}")

    def _update_logs(self) -> None:
        if not self.log_dir.exists():
            logger.error(f"log dir not found {self.log_dir}")
            return

        hf_log_path = f"{self.hf_model_run_dir}/mlruns"
        self.experiment_id = 0  # TODO get from mlflow
        local_log_path = self.log_dir.joinpath(str(self.experiment_id), self.run_id)
        if not local_log_path.exists():
            logger.error(f"local log path not found {local_log_path}")
            return
        self.hf_api.upload_folder(
            repo_id=MODEL_REPO,
            repo_type=MODEL_REPO_TYPE,
            path_in_repo=hf_log_path,
            folder_path=local_log_path,
            commit_message="Upload mlruns",
        )

    def _update_env_results(self) -> None:
        if self.best_model_score is None:
            return
        hf_files = self.hf_api.list_repo_files(MODEL_REPO, repo_type=MODEL_REPO_TYPE)
        hf_env_results_path = f"{self.hf_env_dir}/results.yaml"
        if hf_env_results_path in hf_files:
            local_env_results_path = hf_hub_download(
                repo_id=MODEL_REPO,
                repo_type=MODEL_REPO_TYPE,
                filename=hf_env_results_path,
            )
            with Path(local_env_results_path).open("r") as file:
                results = yaml.safe_load(file)
            if self.model_identifier in results and results[self.model_identifier] > self.best_model_score:
                msg = (
                    f"Trained model score {self.best_model_score} is "
                    f"less than best found {results[self.model_identifier]}"
                )
                logger.info(msg)
                return
        else:
            local_env_results_path = self.tempdir.joinpath("env_results.yaml")
            results = {}

        results[self.model_identifier] = float(self.best_model_score)
        with Path(local_env_results_path).open("w") as file:
            yaml.dump(results, file)
        self.model_operations.append(
            CommitOperationAdd(
                path_in_repo=hf_env_results_path,
                path_or_fileobj=local_env_results_path,
            ),
        )

    def _update_model_results(self) -> None:
        if self.best_model_score is None:
            return
        files = self.hf_api.list_repo_files(MODEL_REPO, repo_type=MODEL_REPO_TYPE)
        hf_model_results_path = f"{self.hf_model_dir}/results.yaml"
        if hf_model_results_path in files:
            local_model_results_path = hf_hub_download(
                repo_id=MODEL_REPO,
                repo_type=MODEL_REPO_TYPE,
                filename=hf_model_results_path,
            )
            with Path(local_model_results_path).open() as f:
                results = yaml.safe_load(
                    f,
                )
        else:
            local_model_results_path = self.tempdir.joinpath("model_results.yaml")
            results = {}
        results[self.run_id] = float(self.best_model_score)
        with Path(local_model_results_path).open("w") as f:
            yaml.dump(results, f)
        self.model_operations.append(
            CommitOperationAdd(
                path_in_repo=hf_model_results_path,
                path_or_fileobj=local_model_results_path,
            ),
        )

    def _update_mp4(self) -> None:
        if self.mp4_dir is None:
            logger.error("mp4_dir is None")
            return
        if not self.mp4_dir.exists():
            logger.error(f"mp4_dir not found {self.mp4_dir}")
            return
        mp4_files = sorted(self.mp4_dir.iterdir())
        demo_mp4_file = mp4_files[-1]
        if demo_mp4_file.suffix != ".mp4":
            logger.error(f"mp4 file is {demo_mp4_file}")
            return

        hf_mp4_path = f"{self.hf_model_run_dir}/demo.mp4"
        mp4_commit = CommitOperationAdd(
            path_in_repo=hf_mp4_path,
            path_or_fileobj=str(demo_mp4_file),
        )
        self.model_operations.append(mp4_commit)
        self._update_gif(demo_mp4_file)

    def _update_gif(self, demo_mp4_file: Path) -> None:
        video_clip = VideoFileClip(str(demo_mp4_file))
        demo_gif_file = demo_mp4_file.with_suffix(".gif")
        video_clip.write_gif(str(demo_gif_file))  # , fps=30)  # TODO check fps

        hf_gif_path = f"{self.hf_model_run_dir}/demo.gif"
        gif_commit = CommitOperationAdd(
            path_in_repo=hf_gif_path,
            path_or_fileobj=str(demo_gif_file),
        )
        self.model_operations.append(gif_commit)

    def _update_onnx_model(self) -> None:
        onnx_path = self._export_onnx_model()
        if onnx_path is None:
            logger.error("onnx path is None")
            return
        hf_onnx_path = f"{self.hf_model_run_dir}/model.onnx"
        onnx_commit = CommitOperationAdd(
            path_in_repo=hf_onnx_path,
            path_or_fileobj=str(onnx_path),
        )
        self.model_operations.append(onnx_commit)

    def _update_model(self) -> None:
        hf_checkpoint_path = f"{self.hf_model_run_dir}/model.pt"
        logger.info(f"best model path is {self.best_model_path}")
        self.model_operations.append(
            CommitOperationAdd(
                path_in_repo=hf_checkpoint_path,
                path_or_fileobj=self.best_model_path,
            ),
        )

    def _update_cfg(self) -> None:
        hf_config_path = f"{self.hf_model_run_dir}/model_config.yaml"
        temp_config_path = self.tempdir.joinpath("model_config.yaml")

        with temp_config_path.open(mode="w", encoding="utf-8") as file:
            yaml.dump(dict(RootModel(self.cfg)), file)

        self.model_operations.append(
            CommitOperationAdd(
                path_in_repo=hf_config_path,
                path_or_fileobj=temp_config_path,
            ),
        )

    def _update_hydra(self) -> None:
        instance = HydraConfig.instance()
        if instance.cfg is None:
            msg = "HydraConfig was not set"
            logger.warning(msg)
            return
        hydra_conf: HydraConf = instance.cfg.hydra  # type: ignore[attr-defined]
        if hydra_conf.output_subdir is None:
            return
        hydra_dir = Path(hydra_conf.output_subdir)
        hydra_config_path = hydra_dir.joinpath("config.yaml")
        if hydra_config_path.exists():
            hf_hydra_config_path = f"{self.hf_model_run_dir}/config.yaml"
            self.model_operations.append(
                CommitOperationAdd(
                    path_in_repo=hf_hydra_config_path,
                    path_or_fileobj=hydra_config_path,
                ),
            )

        hydra_overrides_path = hydra_dir.joinpath("overrides.yaml")
        if hydra_overrides_path.exists():
            hf_hydra_overrides_path = f"{self.hf_model_run_dir}/overrides.yaml"
            self.model_operations.append(
                CommitOperationAdd(
                    path_in_repo=hf_hydra_overrides_path,
                    path_or_fileobj=hydra_overrides_path,
                ),
            )

    def _update_readme(self) -> None:
        hf_readme_path = f"{self.hf_model_run_dir}/README.md"
        temp_readme_path = self.tempdir.joinpath("README.md")

        self._add_readme_metadata(readme_path=temp_readme_path)
        self.model_operations.append(
            CommitOperationAdd(
                path_in_repo=hf_readme_path,
                path_or_fileobj=temp_readme_path,
            ),
        )

    def _add_readme_metadata(self, readme_path: Path) -> None:
        metadata: dict[str, str | list[str] | dict[str, Any]] = metadata_eval_result(
            model_pretty_name="mock",
            task_pretty_name="reinforcement-learning",
            task_id="reinforcement-learning",
            metrics_pretty_name="mean_reward",
            metrics_id="mean_reward",
            metrics_value="mock +/- mock",
            dataset_pretty_name="mock",
            dataset_id="mock",
        )
        metadata["tags"] = [
            "reinforcement-learning",
            "connect-four",
            "pytorch",
            "custom-implementation",
            "generic",
        ]
        repo = git.Repo(search_parent_directories=True)
        metadata["run_info"] = {
            "litrl": {
                "version": litrl_version,
                "repo_url": repo.remotes.origin.url,
                "commit_hash": repo.head.object.hexsha,
            },
        }
        metadata_save(local_path=readme_path, data=metadata)

    def _export_onnx_model(
        self,
    ) -> Path | None:
        if self.model is None or self.dummy_input is None:
            return None
        onnx_path = self.tempdir.joinpath("model.onnx")
        torch.onnx.export(
            model=self.model,
            args=self.dummy_input,
            f=str(onnx_path),
            input_names=["input"],
            output_names=["output"],
        )
        return onnx_path

    def _update_dataset(self) -> None:
        if self.buffer is None:
            return
        dataset_path = self.tempdir.joinpath("buffer.pt")
        torch.save(obj=self.buffer.state_dict(), f=dataset_path)
        hf_dataset_path = f"{self.hf_data_dir}/buffer.pt"
        logger.info(f"uploading dataset to huggingface at {hf_dataset_path}")
        self.dataset_operations.append(
            CommitOperationAdd(
                path_in_repo=hf_dataset_path,
                path_or_fileobj=dataset_path,
            ),
        )
