from enum import Enum
from typing import Callable, Dict, Generic, List, Optional, Set, Type, TypeVar, Union

from pydantic import BaseModel, Field

from nwon_deployment.typings.deployment_base_model import DeploymentBaseModel
from nwon_deployment.typings.env_variable_map import EnvVariableMap

Service = TypeVar("Service", bound=Enum)
Environment = TypeVar("Environment", bound=Enum)


class DeploymentSettingsGitlab(DeploymentBaseModel):
    use_gitlab_container_registry: bool
    user_name: Optional[str] = None
    password: Optional[str] = None
    api_token: Optional[str] = None
    gitlab_registry_url: Optional[str] = None


class DeploymentSettingsPaths(DeploymentBaseModel):
    deployment_scripts_base: str = Field(
        description="Path where the deployment scripts live"
    )
    deployment_environment: str = Field(
        description="Path for all the deployment environments. We assume that there "
        + "is a folder for each environment that will contain at "
        + "least the setting toml files."
    )


class DeploymentSettingsDocker(DeploymentBaseModel, Generic[Service]):
    stack_name: str = Field(description="Name of the docker stack")
    container_name: Callable[[Service, int], str] = Field(
        description="Function that returns the container name for a service"
    )
    user_for_container: Dict[Service, str] = Field(
        description="Map of container names and the default user for that container"
    )
    default_command_for_container: Dict[Service, str] = Field(
        description="Map of container names and their default command"
    )
    env_variable_map: Callable[[], EnvVariableMap] = Field(
        description="Map of environment variables that will be exposed before calling "
        + "docker compose commands"
    )
    compose_files: Callable[..., Union[Set[str], List[str]]] = Field(
        description="Function that returns paths to the compose files for "
        + "the given environment"
    )


class DeploymentSettingsApplicationSettings(DeploymentBaseModel):
    settings: Type[BaseModel] = Field(
        description="Pydantic model for the application settings"
    )
    lines_to_prepend_to_settings_override: List[str] = Field(
        description="List of lines that will be prepended to the settings "
        + "override files"
    )
    lines_to_prepend_to_settings: List[str] = Field(
        description="List of lines that will be prepended to the setting files"
    )
    setting_file_name: str = "settings.toml"
    setting_override_file_name: str = "settings.override.toml"
    optional_json_schema_file_name: str = "settings-optional.schema.json"
    json_schema_file_name: str = "settings.schema.json"
    environment_variable_prefix: str = Field(
        "NWON",
        description="Prefix for environment variables that are used for "
        + "overriding settings",
    )


class DeploymentSettings(BaseModel, Generic[Service]):
    deployment_environment: Callable[[], Environment] = Field(
        description="Function that returns the deployment environment"
    )
    deployment_base_environment: Callable[[Environment], Environment] = Field(
        description="Deployment environments can base upon one another. This function "
        + "returns the base environment for given environment"
    )
    gitlab: Optional[DeploymentSettingsGitlab] = None
    paths: DeploymentSettingsPaths
    docker: DeploymentSettingsDocker[Service]
    application_settings: DeploymentSettingsApplicationSettings


__all__ = [
    "DeploymentSettingsGitlab",
    "DeploymentSettings",
    "DeploymentSettingsDocker",
    "DeploymentSettingsPaths",
    "DeploymentSettingsApplicationSettings",
]
