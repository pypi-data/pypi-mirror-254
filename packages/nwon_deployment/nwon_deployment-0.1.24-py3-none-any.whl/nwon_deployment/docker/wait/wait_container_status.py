from datetime import timedelta
from time import sleep
from typing import List, Optional

from docker.errors import NotFound
from docker.models.containers import Container
from nwon_baseline.date_helper import datetime_now

from nwon_deployment.docker.wait.get_container_status import get_container_status
from nwon_deployment.docker_client import get_docker_client
from nwon_deployment.exceptions import ContainerNotAvailable
from nwon_deployment.print_output import print_output
from nwon_deployment.typings.container_status import ContainerStatus


def wait_container_status(
    container_name: str,
    seconds_to_wait=120,
    status_to_wait: Optional[List[ContainerStatus]] = None,
) -> Container:
    """Basically waits for the container to be running"""

    print_output(f"Waiting for container {container_name} to be accessible")

    if not status_to_wait:
        status_to_wait = [ContainerStatus.Running]

    started = datetime_now()
    container_available = False
    while container_available is False:
        if started + timedelta(seconds=seconds_to_wait) < datetime_now():
            raise ContainerNotAvailable(
                container_name=container_name, seconds_to_wait=seconds_to_wait
            )

        try:
            container: Container = get_docker_client().containers.get(container_name)

            if get_container_status(container).value in [
                s.value for s in status_to_wait
            ]:
                container_available = True
        except NotFound:
            sleep(5)

    return container


__all__ = ["wait_container_status"]
