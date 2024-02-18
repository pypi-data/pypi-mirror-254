from datetime import timedelta
from time import sleep
from typing import List, Optional

from docker.models.containers import Container
from nwon_baseline.date_helper import datetime_now

from nwon_deployment.commands.docker.docker_log_container import docker_log_container
from nwon_deployment.docker.wait.get_container_health import get_container_health
from nwon_deployment.exceptions import ContainerNotHealthy
from nwon_deployment.print_output import print_output
from nwon_deployment.typings import DockerHealthStatus


def wait_container_health_status(
    container: Container,
    status_to_wait_for: Optional[List[DockerHealthStatus]] = None,
    seconds_to_wait=120,
):
    """
    Waits for a certain amount of minutes until a container is healthy
    """
    started = datetime_now()

    if status_to_wait_for is None:
        status_to_wait_for = [DockerHealthStatus.Healthy]

    print_output(f"Waiting for container {container.name} to be healthy")

    container_health = get_container_health(container)

    if container_health is None:
        return

    health_status = container_health

    while health_status.value not in [status.value for status in status_to_wait_for]:
        sleep(2)

        if started + timedelta(seconds=seconds_to_wait) < datetime_now():
            docker_log_container(container)
            raise ContainerNotHealthy(
                container_name=container.name, seconds_to_wait=seconds_to_wait
            )

        container_health = get_container_health(container)
        if container_health is None:
            return

        health_status = container_health


__all__ = ["wait_container_health_status"]
