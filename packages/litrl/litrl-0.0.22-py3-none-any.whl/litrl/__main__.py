import hydra
from omegaconf import DictConfig

from litrl.common.hydra import VERSION_BASE, omegaconf_to_schema, register_resolvers
from litrl.train import train

register_resolvers()


@hydra.main(config_path="../config", config_name="default", version_base=VERSION_BASE)
def main(omegaconf_cfg: DictConfig) -> None:
    """Enter the project."""
    cfg = omegaconf_to_schema(cfg=omegaconf_cfg)
    train(cfg)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
