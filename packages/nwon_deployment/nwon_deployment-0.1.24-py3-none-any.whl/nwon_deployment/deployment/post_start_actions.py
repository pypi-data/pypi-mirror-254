from typing import Optional

from nwon_deployment.typings import DockerService, DockerServiceActionMap


def post_start_actions(
    service: DockerService,
    action_map: Optional[DockerServiceActionMap[DockerService]] = None,
):
    if action_map and service in action_map:
        action_map[service]()
