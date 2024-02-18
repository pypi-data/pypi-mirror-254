from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import TreeNode
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class QueryArgumentsNode(TreeNode):
    node_type: NodeType = NodeType.QUERY_ARGUMENTS
    text: Optional[str] = None
