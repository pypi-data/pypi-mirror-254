from os.path import exists

from docker.errors import ContainerError
from nwon_baseline.typings import AnyDict

from nwon_deployment.docker.handle_docker_package_output import (
    handle_docker_package_output,
)
from nwon_deployment.docker_client import get_docker_client
from nwon_deployment.exceptions.file_missing import FileMissing
from nwon_deployment.print_output import OutputType, TerminalColors, print_output


def handle_docker_run(arguments: AnyDict) -> str:
    """
    A wrapper around docker run from the docker-py package. Meant to handle output
    and catch error messages.
    """

    docker_client = get_docker_client()

    try:
        if "volumes" in arguments and isinstance(arguments["volumes"], dict):
            for path in arguments["volumes"].keys():
                if not exists(path):
                    raise FileMissing(path=path)

        output = docker_client.containers.run(
            stdout=True, stderr=True, stream=True, **arguments
        )

        return handle_docker_package_output(output)

    except ContainerError as error:
        print_output(
            f"status_code: {error.exit_status}, command: {error.command}"
            + f", {error.stderr}",
            output=OutputType.Docker,
            color=TerminalColors.Error,
        )

        raise error


__all__ = [
    "handle_docker_run",
]
