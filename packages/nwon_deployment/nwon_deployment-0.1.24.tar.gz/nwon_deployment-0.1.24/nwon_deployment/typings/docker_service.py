from enum import Enum
from typing import Any, Callable, Dict, TypeVar

DockerService = TypeVar("DockerService", bound=Enum)

DockerServiceActionMap = Dict[DockerService, Callable[..., Any]]
