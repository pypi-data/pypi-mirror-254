from enum import Enum

from nwon_deployment.exceptions.deployment_exception import DeploymentException


class ServiceNotInContainerNameMapping(DeploymentException):
    message = "Service not in container name mapping"

    def __init__(self, service: Enum, *args: object) -> None:
        super().__init__(*args)
        self.message = f"{service.value} not in service to container name mapping"


__all__ = [
    "ServiceNotInContainerNameMapping",
]
