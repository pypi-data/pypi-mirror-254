import os
import warnings
from pathlib import Path

import yaml
from donfig import Config

new_user_config_dir = Path("~/.config/arraylake").expanduser()


def handle_rename():
    old_env_var = os.getenv("ARRAYLAKE_CLIENT_CONFIG", None)
    new_env_var = os.getenv("ARRAYLAKE_CONFIG", None)
    new_user_config_file = new_user_config_dir / "config.yaml"
    old_user_config_dir = Path("~/.config/arraylake_client").expanduser()
    old_user_config_file = old_user_config_dir / "config.yaml"

    if old_env_var:
        if new_env_var:
            warnings.warn(
                "Using ARRAYLAKE_CONFIG instead of ARRAYLAKE_CLIENT_CONFIG when both are set. "
                "Unset ARRAYLAKE_CLIENT_CONFIG to silence this warning.",
                UserWarning,
                stacklevel=2,
            )
        else:
            raise ValueError(
                "The ARRAYLAKE_CLIENT_CONFIG environment variable has been renamed to ARRAYLAKE_CONFIG. "
                "ARRAYLAKE_CLIENT_CONFIG is being ignored.",
            )

    if not new_env_var and old_user_config_file.exists():
        if new_user_config_file.exists():
            warnings.warn(
                f"Preferentially reading {new_user_config_file} over {old_user_config_file}."
                f" To silence this warning, delete the {old_user_config_dir} directory.",
                UserWarning,
                stacklevel=2,
            )
        else:
            import shutil

            new_user_config_dir.mkdir(exist_ok=True)
            shutil.move(str(old_user_config_file), new_user_config_file)

            warnings.warn(
                f"Migrated {old_user_config_file} to {new_user_config_file}. ",
                UserWarning,
                stacklevel=2,
            )

    old_vars = [k for k in os.environ if k.startswith("ARRAYLAKE_CLIENT") and k != "ARRAYLAKE_CLIENT_CONFIG"]
    if old_vars:
        raise ValueError(
            "Detected old configuration enviroment variables. "
            "Please rename the following from `ARRAYLAKE_CLIENT_*` to `ARRAYLAKE_*`. \n"
            f"{' '.join(old_vars)}",
        )


handle_rename()

user_config_dir = Path(os.getenv("ARRAYLAKE_CONFIG", new_user_config_dir)).expanduser()
user_config_file = user_config_dir / "config.yaml"

fn = Path(__file__).resolve().parent / "config.yaml"
with fn.open() as f:
    defaults = yaml.safe_load(f)
config = Config("arraylake", paths=[user_config_dir], defaults=[defaults])

# maybe move a copy of the defaults to the user config space
config.ensure_file(
    source=fn,
    comment=True,
)
