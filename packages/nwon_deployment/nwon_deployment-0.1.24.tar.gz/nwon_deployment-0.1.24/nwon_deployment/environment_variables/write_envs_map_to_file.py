from typing import List

from nwon_deployment.typings import EnvVariableMap


def write_envs_map_to_file(env_variables_map: EnvVariableMap, path_to_write: str):
    with open(path_to_write, "w+", encoding="utf-8") as file:
        content: List[str] = []
        for key, value in env_variables_map.items():
            # skip variables masked by Gitlab
            if value is None or value == "[MASKED]":
                continue

            if isinstance(value, str):
                prepared_value = f'"{value}"'
            elif isinstance(value, bool):
                prepared_value = f'"{str(value)}"'
            else:
                prepared_value = str(value)

            content.append(f"{key}={prepared_value}")

        file.write("\n".join(content))
        file.close()


__all__ = [
    "write_envs_map_to_file",
]
