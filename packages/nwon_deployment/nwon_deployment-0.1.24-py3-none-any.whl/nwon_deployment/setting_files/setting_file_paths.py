from enum import Enum
from os.path import join

from nwon_deployment.settings import get_deployment_package_settings


def deployment_environment_dir_for_environment(environment: Enum):
    settings = get_deployment_package_settings()
    return join(settings.paths.deployment_environment, environment.value)


def path_base_setting_file(environment: Enum):
    settings = get_deployment_package_settings()
    return join(
        deployment_environment_dir_for_environment(environment),
        settings.application_settings.setting_file_name,
    )


def path_settings_override_file(environment: Enum):
    settings = get_deployment_package_settings()
    return join(
        deployment_environment_dir_for_environment(environment),
        settings.application_settings.setting_override_file_name,
    )
