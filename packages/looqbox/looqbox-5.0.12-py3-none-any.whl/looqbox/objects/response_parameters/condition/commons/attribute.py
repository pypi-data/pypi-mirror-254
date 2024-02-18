from typing import Any, Optional, List

from pydantic import Field
from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.relation_operator import RelationOperator


@dataclass(config=PydanticConfiguration.Config)
class AttributeValue:
    id: Optional[Any] = None
    name: Optional[Any] = None
    text: Optional[str] = None

    @property
    def value(self):
        return self.id or self.name


@dataclass(config=PydanticConfiguration.Config)
class AttributeRelation:
    values: List[AttributeValue]
    _operator: str = Field(..., alias="operator")

    @property
    def operator(self) -> RelationOperator:
        return RelationOperator.from_str(self._operator)


@dataclass(config=PydanticConfiguration.Config)
class AtemporalReference:
    entity_id: Optional[int] = Field(..., alias="id")
    parameter_name: Optional[str] = None
