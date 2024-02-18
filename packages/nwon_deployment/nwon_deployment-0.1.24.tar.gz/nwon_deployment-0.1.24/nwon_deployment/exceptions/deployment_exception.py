class DeploymentException(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


__all__ = [
    "DeploymentException",
]
