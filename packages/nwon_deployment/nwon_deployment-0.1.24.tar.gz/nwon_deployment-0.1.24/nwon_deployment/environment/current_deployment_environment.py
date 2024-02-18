from enum import Enum

from nwon_deployment.settings import get_deployment_package_settings


def current_deployment_environment() -> Enum:
    settings = get_deployment_package_settings()
    return settings.deployment_environment()
