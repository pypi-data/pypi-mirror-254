from typing import List, Optional

from docker.models.containers import Container

from nwon_deployment.docker.container.container_name_for_service import (
    container_name_for_service,
)
from nwon_deployment.docker.wait.wait_container_status import wait_container_status
from nwon_deployment.typings import ContainerStatus, DockerService


def wait_service_container_status(
    service: DockerService,
    seconds_to_wait=120,
    container_index: int = 1,
    status_to_wait: Optional[List[ContainerStatus]] = None,
) -> Container:
    """Basically waits for the service to be accessible"""

    if not status_to_wait:
        status_to_wait = [ContainerStatus.Running]

    container_name = container_name_for_service(service, container_index)
    return wait_container_status(container_name, seconds_to_wait)
