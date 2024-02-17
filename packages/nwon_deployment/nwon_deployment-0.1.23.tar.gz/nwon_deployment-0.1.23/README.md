# NWON Deployment

This package provides some basic functionality that we are using for our
deployment scripts and CIs.

Package is meant for internal use at [NWON](https://nwon.de) as breaking changes may occur on version changes. This may change at some point but not for now 😇.

## What we offer

This package can help you:

- execute shell commands
- handle dependant environments in a docker compose based deployment
- docker commands
- different deployment strategy for updating a service
- setting files handling

### Command execution

We offer [functions](./nwon_deployment/commands/executor/__init__.py) for easily execute a shell command either locally or on a docker container that is attached to one of your defined services.

### Running docker commands

We offer a bunch of function that makes it easy to interact with you docker stack through docker compose or docker [commands](./nwon_deployment/commands/docker/).

There are also some [functions](./nwon_deployment/docker/) that basically wrap functionalities from the official [docker](https://pypi.org/project/docker/) package and ads our logging and some typing.

On top you get [functions](./nwon_deployment/docker/wait/) that wait for a specific health or container status.

### Environment handling

We assume that you have a folder which has folders with the names of all of your deployment environments. In the settings you can also define a function which defines a parent environment. For example it makes some sense to have a staging environment that is basically a copy of the production environments.

Here we offer some very simple helper to get the folder for the [current environment and base environment](./nwon_deployment/environment/__init__.py).

### Zero downtime deployment

We offer a bunch of [functions](./nwon_deployment/deployment/) updating a running docker stack either by simply starting or restarting or by performing a more sophisticated zero downtime update. You can also define post start executions for each defined service. For example migrating the database after updating an api service.

### Setting file handling

Every environment needs settings. We handle those in [toml](https://toml.io/en/) files living on the environment directories. There is one base file that and should be checked into version control and potentially a local override file that should not be checked in.

We handle the creation of those override files and also the loading of the settings and validating them against the provided schema.

For facilitating working with the toml files we offer functions that will create json schema files for both of these setting files in the base of you deployment scripts folder. Another function will then add the schema comment to the toml files. And 💣 boom you have autocomplete in your setting files when your editor can handle schemas for toml files.

## How to use

The package is configured via a setting object. You should set this settings in your deployment scripts before using any of the tools this package provides.

Typically this happens in the top level `__init__.py` file.

```python
from nwon_deployment.settings import set_deployment_package_settings
from nwon_deployment.typings.deployment_settings import (
    DeploymentSettings,
    DeploymentSettingsApplicationSettings,
    DeploymentSettingsDocker,
    DeploymentSettingsGitlab,
    DeploymentSettingsPaths,
)

settings = DeploymentSettings(
    deployment_environment=deployment_environment,
    deployment_base_environment=deployment_base_environment,
    gitlab=DeploymentSettingsGitlab(
        gitlab_registry_url="https://registry.gitlab.com/test",
        use_gitlab_container_registry=False,
    ),
    docker=DeploymentSettingsDocker(
        stack_name="test",
        container_name=container_name,
        user_for_container={
            DockerService.Api: "test",
        },
        default_command_for_container={DockerService.Api: "zsh"},
        env_variable_map=env_variables_map_callable,
        compose_files=docker_compose_files,
    ),
    application_settings=DeploymentSettingsApplicationSettings(
        settings=Settings,
        lines_to_prepend_to_settings_override=["Some","thing"],
        lines_to_prepend_to_settings=["Some","other","thing"],
    ),
    paths=DeploymentSettingsPaths(
        deployment_scripts_base="/Some/path",
        deployment_environment="/Some/other/path",
    ),
)

set_deployment_package_settings(settings)
```

## Working on the package

We recommend developing using poetry.

This are the steps to setup the project with a local virtual environment:

1. Tell poetry to create dependencies in a `.venv` folder withing the project: `poetry config virtualenvs.in-project true`
1. Create a virtual environment using the local python version: `poetry env use $(cat .python-version)`
1. Install dependencies: `poetry install`

## Prepare Package

Publishing the package it is not as straight forward as just calling `poetry build` 😥.

We need to:

1. Clean dist folder
1. Bump up the version of the package
1. Build the package

Luckily we provide a script for doing all of this `python scripts/prepare.py patch`. Alternatively you can run the script in a poetry context `poetry run prepare patch`. The argument at the end defines whether you want a `patch`, `minor` or `major` version bump.

The final zipped data ends up in the `dist` folder.

## Publish Package

Before publishing the package we need to:

1. Add test PyPi repository: `poetry config repositories.testpypi https://test.pypi.org/legacy/`
2. Publish the package to the test repository: `poetry publish -r testpypi`
3. Test package: `pip install --index-url https://test.pypi.org/simple/ nwon_baseline`

If everything works fine publish the package via `poetry publish`.
