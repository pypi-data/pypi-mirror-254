import json
from typing import Any

from nwon_deployment.print_output import OutputType, print_output


def handle_docker_package_output(output: Any) -> str:
    try:
        output = output.decode("utf-8").strip()
    except (UnicodeDecodeError, AttributeError):
        pass

    if isinstance(output, (int, str)):
        text = str(output)

    elif output is None:
        text = "EMPTY"

    else:
        text = __text_from_iterator(output)

    print_output(
        text,
        output=OutputType.Docker,
    )

    return text


def __text_from_iterator(output: Any):
    return_output = ""

    try:
        for line in output:
            try:
                line_as_dict = line if isinstance(line, dict) else json.loads(line)

                if "stream" in line_as_dict:
                    text = line_as_dict["stream"].strip()
                    return_output = return_output + line_as_dict["stream"].strip()
                else:
                    values = []
                    for key, value in line_as_dict.items():
                        values.append(f"{key}: {value}")

                    text = ", ".join(values)
            except (
                UnicodeDecodeError,
                AttributeError,
                TypeError,
                json.decoder.JSONDecodeError,
            ):
                if isinstance(line, (int, str)):
                    text = str(line)
                else:
                    text = line.decode("utf-8").strip()

            print_output(
                text,
                output=OutputType.Docker,
            )

            return_output = return_output + text

    except TypeError:
        pass

    try:
        line_as_dict = output if isinstance(output, dict) else json.loads(output)

        if "stream" in line_as_dict:
            return_output = line_as_dict["stream"].strip()
        else:
            return_output = line_as_dict
    except Exception:  # pylint: disable=broad-exception-caught
        return_output = output

    return return_output
