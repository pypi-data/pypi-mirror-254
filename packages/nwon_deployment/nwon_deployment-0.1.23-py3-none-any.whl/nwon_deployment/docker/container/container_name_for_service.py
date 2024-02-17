from nwon_deployment.settings import get_deployment_package_settings
from nwon_deployment.typings import DockerService


def container_name_for_service(service: DockerService, index: int = 1):
    return get_deployment_package_settings().docker.container_name(service, index)


__all__ = ["container_name_for_service"]
