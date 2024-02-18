from enum import Enum
from os import getenv
from typing import Dict, Optional

from nwon_baseline import print_helper
from nwon_baseline.typings import TerminalColors

from nwon_deployment.typings.deployment_base_model import DeploymentBaseModel


class OutputType(Enum):
    Docker = "docker"
    Debug = "debug"
    Information = "information"
    Command = "information"


class DeploymentPrintSetting(DeploymentBaseModel):
    debug: bool
    command: bool
    docker: bool
    information: bool


COLOR_MAP: Dict[OutputType, TerminalColors] = {
    OutputType.Docker: TerminalColors.Default,
    OutputType.Debug: TerminalColors.Cyan,
    OutputType.Information: TerminalColors.Blue,
    OutputType.Command: TerminalColors.Default,
}


def print_output(
    text: str,
    output: OutputType = OutputType.Information,
    color: Optional[TerminalColors] = None,
    print_settings: Optional[DeploymentPrintSetting] = None,
):
    if print_settings is None:
        print_settings = DeploymentPrintSetting(
            debug=True,
            command=True,
            docker=True,
            information=True,
        )

    if color is None:
        color_to_use = COLOR_MAP.get(output, TerminalColors.Default)
    else:
        color_to_use = color

    if getenv("RESOLVIO_DEBUG"):
        print_helper.print_color(text, color_to_use)
        return

    if output.value == OutputType.Debug.value and not print_settings.debug:
        return

    if output.value == OutputType.Command.value and not print_settings.command:
        return

    if output.value == OutputType.Information.value and not print_settings.information:
        return

    if output.value == OutputType.Docker.value and not print_settings.docker:
        return

    print_helper.print_color(text, color_to_use)


__all__ = ["print_output", "TerminalColors", "OutputType", "DeploymentPrintSetting"]
