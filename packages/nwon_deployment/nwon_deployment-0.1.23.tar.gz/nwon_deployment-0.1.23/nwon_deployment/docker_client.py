from os import getenv
from typing import Optional

import docker

__DOCKER_CLIENT: Optional[docker.DockerClient] = None
"""
Class for working with the default docker package.

Documentation: https://docker-py.readthedocs.io/en/stable/api.html
"""

__DOCKER_API_CLIENT: Optional[docker.APIClient] = None
"""
Class for working with the low level Api of the docker package.

Documentation: https://docker-py.readthedocs.io/en/stable/api.html#low-level-api
"""


def set_docker_client(client: docker.DockerClient) -> docker.DockerClient:
    global __DOCKER_CLIENT

    __DOCKER_CLIENT = client

    return __DOCKER_CLIENT


def get_docker_client() -> docker.DockerClient:
    global __DOCKER_CLIENT

    if __DOCKER_CLIENT is None:
        __DOCKER_CLIENT = docker.DockerClient(base_url="unix://var/run/docker.sock")
        __login_to_ci()

    return __DOCKER_CLIENT


def set_docker_api_client(client: docker.APIClient) -> docker.APIClient:
    global __DOCKER_API_CLIENT

    __DOCKER_API_CLIENT = client

    return __DOCKER_API_CLIENT


def get_docker_api_client() -> docker.APIClient:
    global __DOCKER_API_CLIENT

    if __DOCKER_API_CLIENT is None:
        __DOCKER_API_CLIENT = docker.APIClient(base_url="unix://var/run/docker.sock")
        __login_to_ci()

    return __DOCKER_API_CLIENT


def __login_to_ci():
    ci_registry = getenv("CI_REGISTRY")
    ci_registry_user = getenv("CI_REGISTRY_USER")
    ci_registry_password = getenv("CI_REGISTRY_PASSWORD")

    if ci_registry and ci_registry_user and ci_registry_password:
        if __DOCKER_CLIENT:
            __DOCKER_CLIENT.login(
                registry=ci_registry,
                username=ci_registry_user,
                password=ci_registry_password,
            )

        if __DOCKER_API_CLIENT:
            __DOCKER_API_CLIENT.login(
                registry=ci_registry,
                username=ci_registry_user,
                password=ci_registry_password,
            )
