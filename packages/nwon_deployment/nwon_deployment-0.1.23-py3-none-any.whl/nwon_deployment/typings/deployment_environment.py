from enum import Enum


class DeploymentEnvironment(Enum):
    Review = "review"
    Development = "development"
    Testing = "testing"
    Staging = "staging"
    Production = "production"
