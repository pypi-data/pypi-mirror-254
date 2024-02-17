from typing import Optional

from docker.models.containers import Container

from nwon_deployment.typings.container_status import ContainerStatus
from nwon_deployment.typings.deployment_base_model import DeploymentBaseModel
from nwon_deployment.typings.docker_health_status import DockerHealthStatus


class ContainerInformation(DeploymentBaseModel):
    container: Container
    index: int
    health: Optional[DockerHealthStatus]
    status: ContainerStatus
    name: str

    class Config:
        arbitrary_types_allowed = True
