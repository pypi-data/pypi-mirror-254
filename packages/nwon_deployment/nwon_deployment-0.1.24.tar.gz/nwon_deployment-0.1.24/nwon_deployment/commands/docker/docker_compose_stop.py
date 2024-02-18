from typing import List, Optional

from nwon_deployment.commands.executor.docker_compose_command import (
    docker_compose_command,
)
from nwon_deployment.print_output import print_output
from nwon_deployment.typings import DockerService


def docker_compose_stop(
    service: Optional[DockerService] = None,
    additional_arguments: Optional[List[str]] = None,
):
    if service:
        print_output(f"Stopping {service.value}")
    else:
        print_output("Stopping docker stack")

    command = ["down"]

    if service is not None:
        command.append(service.value)

    if additional_arguments:
        command = command + additional_arguments

    docker_compose_command(command)


__all__ = ["docker_compose_stop"]
