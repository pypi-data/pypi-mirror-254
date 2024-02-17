import os

from nwon_deployment.helper.prepend_lines_to_file import prepend_lines_to_file
from nwon_deployment.setting_files.lines_to_prepend import (
    lines_to_prepend_setting,
    lines_to_prepend_setting_override,
)
from nwon_deployment.settings import get_deployment_package_settings


def prepend_schemas_to_setting_files():
    settings = get_deployment_package_settings()

    setting_file_name = settings.application_settings.setting_file_name
    setting_override_file_name = (
        settings.application_settings.setting_override_file_name
    )

    for root, _, files in os.walk(settings.paths.deployment_environment):
        for file in files:
            file_path = os.path.join(root, file)

            if setting_file_name in file:
                setting_lines = lines_to_prepend_setting(file_path)
                prepend_lines_to_file(file_path, setting_lines)

            if setting_override_file_name in file:
                setting_overwrite_lines = lines_to_prepend_setting_override(file_path)
                prepend_lines_to_file(file_path, setting_overwrite_lines)
