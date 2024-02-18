from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.condition.condition_type import ConditionType


@dataclass(config=PydanticConfiguration.Config)
class QuantityNode(Condition):
    condition_type: ConditionType = ConditionType.QUANTITY
    text: Optional[str] = None
    content: Optional[int] = 10
    unit: Optional[dict] = None

    def as_sql_filter(self, column_name: str) -> str:
        return ""

    def get_entity_type(self) -> str | None:
        return "$topn"

    def _retrieve_value(self) -> int:
        return self.content
