from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class MetricReferenceNode(Node):
    node_type: NodeType = NodeType.METRIC_REFERENCE
    text: Optional[str] = None
    parameter_id: Optional[str] = None
    id: Optional[str | int] = None

