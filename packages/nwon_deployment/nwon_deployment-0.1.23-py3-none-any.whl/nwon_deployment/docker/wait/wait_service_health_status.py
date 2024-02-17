from enum import Enum
from typing import List, Optional, TypeVar

from docker.models.containers import Container

from nwon_deployment.docker.container.container_name_for_service import (
    container_name_for_service,
)
from nwon_deployment.docker.wait.wait_container_health_status import (
    wait_container_health_status,
)
from nwon_deployment.docker.wait.wait_container_status import wait_container_status
from nwon_deployment.typings import DockerHealthStatus

DockerService = TypeVar("DockerService", bound=Enum)


def wait_service_health_status(
    service: DockerService,
    status_to_wait_for: Optional[List[DockerHealthStatus]] = None,
    seconds_to_wait=120,
    container_index: int = 1,
) -> Container:
    """Basically waits for the service to be in a certain health status"""

    if status_to_wait_for is None:
        status_to_wait_for = [DockerHealthStatus.Healthy]

    container_name = container_name_for_service(service, container_index)

    container = wait_container_status(container_name)
    return wait_container_health_status(
        container=container,
        seconds_to_wait=seconds_to_wait,
        status_to_wait_for=status_to_wait_for,
    )


__all__ = ["wait_service_health_status"]
