from typing import List

from nwon_deployment.commands.executor.docker_compose_command import (
    docker_compose_command,
)
from nwon_deployment.typings import DockerService


def docker_compose_exec(
    options: List[str],
    service: DockerService,
    command: str,
    interactive=False,
):
    """
    Execute a docker compose command

    Refer to https://docs.docker.com/engine/reference/commandline/compose_exec/
    """

    if not interactive:
        options = ["-T"] + options

    command_to_execute = ["exec"] + options + [service.value] + [command]
    docker_compose_command(command_to_execute)
