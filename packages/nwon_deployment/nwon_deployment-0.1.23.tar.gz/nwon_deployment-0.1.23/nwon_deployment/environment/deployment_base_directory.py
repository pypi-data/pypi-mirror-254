from os.path import join

from nwon_deployment.environment.current_deployment_environment import (
    current_deployment_environment,
)
from nwon_deployment.settings import get_deployment_package_settings


def deployment_base_directory():
    settings = get_deployment_package_settings()
    environment = current_deployment_environment()
    base_environment = settings.deployment_base_environment(environment)

    return join(settings.paths.deployment_environment, base_environment.value)
