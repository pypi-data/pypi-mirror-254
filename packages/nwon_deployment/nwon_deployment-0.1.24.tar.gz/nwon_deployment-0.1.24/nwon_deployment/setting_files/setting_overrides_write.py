from enum import Enum

import toml
from nwon_baseline.typings import AnyDict

from nwon_deployment.helper.prepend_lines_to_file import prepend_lines_to_file
from nwon_deployment.setting_files.application_setting_schemas import dump_schemas
from nwon_deployment.setting_files.lines_to_prepend import (
    lines_to_prepend_setting_override,
)
from nwon_deployment.setting_files.setting_file_paths import path_settings_override_file


def setting_overrides_write(settings: AnyDict, environment: Enum):
    """
    Write settings to the settings override file and returns path to file.

    Overwrites all previous settings!!!
    """

    dump_schemas()
    setting_override_file = path_settings_override_file(environment)

    with open(setting_override_file, "w+", encoding="utf-8") as setting_file:
        toml.dump(settings, setting_file)

    prepend_lines_to_file(
        setting_override_file, lines_to_prepend_setting_override(setting_override_file)
    )
    return setting_override_file
