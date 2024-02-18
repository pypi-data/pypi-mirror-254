from typing import Optional

from docker.models.containers import Container

from nwon_deployment.typings import DockerHealthStatus


def get_container_health(container: Container) -> Optional[DockerHealthStatus]:
    container.reload()

    return (
        DockerHealthStatus(container.attrs["State"]["Health"]["Status"])
        if "Health" in container.attrs["State"]
        else None
    )


__all__ = ["get_container_health"]
