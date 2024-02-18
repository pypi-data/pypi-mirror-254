from enum import Enum
from os import path

import toml
from mergedeep import merge
from nwon_baseline.typings import AnyDict

from nwon_deployment.setting_files.setting_file_paths import path_settings_override_file
from nwon_deployment.setting_files.setting_overrides_write import (
    setting_overrides_write,
)


def setting_overrides_add_data(settings: AnyDict, environment: Enum):
    """
    Adds data to the setting overrides file and returns path to file.
    """

    setting_override_file = path_settings_override_file(environment)

    if path.exists(setting_override_file):
        with open(setting_override_file, encoding="utf-8") as file:
            setting_overrides = toml.load(file)
    else:
        setting_overrides = {}

    setting_overrides = merge(
        setting_overrides,
        settings,
    )

    return setting_overrides_write(setting_overrides, environment)
