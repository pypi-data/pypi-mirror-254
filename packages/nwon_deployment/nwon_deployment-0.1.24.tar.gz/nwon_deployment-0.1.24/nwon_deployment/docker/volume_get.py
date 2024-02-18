from typing import Optional

from docker.errors import NotFound
from docker.models.volumes import Volume

from nwon_deployment.docker_client import get_docker_client


def volume_get(volume_name: str) -> Optional[Volume]:
    docker_client = get_docker_client()

    try:
        volume: Volume = docker_client.volumes.get(volume_name)
        return volume
    except NotFound:
        return None
