from nwon_deployment.exceptions.deployment_exception import DeploymentException


class ContainerNotAvailable(DeploymentException):
    message = "Container is not available"

    def __init__(
        self, container_name: str, seconds_to_wait: int, *args: object
    ) -> None:
        super().__init__(*args)
        self.message = (
            f"Container {container_name} is not available "
            + f"within {seconds_to_wait} seconds"
        )


__all__ = [
    "ContainerNotAvailable",
]
