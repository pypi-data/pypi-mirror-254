from pydantic import BaseModel, ConfigDict


class DeploymentBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
