from enum import Enum
from typing import List, TypeVar

from nwon_deployment.commands.executor.docker_compose_exec import docker_compose_exec
from nwon_deployment.docker.container.suitable_container_for_service import (
    suitable_container_for_service,
)
from nwon_deployment.exceptions.container_for_service_not_available import (
    ContainerForServiceNotAvailable,
)
from nwon_deployment.settings import get_deployment_package_settings

DockerService = TypeVar("DockerService", bound=Enum)


def run_on_container(service: DockerService, command: str):
    suitable_container = suitable_container_for_service(service)

    if not suitable_container:
        raise ContainerForServiceNotAvailable(service)

    settings = get_deployment_package_settings()

    if service in settings.docker.default_command_for_container:
        default_command = settings.docker.default_command_for_container[service]
    else:
        default_command = "bash"

    options: List[str] = ["--index", str(suitable_container.index)]

    settings = get_deployment_package_settings()

    if service in settings.docker.user_for_container:
        options.append(f"--user {settings.docker.user_for_container[service]}")

    compose_command: str = command if command else default_command

    docker_compose_exec(options=options, service=service, command=compose_command)
