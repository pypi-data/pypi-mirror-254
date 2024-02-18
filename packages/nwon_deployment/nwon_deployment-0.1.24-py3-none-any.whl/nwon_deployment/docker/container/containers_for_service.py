from typing import List, Optional

from nwon_deployment.docker.wait.get_container_health import get_container_health
from nwon_deployment.docker.wait.get_container_status import get_container_status
from nwon_deployment.docker_client import get_docker_client
from nwon_deployment.print_output import OutputType, print_output
from nwon_deployment.typings import ContainerInformation, ContainerStatus, DockerService


def containers_for_service(service: DockerService) -> List[ContainerInformation]:
    """
    Returns all containers for a service
    """

    print_output(
        f"Looking for containers for {service.value}", output=OutputType.Docker
    )

    identify_service_by = f"-{service.value}-"

    containers = get_docker_client().containers.list()
    containers = [
        container for container in containers if identify_service_by in container.name
    ]

    containers_information = [
        ContainerInformation(
            container=container,
            name=container.name,
            index=int(container.name.split(identify_service_by)[1]),
            health=get_container_health(container)
            if get_container_status(container).value
            in [ContainerStatus.Restarting.value, ContainerStatus.Running.value]
            else None,
            status=get_container_status(container),
        )
        for container in containers
    ]

    sorted_containers = sorted(containers_information, key=lambda x: x.index)

    print_output(
        f"Found containers {[info.dict() for info in sorted_containers]}",
        output=OutputType.Docker,
    )

    return sorted_containers


def max_service_index(service: DockerService) -> Optional[int]:
    """
    Returns the last known index of a container for the service
    """

    containers = containers_for_service(service)

    if len(containers) < 1:
        return None

    max_index = max(containers, key=lambda x: x.index)
    return max_index.index


__all__ = ["max_service_index", "containers_for_service"]
