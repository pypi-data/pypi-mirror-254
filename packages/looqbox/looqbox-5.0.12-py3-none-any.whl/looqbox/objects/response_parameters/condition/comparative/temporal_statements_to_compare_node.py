from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node_type import NodeType
from looqbox.objects.response_parameters.condition.temporal_relation import TemporalRelation
from looqbox.objects.response_parameters.condition.comparative.comparison_node import ComparisonNode
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.token import Token
from looqbox.utils.dot_notation import Functional


@dataclass(config=PydanticConfiguration.Config)
class TemporalStatementsToCompareNode(ComparisonNode, Condition):
    node_type: NodeType = NodeType.TEMPORAL_STATEMENTS_TO_COMPARE
    content: Optional[list[TemporalRelation]] = None
    text: Optional[str] = None

    def as_sql_filter(self, column_name: str) -> str:
        return "\n".join(Functional(self.content).map_not_none_to_list(lambda relation: relation.as_sql_filter(column_name)))

    def get_entity_type(self) -> str | None | TemporalRelation:
        return Functional(self.content).first_not_none(lambda relation: relation.parameter_name)

    def _retrieve_value(self) -> list[any]:
        return Functional(self.content).flat_map_not_none_to_list(lambda relation: relation.values)

    def to_token(self):
        entity_token = self.get_entity_type()
        return Token(
            value=Functional(self.content).map_not_none_to_list(lambda relation: relation.to_token()),
            segment=self.text,
            text=self.text,
            entity_name=entity_token.parameter_name if isinstance(entity_token, TemporalRelation) else entity_token,
        )
