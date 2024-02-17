from typing import List, Optional

from nwon_deployment.commands.executor.docker_compose_command import (
    docker_compose_command,
)
from nwon_deployment.print_output import print_output
from nwon_deployment.typings import DockerService


def docker_compose_build(
    service: Optional[DockerService] = None,
    additional_options: Optional[List[str]] = None,
):
    if service:
        print_output(f"Building {service.value}")
    else:
        print_output("Building docker stack")

    command = ["build"]

    if additional_options:
        command = command + additional_options

    if service:
        command.append(service.value)

    docker_compose_command(command)


__all__ = ["docker_compose_build"]
