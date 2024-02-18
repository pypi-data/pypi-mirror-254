import json
from os import path, remove

from nwon_deployment.settings import get_deployment_package_settings


def dump_schemas():
    """
    Dump JSON schemas of application settings to files.

    We dump one version with the original schema for the default setting files.
     We also dump a second one with all fields set to optional for the setting
     override files.
    """

    file_name = optional_json_schema_file_name()
    remove(file_name)
    dump_optional_schema_if_not_exists(file_name)

    file_name = json_schema_file_name()
    remove(file_name)
    dump_setting_schema_if_not_exists(file_name)


def dump_optional_schema_if_not_exists(file_name: str):
    """
    Dump of a JSON schema for the application settings with all fields set to optional.

    This is used for validating the setting override file.
    """

    if not path.exists(file_name):
        __dump_application_settings_optional_schema(file_name)


def dump_setting_schema_if_not_exists(file_name: str):
    """
    Dump of a JSON schema for the application settings.

    This is used for validating the setting file.
    """

    if not path.exists(file_name):
        __dump_application_settings_schema(file_name)


def optional_json_schema_file_name():
    settings = get_deployment_package_settings()
    return path.join(
        settings.paths.deployment_scripts_base,
        settings.application_settings.optional_json_schema_file_name,
    )


def json_schema_file_name():
    settings = get_deployment_package_settings()
    return path.join(
        settings.paths.deployment_scripts_base,
        settings.application_settings.json_schema_file_name,
    )


def __dump_application_settings_schema(target_path: str):
    settings = get_deployment_package_settings()
    schema = settings.application_settings.settings.model_json_schema()

    with open(target_path, "w+", encoding="utf-8") as file:
        file.write(json.dumps(schema))


def __dump_application_settings_optional_schema(target_path: str):
    settings = get_deployment_package_settings()
    schema = settings.application_settings.settings.model_json_schema()
    __set_required_to_false(schema)

    with open(target_path, "w+", encoding="utf-8") as file:
        file.write(json.dumps(schema))


def __set_required_to_false(schema):
    if isinstance(schema, dict):
        for k, value in schema.items():
            if k == "required":
                schema[k] = False
            elif isinstance(value, dict):
                __set_required_to_false(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        __set_required_to_false(item)


__ALL__ = [
    "optional_json_schema_file_name",
    "json_schema_file_name",
    "dump_schemas",
    "dump_optional_schema_if_not_exists",
    "dump_setting_schema_if_not_exists",
]
