from docker.models.volumes import Volume

from nwon_deployment.docker_client import get_docker_client


def volume_remove(volume_name: str) -> Volume:
    docker_client = get_docker_client()

    database_volume: Volume = docker_client.volumes.get(volume_name)
    database_volume.remove()

    return database_volume
