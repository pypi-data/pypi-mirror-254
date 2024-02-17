import subprocess
import sys
from typing import Dict, Optional

from nwon_deployment.print_output import OutputType, TerminalColors, print_output


def execute_command(
    command: str,
    environment_to_pass: Optional[Dict[str, str]] = None,
    should_hide_successful_stdout=False,
    cwd: Optional[str] = None,
):
    print_output(f"Executing command: \n{command}", output=OutputType.Debug)

    def log_output(res, is_error):
        should_hide_output = should_hide_successful_stdout and not is_error

        if res.stdout and res.stdout != "" and not should_hide_output:
            print_output(
                res.stdout,
                output=OutputType.Command,
                color=TerminalColors.Default,
            )

        if res.stderr and res.stderr != "":
            print_output(
                res.stderr,
                output=OutputType.Command,
                color=TerminalColors.Error,
            )

    try:
        res = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,  # Decode output as text
            shell=True,
            cwd=cwd,
            env=environment_to_pass,
        )

        log_output(res, False)

    except subprocess.CalledProcessError as error:
        print_output(
            f"Command execution failed with return code: {error.returncode}",
            output=OutputType.Command,
            color=TerminalColors.Error,
        )

        log_output(error, True)

        sys.exit(1)

    except Exception as error:  # pylint: disable=broad-exception-caught
        print_output(f"An error occurred during command execution: f{str(error)}")
        sys.exit(1)
