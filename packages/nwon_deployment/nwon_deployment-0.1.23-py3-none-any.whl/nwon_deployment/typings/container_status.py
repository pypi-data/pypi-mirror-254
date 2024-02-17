from enum import Enum


class ContainerStatus(Enum):
    Created = "created"
    Restarting = "restarting"
    Running = "running"
    Paused = "paused"
    Exited = "exited"
    Removing = "removing"
