from enum import Enum
from os.path import exists

from nwon_deployment.setting_files.setting_file_paths import path_settings_override_file


def create_setting_override_file(environment: Enum):
    setting_override_file = path_settings_override_file(environment)
    if not exists(setting_override_file):
        with open(setting_override_file, "w", encoding="utf-8") as _:
            pass

    return setting_override_file
