from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class NumberNode(Node):
    node_type: NodeType = NodeType.NUMBER
    text: Optional[str] = None
    content: Optional[str | float] = None
    unit: Optional[dict] = None
