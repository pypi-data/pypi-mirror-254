from os.path import dirname, relpath
from pathlib import Path
from typing import Dict, Optional

from docker import APIClient, DockerClient
from docker.errors import ImageNotFound
from docker.models.images import Image

from nwon_deployment.docker.handle_docker_package_output import (
    handle_docker_package_output,
)
from nwon_deployment.docker_client import get_docker_api_client, get_docker_client
from nwon_deployment.print_output import print_output


def get_docker_image(
    path_to_docker_file: str,
    image_name: str,
    build_args: Optional[Dict[str, str]] = None,
    custom_context: Optional[str] = None,
    force_rebuild: bool = False,
):
    """
    Wrapper around getting a docker image via Docker package.
    """

    print_output(f"Getting docker image {image_name}")

    docker_client = get_docker_client()
    docker_api_client = get_docker_api_client()

    try:
        if force_rebuild:
            return __build_image(
                path_to_docker_file=path_to_docker_file,
                image_name=image_name,
                build_args=build_args,
                custom_context=custom_context,
                force_rebuild=force_rebuild,
                docker_api_client=docker_api_client,
                docker_client=docker_client,
            )

        image = docker_client.images.get(image_name)

        print_output(f"Image {image_name} found")

        return image
    except ImageNotFound:
        print_output(f"Image {image_name} not found")
        return __build_image(
            path_to_docker_file=path_to_docker_file,
            image_name=image_name,
            build_args=build_args,
            custom_context=custom_context,
            force_rebuild=force_rebuild,
            docker_api_client=docker_api_client,
            docker_client=docker_client,
        )


def __build_image(
    path_to_docker_file: str,
    image_name: str,
    docker_client: DockerClient,
    docker_api_client: APIClient,
    build_args: Optional[Dict[str, str]] = None,
    custom_context: Optional[str] = None,
    force_rebuild: bool = False,
):
    print_output(f"Building docker image {image_name}")

    context = custom_context if custom_context else dirname(path_to_docker_file)

    output = docker_api_client.build(
        dockerfile=relpath(
            Path(path_to_docker_file),
            start=Path(context),
        ),
        path=context,
        buildargs=build_args,
        tag=image_name,
        nocache=force_rebuild,
    )

    handle_docker_package_output(output)

    image: Image = docker_client.images.get(image_name)
    return image
