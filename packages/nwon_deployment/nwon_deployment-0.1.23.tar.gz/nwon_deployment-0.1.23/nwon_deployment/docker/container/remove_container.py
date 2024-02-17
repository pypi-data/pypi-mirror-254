from nwon_deployment.print_output import print_output
from nwon_deployment.typings import ContainerInformation, ContainerStatus


def remove_container(container: ContainerInformation):
    if container.status.value == ContainerStatus.Running.value:
        print_output(f"Stopping container {container.container.name}")
        container.container.stop()

    print_output(f"Removing container {container.container.name}")
    container.container.remove()


__all__ = ["remove_container"]
