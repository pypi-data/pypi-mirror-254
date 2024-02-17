import pwd
from os import getuid

from nwon_deployment.helper.running_on_gitlab_ci import running_on_gitlab_ci


def get_user_id(user_name: str = "gitlab-runner"):
    """
    Returns the current user id.

    When running in gitlab CI it returns the id of the gitlab-runner user.
    """

    if running_on_gitlab_ci():
        try:
            return pwd.getpwnam(user_name).pw_uid
        except KeyError:
            pass

    return getuid()


__all__ = ["get_user_id"]
