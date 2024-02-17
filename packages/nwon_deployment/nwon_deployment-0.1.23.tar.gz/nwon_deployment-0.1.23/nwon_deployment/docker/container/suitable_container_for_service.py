from typing import Optional

from nwon_deployment.docker.container.containers_for_service import (
    containers_for_service,
)
from nwon_deployment.typings import (
    ContainerInformation,
    ContainerStatus,
    DockerHealthStatus,
    DockerService,
)


def suitable_container_for_service(
    service: DockerService,
) -> Optional[ContainerInformation]:
    """
    Loop through potentially available containers and choose the
    best (healthy and newest) one.

    Returns the found container or None
    """

    containers = containers_for_service(service)
    healthy_containers = [
        container
        for container in containers
        if container.health
        and container.health.value == DockerHealthStatus.Healthy.value
    ]

    unhealthy_containers = [
        container
        for container in containers
        if not container.health
        or container.health.value != DockerHealthStatus.Healthy.value
    ]

    if len(healthy_containers) > 0:
        return healthy_containers[-1]

    if len(unhealthy_containers) > 0:
        running = [
            container
            for container in unhealthy_containers
            if container.status.value == ContainerStatus.Running.value
        ]

        return running[-1] if len(running) > 0 else None

    return None


__all__ = ["suitable_container_for_service"]
