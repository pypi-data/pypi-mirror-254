from docker.models.containers import Container

from nwon_deployment.typings import ContainerStatus


def get_container_status(container: Container) -> ContainerStatus:
    container.reload()

    return ContainerStatus(container.attrs["State"]["Status"])


__all__ = ["get_container_status"]
