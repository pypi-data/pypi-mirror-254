from typing import List, Optional

from nwon_baseline import unique_list

from nwon_deployment.commands.executor.docker_compose_command import (
    docker_compose_command,
)
from nwon_deployment.print_output import print_output
from nwon_deployment.typings import DockerService


def docker_compose_restart(
    service: Optional[DockerService] = None,
    additional_options: Optional[List[str]] = None,
):
    if service:
        print_output(f"Restarting {service.value}")
    else:
        print_output("Restarting docker stack")

    command = ["up", "-d", "--wait", "--wait-timeout", "60000", "--force-recreate"]

    if additional_options:
        command = unique_list(command + additional_options)

    if service:
        command.append(service.value)

    docker_compose_command(command)


__all__ = ["docker_compose_restart"]
