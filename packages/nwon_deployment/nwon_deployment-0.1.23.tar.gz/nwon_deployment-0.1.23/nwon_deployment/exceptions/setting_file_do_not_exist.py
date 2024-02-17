from nwon_deployment.exceptions.deployment_exception import DeploymentException


class SettingFileDoNotExist(DeploymentException):
    message = "Setting file does not exist"


__all__ = [
    "SettingFileDoNotExist",
]
