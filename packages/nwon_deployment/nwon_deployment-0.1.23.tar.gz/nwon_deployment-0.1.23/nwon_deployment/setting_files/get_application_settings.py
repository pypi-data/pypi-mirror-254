from enum import Enum
from os import getenv
from os.path import exists
from typing import Any

from mergedeep import merge
from pydantic import BaseModel

from nwon_deployment.environment.current_deployment_environment import (
    current_deployment_environment,
)
from nwon_deployment.exceptions.setting_file_do_not_exist import SettingFileDoNotExist
from nwon_deployment.print_output import OutputType, print_output
from nwon_deployment.setting_files.create_setting_override_file import (
    create_setting_override_file,
)
from nwon_deployment.setting_files.load_settings_from_file import (
    load_settings_from_file,
)
from nwon_deployment.setting_files.setting_file_paths import (
    path_base_setting_file,
    path_settings_override_file,
)
from nwon_deployment.settings import get_deployment_package_settings


def get_application_settings() -> BaseModel:
    """
    Get deployment settings.

    Settings are defined via a settings.toml file in the directory of the deployment
    environment. On top all settings can be overridden using a settings.override.toml
    file in the same directory.
    """

    environment = current_deployment_environment()
    return get_application_settings_for_environment(environment)


def get_application_settings_for_environment(environment: Enum) -> BaseModel:
    """
    Get deployment settings for a specific environment.

    Settings are defined via a settings.toml file in the directory of the deployment
    environment. On top all settings can be overridden using a settings.override.toml
    file in the same directory.
    """

    setting_file = path_base_setting_file(environment)
    setting_override_file = path_settings_override_file(environment)

    if not exists(setting_override_file):
        create_setting_override_file(environment)

    if not exists(setting_file):
        raise SettingFileDoNotExist(
            f"Base setting file for environment {str(environment)} "
            f"does not exist in {setting_file}"
        )

    settings = load_settings_from_file(setting_file)

    if exists(setting_override_file):
        user_settings = load_settings_from_file(setting_override_file)
        settings = merge(settings, user_settings)

    deployment_package_settings = get_deployment_package_settings()

    parsed_application_settings = (
        deployment_package_settings.application_settings.settings.model_validate(
            settings
        )
    )

    return __apply_environment_variables(parsed_application_settings)


def __apply_environment_variables(
    settings: BaseModel,
) -> BaseModel:
    """
    Apply environment variables to settings.

    Environment variables can be defined for overriding settings. They must start
    with the defined prefix and each layer is separated by a double underscore. The
    whole variable name must be upper case.
    """

    package_settings = get_deployment_package_settings()
    prefix = package_settings.application_settings.environment_variable_prefix

    def recursive_update(obj: BaseModel, path: str = ""):
        for key, _ in obj.model_fields.items():
            new_path = f"{path}__{key}".lstrip("__").upper()

            # If value is another pydantic model check recursively
            value: Any = None
            if hasattr(obj, key):
                value = getattr(obj, key)

            if isinstance(value, BaseModel):
                recursive_update(value, new_path)
                continue

            # Check if environment variable is set
            environment_variable_name = f"{prefix}__{new_path}"
            env_value = getenv(environment_variable_name)

            print_output(
                f"Checking environment variable {environment_variable_name} "
                + "for overriding setting",
                OutputType.Debug,
            )

            # If environment variable is set override setting
            if env_value is not None:
                print_output(
                    f"Overriding setting {new_path} with value {env_value} "
                    + "from environment variable",
                    OutputType.Information,
                )
                setattr(obj, key, env_value)

    recursive_update(settings)
    return settings
