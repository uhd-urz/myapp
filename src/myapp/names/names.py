from collections import UserList
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Optional

from properpath import P
from pydantic import BaseModel
from rya.pre_utils import (
    ConfigFileTuple,
    DefaultLoggerName,
    FileTupleContainer,
    LogFileTuple,
    is_platform_unix,
)


class AppIdentity(StrEnum):
    app_name = "myapp"
    app_fancy_name = "MyApp"
    log_file_name = f"{app_name}.log"
    config_file_extension = "toml"
    user_config_file_name = f"config.{config_file_extension}"
    project_config_file_name = f"{app_name}.{config_file_extension}"
    version_file_name = "VERSION"


DefaultLoggerName.name = AppIdentity.app_name

app_dirs = P.platformdirs(
    appname=AppIdentity.app_name,
    appauthor=AppIdentity.app_name,
    ensure_exists=True,
    follow_unix=True,
)

# Configuration file path definitions
config_file_sources: UserList[ConfigFileTuple]
config_file_sources = FileTupleContainer()
if is_platform_unix():
    config_file_sources.append(
        ConfigFileTuple(
            path=(P("/etc") / AppIdentity.app_name / AppIdentity.user_config_file_name),
            name="system config",
        ),
    )
config_file_sources.append(
    ConfigFileTuple(
        path=app_dirs.user_config_dir / AppIdentity.user_config_file_name,
        name="user config",
        init_cmd_default=True,
    )
)
config_file_sources.append(
    ConfigFileTuple(
        path=P.cwd() / AppIdentity.project_config_file_name,
        name="project config",
    )
)

# Log file path definitions
log_file_sinks: UserList[LogFileTuple]
log_file_sinks = FileTupleContainer()
if is_platform_unix():
    log_file_sinks.append(
        LogFileTuple(
            path=(P("/var/log") / AppIdentity.app_name / AppIdentity.log_file_name),
            name="system log",
        )
    )
log_file_sinks.append(
    LogFileTuple(
        path=app_dirs.user_log_dir / AppIdentity.log_file_name,
        name="user log",
    )
)


# Cache file definitions
class CacheModel(BaseModel):
    date: datetime
    log_file_path: Optional[P] = None


@dataclass(frozen=True)
class CacheFileProperties:
    expires_in_days = 30
    encoding = "utf-8"
    indent = 4


cache_path: P = app_dirs.user_cache_dir / f"{AppIdentity.app_name}.json"
