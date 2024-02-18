from typing import List, Optional

from nwon_baseline import unique_list

from nwon_deployment.commands.executor.docker_compose_command import (
    docker_compose_command,
)
from nwon_deployment.print_output import print_output
from nwon_deployment.typings import DockerService


def docker_compose_start(
    service: Optional[DockerService] = None,
    additional_options: Optional[List[str]] = None,
    wait_for_healthy=True,
):
    if service:
        print_output(f"Starting {service.value}")
    else:
        print_output("Starting docker stack")

    if wait_for_healthy:
        command = ["up", "-d", "--wait", "--wait-timeout", "60000"]
    else:
        command = ["up", "-d"]

    if additional_options:
        command = unique_list(command + additional_options)

    if service:
        command.append(service.value)

    docker_compose_command(command)


__all__ = ["docker_compose_start"]
