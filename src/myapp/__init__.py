# ╭─────────────────────── Important ────────────────────────╮
# │                                                          │
# │ Don't modify code within the border down below, unless   │
# │ you know what you are doing. The "import" sequences      │
# │ below controls the trigger points for overloading rya.   │
# │ You can import your own modules as you wish outside the  │
# │ border.                                                  │
# │                                                          │
# ╰──────────────────────────────────────────────────────────╯

from properpath import P

# Only modules from rya.pre_utils should be imported.
from rya.pre_utils import (
    LayerLoader,
    get_logger,
    load_basic_debug_mode,
)

# Only main app layers that don't rely on rya (except
# rya.pre_utils)layer should be imported. The following
# triggers sys.modules registration of the
# .names. __init__
from .names import AppIdentity

LayerLoader.logger = P.default_err_logger = get_logger()
load_basic_debug_mode(AppIdentity.app_name, reload=True)
LayerLoader.enable_bootstrap_mode(
    root_installation_dir=P(__file__).parent,
    app_name=AppIdentity.app_name,
)
# The following import calls get_logger. This makes sure when
# the app is imported as a package "import <myapp>", it
# automatically registers the main "myapp" logger to
# Python's built-in logging.
from rya.loggers import get_logger  # noqa: E402, F401, I001

# Calling get_logger ensures the main "myapp" logger
# is registered to Python built-in logging.
get_logger()

# The border
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# The following makes sure ConfigModel is registered as soon as
# Rya is finished bootstrapping. You should remove this line
# if you are not using configuration files at all.
# You may rename the class "ConfigModel" to whatever
# else you like in .config/
from .config import ConfigModel  # noqa: E402, F401
