from nwon_deployment.exceptions.deployment_exception import DeploymentException


class CredentialsMissing(DeploymentException):
    message = "Credentials missing"


__all__ = [
    "CredentialsMissing",
]
