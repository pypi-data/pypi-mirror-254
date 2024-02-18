from enum import Enum


class DockerHealthStatus(Enum):
    Starting = "starting"
    Healthy = "healthy"
    Unhealthy = "unhealthy"
