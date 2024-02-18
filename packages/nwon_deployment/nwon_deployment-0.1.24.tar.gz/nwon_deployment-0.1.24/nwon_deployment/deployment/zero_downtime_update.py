from nwon_baseline.typings import TerminalColors

from nwon_deployment.commands.docker import docker_compose_start
from nwon_deployment.deployment.post_start_actions import post_start_actions
from nwon_deployment.docker.container.containers_for_service import (
    containers_for_service,
)
from nwon_deployment.docker.container.remove_container import remove_container
from nwon_deployment.docker.wait.wait_container_health_status import (
    wait_container_health_status,
)
from nwon_deployment.docker.wait.wait_container_status import wait_container_status
from nwon_deployment.print_output import OutputType, print_output
from nwon_deployment.typings import DockerHealthStatus, DockerService


def zero_downtime_update(service: DockerService):
    print_output(
        f"Starting second instance of {service.value}",
        output=OutputType.Docker,
    )

    # Remove unhealthy existing container
    for container in [
        c
        for c in containers_for_service(service)
        if c.health and c.health.value != DockerHealthStatus.Healthy.value
    ]:
        remove_container(container)

    docker_compose_start(service, ["--scale", f"{service.value}=2"])

    containers = containers_for_service(service)
    new_container = containers[-1:][0]

    new_container = wait_container_status(new_container.container.name)

    post_start_actions(service)

    wait_container_health_status(new_container, [DockerHealthStatus.Healthy])

    old_containers = [c for c in containers if c.container.name != new_container.name]
    print_output(
        f"Stopping old containers: {[','.join([c.name for c in old_containers])]} 🪦",
        output=OutputType.Docker,
    )

    for container in old_containers:
        remove_container(container)

    print_output(
        "Deployment successful 🥳",
        output=OutputType.Docker,
        color=TerminalColors.Success,
    )


__all__ = [
    "zero_downtime_update",
]
