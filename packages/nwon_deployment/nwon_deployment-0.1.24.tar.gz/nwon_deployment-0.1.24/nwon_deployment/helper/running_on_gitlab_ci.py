from os import getenv


def running_on_gitlab_ci() -> bool:
    """
    Returns whether or not we are running on a Gitlab CI pipeline.

    This is determined based on the existence of CI environment variables:
    https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
    """

    return getenv("CI") is not None


__all__ = ["running_on_gitlab_ci"]
