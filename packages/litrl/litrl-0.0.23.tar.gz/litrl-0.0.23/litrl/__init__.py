import warnings

from pydantic.warnings import PydanticDeprecatedSince20

from litrl._version import __version__
from litrl.env.make import make, make_multiagent

warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20, module="mlflow")
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
warnings.filterwarnings(
    "ignore",
    category=PydanticDeprecatedSince20,
    module="huggingface_hub",
)

__all__ = ["make", "make_multiagent", "__version__"]
