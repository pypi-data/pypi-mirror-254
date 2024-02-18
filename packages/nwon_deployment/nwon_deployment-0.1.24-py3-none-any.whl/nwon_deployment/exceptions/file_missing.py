from nwon_deployment.exceptions.deployment_exception import DeploymentException


class FileMissing(DeploymentException):
    message = "File does not exist"

    def __init__(self, path: str, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Path {path} does not exist"


__all__ = [
    "FileMissing",
]
