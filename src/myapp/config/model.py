from functools import partial

from pydantic import BaseModel
from rya.config import ConfigMaker
from rya.styles import update_rich_click_cli_theme

from ..names import run_early_list


class RichClickTheme(BaseModel):
    theme: str = "quartz2-modern"


class ConfigModel(BaseModel):
    """An example configuration model"""

    foo: str = "foo"
    styles: RichClickTheme = RichClickTheme()


# Add model registers the model to Rya
ConfigMaker.add_model(ConfigModel)
run_early_list.append(
    partial(
        update_rich_click_cli_theme,
        config_field_loc="styles.theme",
        default_theme=RichClickTheme.model_fields.get("theme").default,
    )
)
