from os import path
from typing import List

from nwon_deployment.setting_files.application_setting_schemas import (
    json_schema_file_name,
    optional_json_schema_file_name,
)
from nwon_deployment.settings import get_deployment_package_settings


def lines_to_prepend_setting(file_path: str) -> List[str]:
    settings = get_deployment_package_settings()

    path1 = path.abspath(json_schema_file_name())
    path2 = path.dirname(file_path)

    return [
        f"#:schema {path.relpath(path1, path2)}",
        "",
    ] + settings.application_settings.lines_to_prepend_to_settings


def lines_to_prepend_setting_override(file_path: str) -> List[str]:
    settings = get_deployment_package_settings()

    path1 = path.abspath(optional_json_schema_file_name())
    path2 = path.dirname(file_path)

    return [
        f"#:schema {path.relpath(path1, path2)}",
        "",
    ] + settings.application_settings.lines_to_prepend_to_settings_override


__all__ = ["lines_to_prepend_setting", "lines_to_prepend_setting_override"]
