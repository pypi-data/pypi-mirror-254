from nwon_deployment.exceptions.deployment_exception import DeploymentException


class DeploymentSettingsNotSet(DeploymentException):
    message = "Deployment settings not set"


__all__ = [
    "DeploymentSettingsNotSet",
]
