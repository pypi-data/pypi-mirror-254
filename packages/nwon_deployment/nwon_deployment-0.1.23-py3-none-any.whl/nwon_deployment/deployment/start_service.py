from typing import Optional

from nwon_deployment.commands.docker import docker_compose_start
from nwon_deployment.deployment.post_start_actions import post_start_actions
from nwon_deployment.typings import DockerService, DockerServiceActionMap


def start_service(
    service: DockerService,
    action_map: Optional[DockerServiceActionMap[DockerService]] = None,
):
    docker_compose_start(service, additional_options=["--no-recreate"])
    post_start_actions(service, action_map)


__all__ = [
    "start_service",
]
