from rya.cli import app
from rya.config import AppConfig
from rya.styles import stdout_console


@app.command(
    name="print-config",
    short_help="An example command that prints the validated configuration.",
)
def print_validated_config():
    """
    Print the validated configuration.
    """
    stdout_console.print("Validated configuration:")
    stdout_console.print(AppConfig.validated)
