from nwon_deployment.exceptions.deployment_exception import DeploymentException


class ContainerNotHealthy(DeploymentException):
    message = "Container did not turn healthy"

    def __init__(
        self, container_name: str, seconds_to_wait: int, *args: object
    ) -> None:
        super().__init__(*args)
        self.message = (
            f"Container {container_name} did not turn "
            + f"healthy within {seconds_to_wait} minutes"
        )


__all__ = [
    "ContainerNotHealthy",
]
