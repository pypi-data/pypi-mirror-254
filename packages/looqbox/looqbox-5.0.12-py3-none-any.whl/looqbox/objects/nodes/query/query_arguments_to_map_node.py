from typing import Optional, List, Any

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import TreeNode, Node
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class QueryArgumentsToMapNode(TreeNode):
    node_type: NodeType = NodeType.QUERY_ARGUMENTS_TO_MAP
    text: Optional[str] = None
    content: Optional[List[Node] | Any] = None
    id: Optional[dict] = None

    def accept(self, visitor):
        return visitor.visit(self)
