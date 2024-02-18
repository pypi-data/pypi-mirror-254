from functools import cached_property
from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node
from looqbox.objects.nodes.node_type import NodeType
from looqbox.objects.response_parameters.condition.set_relation import SetRelation
from looqbox.objects.response_parameters.condition.comparative.comparison_node import ComparisonNode
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.token import Token
from looqbox.utils.dot_notation import Functional


@dataclass(config=PydanticConfiguration.Config)
class Relations(Node):
    node_type: NodeType = NodeType.RELATIONS
    content: Optional[list[SetRelation]] = None
    text: Optional[str] = None


@dataclass(config=PydanticConfiguration.Config)
class AtemporalStatementsToCompareNode(ComparisonNode, Condition):
    node_type: NodeType = NodeType.ATEMPORAL_STATEMENTS_TO_COMPARE
    content: Optional[list[Relations]] = None
    text: Optional[str] = None

    @cached_property
    def relation_content(self):
        return Functional(self.content).flat_map_not_none_to_list(lambda relation: relation.content)

    def as_sql_filter(self, column_name: str) -> str:
        return "\n".join(Functional(self.relation_content).map_not_none_to_list(lambda relation: relation.as_sql_filter(column_name)))

    def get_entity_type(self) -> str | None:
        return Functional(self.relation_content).first_not_none(lambda relation: relation.entity_type)

    def _retrieve_value(self) -> list[any]:
        return Functional(self.relation_content).flat_map_not_none_to_list(lambda relation: relation.values)

    def to_token(self):
        return Token(
            value=Functional(self.relation_content).map_not_none_to_list(lambda relation: relation.to_token()),
            segment=self.text,
            text=self.text,
            entity_name=Functional(self.relation_content).map_not_none(lambda relation: relation.entity_type).drop_duplicates().to_list()
        )
