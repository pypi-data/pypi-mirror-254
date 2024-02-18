from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class MathematicalOperationNode(Node):
    node_type: NodeType = NodeType.MATHEMATICAL_OPERATION
    text: Optional[str] = None
    apply: Optional[dict] = None
