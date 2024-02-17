from enum import Enum
from typing import Optional

from nwon_deployment.exceptions.settings_not_set import DeploymentSettingsNotSet
from nwon_deployment.typings.deployment_settings import (
    DeploymentSettings,
    DeploymentSettingsGitlab,
)

__DEPLOYMENT_SETTINGS: Optional[DeploymentSettings[Enum]] = None


def set_deployment_package_settings(
    settings: DeploymentSettings[Enum],
) -> DeploymentSettings[Enum]:
    global __DEPLOYMENT_SETTINGS

    __DEPLOYMENT_SETTINGS = settings

    return __DEPLOYMENT_SETTINGS


def get_deployment_package_settings() -> DeploymentSettings[Enum]:
    global __DEPLOYMENT_SETTINGS

    if __DEPLOYMENT_SETTINGS is None:
        raise DeploymentSettingsNotSet("Deployment settings not set")

    return __DEPLOYMENT_SETTINGS


def get_gitlab_settings() -> Optional[DeploymentSettingsGitlab]:
    global __DEPLOYMENT_SETTINGS

    if __DEPLOYMENT_SETTINGS is None:
        return None

    return __DEPLOYMENT_SETTINGS.gitlab
