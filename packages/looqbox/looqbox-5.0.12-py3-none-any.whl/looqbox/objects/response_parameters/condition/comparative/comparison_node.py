from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import TreeNode, Node
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class ComparisonNode(TreeNode):
    node_type: NodeType = NodeType.COMPARISON_NODE
    text: Optional[str] = None
    content: Optional[list[Node]] = None
