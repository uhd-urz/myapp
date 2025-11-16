# MyApp

A Rya bootstrapped example application.

## Usage

Clone this repository, `cd` into the project directory, then run `uv --sync`.

```shell
$ git clone https://github.com/uhd-urz/myapp.git ~/myapp
$ cd ~/myapp
$ uv --sync
$ source .venv/bin/activate
```

Done! `myapp` should be installed as an executable within the virtual environment. Run `myapp` and the
`--help` message should be displayed.

## How to change the application name

> [!NOTE]  
> The following steps will be automated in the future.

1. Open `src/myapp/names/names.py`, and update the following Enum class:

```python
class AppIdentity(StrEnum):
    app_name = "<new app name here>"
    app_fancy_name = "<new fancy name here>"
    pypi_name = "<the [project] 'name' from pyproject.toml>"
    log_file_name = f"{app_name}.log"
    config_file_extension = "toml"
    user_config_file_name = f"config.{config_file_extension}"
    project_config_file_name = f"{app_name}.{config_file_extension}"
```

2. Rename the project directory.

```shell
mv src/myapp src/<new app name from AppIdentity>
```

3. Update the executable name in `pyproject.toml`

```toml
[project.scripts]
myapp = "<new app name from AppIdentity>.cli.__main__:app"
```

4. Run `uv --sync` to update the virtual environment metadata. Run `<new app name here>` on the terminal and the
   `--help` message should be displayed like before.
