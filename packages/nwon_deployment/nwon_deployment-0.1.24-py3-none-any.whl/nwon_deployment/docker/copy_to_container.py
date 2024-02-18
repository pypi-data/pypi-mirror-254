import os
import tarfile

from docker.models.containers import Container

from nwon_deployment.docker_client import get_docker_client


def copy_to_container(
    container_name: str, src_path: str, path_in_container: str
) -> bool:
    """
    Copy a file to a docker container.
    """

    docker_client = get_docker_client()

    container: Container = docker_client.containers.get(container_name)

    os.chdir(os.path.dirname(src_path))
    src_basename = os.path.basename(src_path)

    with tarfile.open(src_path + ".tar", mode="w") as file:
        tar = file

        try:
            tar.add(src_basename)
        finally:
            tar.close()

    with open(src_path + ".tar", "rb") as file:
        data = file.read()
        response: bool = container.put_archive(os.path.dirname(path_in_container), data)

    return response


__all__ = ["copy_to_container"]
