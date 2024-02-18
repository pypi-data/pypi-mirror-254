from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.container.response_vars import ResponseVars
from looqbox.objects.flow.flow_type import FlowType


@dataclass(config=PydanticConfiguration.Config)
class ScriptInfo:
    result_path: str
    response_parameters_path: str = Field(..., alias="responseParameters")
    flow_type: FlowType = Field(..., alias="flowId")
    upload_file: Optional[bool] = False
    response_vars: Optional[ResponseVars] = Field(..., alias="vars")
