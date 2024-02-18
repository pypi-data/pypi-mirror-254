from typing import Optional, Any

from pydantic import Field
from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.relation_operator import RelationOperator


@dataclass(config=PydanticConfiguration.Config)
class RelationValue:
    content: int
    text: Optional[str] = None
    unit: Optional[dict] = None


@dataclass(config=PydanticConfiguration.Config)
class MetricRelation:
    value: RelationValue | Any
    _operator: str = Field(..., alias="operator")

    @property
    def operator(self) -> RelationOperator:
        return RelationOperator.from_str(self._operator)
