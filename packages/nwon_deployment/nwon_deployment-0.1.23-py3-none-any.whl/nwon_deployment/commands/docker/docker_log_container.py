from docker.models.containers import Container

from nwon_deployment.docker.handle_docker_package_output import (
    handle_docker_package_output,
)


def docker_log_container(container: Container):
    container.attach()
    output = container.logs(tail=100)

    handle_docker_package_output(output)


__all__ = ["docker_log_container"]
