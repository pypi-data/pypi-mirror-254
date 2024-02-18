from typing import Optional, List

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.condition.commons.attribute import AtemporalReference, AttributeRelation, \
    AttributeValue
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.condition.condition_type import ConditionType
from looqbox.utils.dot_notation import Functional


# noinspection PyArgumentList
@dataclass(config=PydanticConfiguration.Config)
class SetRelation(Condition):
    left_operand: AtemporalReference
    relations: List[AttributeRelation]
    condition_type = ConditionType.SET_RELATION
    entity_type: Optional[str] = None
    text: Optional[str] = None
    _skip_child_type_check: bool = True

    def get_entity_type(self):
        return self.entity_type

    def as_sql_filter(self, column_name: str) -> str:
        return "\n".join(
            f"AND {column_name} {relation.operator.value} {self._evaluate_value(relation.values)}"  # relation = AttributeRelation / values = list[AttributeValue]
            for relation in self.relations
        )

    @staticmethod
    def _evaluate_value(values): # values = list[AttributeValue]
        if len(values) == 1:
            values = values[0]

        options = {
            list: lambda: f"({', '.join(str(el.value) for el in values)})",
            int: lambda : f"({values.value})",
            str: lambda: f"'{values.value}'",
        }
        return options[type(values.value)]()

    def _retrieve_value(self) -> list[any]:
        return Functional(self.relations).flat_map_not_none_to_list(
            lambda relation: Functional(relation.values).map_not_none_to_list(lambda it: it.value)
        )
