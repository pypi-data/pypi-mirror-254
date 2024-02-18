from os import getenv
from typing import List

from nwon_deployment.commands.executor.execute_command import execute_command
from nwon_deployment.environment_variables.set_envs_from_map import set_envs_from_map
from nwon_deployment.exceptions.credentials_missing import CredentialsMissing
from nwon_deployment.settings import get_deployment_package_settings


def docker_compose_command(parameters: List[str]):
    """
    Generic wrapper around docker-compose. Takes care of using the right docker-compose
    files in accordance to the current environment.
    """

    set_envs_from_map()
    settings = get_deployment_package_settings()

    login_command = None
    ci_registry = getenv("CI_REGISTRY")

    if settings.gitlab and settings.gitlab.use_gitlab_container_registry or ci_registry:
        ci_registry_user = getenv("CI_REGISTRY_USER")
        ci_registry_password = getenv("CI_REGISTRY_PASSWORD")

        registry = None
        user_name = None
        password = None
        login_command = None

        if ci_registry and ci_registry_user and ci_registry_password:
            registry = ci_registry
            user_name = ci_registry_user
            password = ci_registry_password
        elif settings.gitlab and settings.gitlab.gitlab_registry_url:
            registry = settings.gitlab.gitlab_registry_url

            if (
                not settings.gitlab
                or not settings.gitlab.user_name
                or not settings.gitlab.api_token
            ):
                raise CredentialsMissing("Gitlab credentials missing in settings")

            user_name = settings.gitlab.user_name
            password = settings.gitlab.api_token

        if registry and user_name and password:
            login_command = " ".join(
                [
                    "docker",
                    "login",
                    registry,
                    "-u",
                    user_name,
                    "-p",
                    password,
                ]
            )

    compose_files = settings.docker.compose_files()
    compose_files_argument = [f"--file {file}" for file in compose_files]

    command_to_execute = " ".join(
        ["docker", "compose", "--verbose", "--project-name", settings.docker.stack_name]
        + compose_files_argument
        + parameters
    )

    execute_command(
        " && ".join([login_command, command_to_execute])
        if login_command
        else command_to_execute
    )
