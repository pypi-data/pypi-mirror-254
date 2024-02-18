from typing import Optional, Any, List, Dict

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.container.response_vars import ResponseVars
from looqbox.objects.response_parameters.condition.api import Condition
from looqbox.objects.response_parameters.group_by.group_by import GroupBy
from looqbox.objects.response_parameters.keyword.keyword import Keyword
from looqbox.objects.response_parameters.response_question import ResponseQuestion
from looqbox.objects.response_parameters.response_user import ResponseUser
from looqbox.objects.nodes.api import *


@dataclass(config=PydanticConfiguration.Config)
class ResponseParameters:
    question: ResponseQuestion | str
    user: ResponseUser
    company_id: int
    conditions: Optional[List[Condition]] = None
    keywords: Optional[Dict[str, Keyword]] = None
    group_by: Optional[Dict[str, GroupBy]] = None
    connection_name: Optional[str] = None
    response_vars: Optional[ResponseVars] = None
    device_type: Optional[str] = "desktop"
    app_type: Optional[str] = "browser"
    syntax_tree: Optional[Node] = None
