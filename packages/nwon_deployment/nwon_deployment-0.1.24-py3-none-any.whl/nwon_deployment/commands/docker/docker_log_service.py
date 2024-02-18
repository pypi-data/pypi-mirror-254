from nwon_deployment.commands.docker.docker_log_container import docker_log_container
from nwon_deployment.docker.wait.wait_service_container_status import (
    wait_service_container_status,
)
from nwon_deployment.print_output import print_output
from nwon_deployment.typings.docker_service import DockerService


def docker_log_service(service: DockerService, container_index: int = 1):
    print_output(f"Logging {service.value} with index {container_index}")

    container = wait_service_container_status(
        service=service, container_index=container_index
    )
    docker_log_container(container)


__all__ = ["docker_log_service"]
