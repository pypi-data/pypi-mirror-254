from nwon_deployment.exceptions.deployment_exception import DeploymentException
from nwon_deployment.typings.docker_service import DockerService


class ContainerForServiceNotAvailable(DeploymentException):
    message = "Container is not available"

    def __init__(
        self,
        service: DockerService,
        *args: object,
    ) -> None:
        super().__init__(*args)
        self.message = f"Container for service {service.value} is not available "


__all__ = ["ContainerForServiceNotAvailable"]
