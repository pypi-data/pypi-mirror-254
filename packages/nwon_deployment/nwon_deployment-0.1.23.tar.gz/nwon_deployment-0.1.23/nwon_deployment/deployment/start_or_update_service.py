from nwon_baseline.typings import TerminalColors

from nwon_deployment.deployment.start_service import start_service
from nwon_deployment.deployment.zero_downtime_update import zero_downtime_update
from nwon_deployment.docker.container.suitable_container_for_service import (
    suitable_container_for_service,
)
from nwon_deployment.docker.docker_services import docker_services
from nwon_deployment.print_output import OutputType, print_output
from nwon_deployment.typings import DockerService


def start_or_update_service(service: DockerService):
    """
    If we find a container for the service we update it.
    If we don't find any we spin up the service.
    """

    if not service.value in docker_services():
        print_output(
            f"Service {service.value} is not part of selected compose files",
            output=OutputType.Docker,
            color=TerminalColors.Error,
        )
        return

    print_output(
        f"Starting/Updating {service.value}",
        output=OutputType.Docker,
        color=TerminalColors.Green,
    )

    old_container = suitable_container_for_service(service)

    if old_container:
        zero_downtime_update(service)
    else:
        start_service(service)


__all__ = [
    "start_or_update_service",
]
