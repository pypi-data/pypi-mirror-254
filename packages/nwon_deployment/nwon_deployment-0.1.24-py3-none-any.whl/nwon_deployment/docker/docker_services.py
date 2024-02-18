from typing import List, Set

import yaml
from nwon_baseline import unique_list
from nwon_baseline.typings import AnyDict
from yaml.loader import SafeLoader

from nwon_deployment.settings import get_deployment_package_settings
from nwon_deployment.typings.docker_compose import ComposeSpecification


def docker_services() -> Set[str]:
    """
    A list of all services configured in the active docker compose files.
    """

    settings = get_deployment_package_settings()

    services: List[str] = []
    for file in settings.docker.compose_files():
        with open(file, "r", encoding="utf-8") as compose_file:
            yaml_files: List[AnyDict] = list(
                yaml.load_all(compose_file, Loader=SafeLoader)
            )
            for yaml_file in yaml_files:
                compose = ComposeSpecification.model_validate(yaml_file)
                if compose.services:
                    services = services + list(compose.services.keys())

    return unique_list(services)


__all__ = [
    "docker_services",
]
