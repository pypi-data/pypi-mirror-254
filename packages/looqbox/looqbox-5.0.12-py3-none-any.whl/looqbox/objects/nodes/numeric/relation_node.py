from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node
from looqbox.objects.nodes.node_type import NodeType
from looqbox.objects.nodes.reference.metric_reference_node import MetricReferenceNode


@dataclass(config=PydanticConfiguration.Config)
class RelationNode(Node):
    node_type: NodeType = NodeType.RELATION
    text: Optional[str] = None
    left_operand: Optional[MetricReferenceNode | dict] = None
    relations: Optional[list] = None
    _skip_child_type_check: bool = True
