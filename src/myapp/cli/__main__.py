from rya.cli import initiate_cli_startup
from rya.cli.doc import MainAppCLIDoc

from ..names import AppIdentity
from .app import app


MainAppCLIDoc.config_file = (
    f"Configuration file with the highest priority. E.g., [green]{AppIdentity.app_name} --C "
    f"./project_config.{AppIdentity.config_file_extension} <command>[/green]."
)
initiate_cli_startup(app)
app(prog_name=AppIdentity.app_name)
