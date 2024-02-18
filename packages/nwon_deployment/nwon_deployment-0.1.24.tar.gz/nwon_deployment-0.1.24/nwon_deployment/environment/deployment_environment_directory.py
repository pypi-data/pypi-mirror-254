from enum import Enum
from os.path import join

from nwon_deployment.settings import get_deployment_package_settings


def deployment_environment_directory() -> str:
    settings = get_deployment_package_settings()
    environment: Enum = settings.deployment_environment()
    return deployment_environment_dir_for_environment(environment)


def deployment_environment_dir_for_environment(environment: Enum):
    settings = get_deployment_package_settings()
    return join(settings.paths.deployment_environment, environment.value)
