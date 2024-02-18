from typing import Optional, List

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.condition.commons.metric import MetricRelation
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.condition.condition_type import ConditionType
from looqbox.objects.response_parameters.token import Token
from looqbox.utils.dot_notation import Functional


# noinspection PyArgumentList
@dataclass(config=PydanticConfiguration.Config)
class PotentialCondition(Condition):
    relations: List[MetricRelation]
    condition_type = ConditionType.POTENTIAL_CONDITION
    text: Optional[str] = None

    def as_sql_filter(self, column_name: str) -> str:
        return "\n".join(
            f"AND {column_name} {relation.operator.value} {relation.value.content}"
            for relation in self.relations
        )

    def get_entity_type(self):
        return None

    def _retrieve_value(self) -> list[any]:
        return Functional(self.relations).map_not_none_to_list(lambda relation: relation.value.content)
