from os import environ

from nwon_deployment.helper.running_on_gitlab_ci import running_on_gitlab_ci
from nwon_deployment.settings import get_deployment_package_settings


def set_envs_from_map():
    settings = get_deployment_package_settings()

    for key, value in settings.docker.env_variable_map().items():
        if value is not None:
            environ[key] = str(value)
        elif key in environ and value is None and running_on_gitlab_ci() is False:
            del environ[key]
