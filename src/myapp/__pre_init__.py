# Only modules that don't depend on layers above rya.pre_utils
# should be imported in the top level (below). All other modules
# should be imported within the function body.

from properpath import P
from rya.pre_utils import (
    DebugMode,
    LayerLoader,
    get_logger,
)

from .names import AppIdentity

__all__ = [
    "enable_bootstrap_mode",
    "register_logger",
    "register_config_model",
]


def enable_bootstrap_mode() -> None:
    # The following triggers sys.modules registration of the
    # .names. __init__

    LayerLoader.logger = P.default_err_logger = get_logger()
    DebugMode(AppIdentity.app_name).load(reload=True)
    LayerLoader.enable_bootstrap_mode(
        root_installation_dir=P(__file__).parent,
        app_name=AppIdentity.app_name,
    )


def register_logger() -> None:
    # The following import calls get_logger. This makes sure when
    # the app is imported as a package "import <myapp>", it
    # automatically registers the main "myapp" logger to
    # Python's built-in logging.
    from rya.loggers import get_logger

    # Calling get_logger ensures the main "myapp" logger
    # is registered to Python built-in logging.
    get_logger()


def register_config_model() -> None:
    # The following makes sure ConfigModel is registered as soon as
    # Rya is finished bootstrapping. You should remove this line
    # if you are not using configuration files at all.
    # You may rename the class "ConfigModel" to whatever
    # else you like in .config/
    from rya.config import ConfigMaker

    from .config import ConfigModel

    # Add model registers the model to Rya
    ConfigMaker.add_model(ConfigModel)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Use/add your custom functions below
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
