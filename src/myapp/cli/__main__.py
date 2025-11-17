from rya.cli import initiate_cli_startup

from ..names import AppIdentity
from .app import app

initiate_cli_startup(app)
app(prog_name=AppIdentity.app_name)
