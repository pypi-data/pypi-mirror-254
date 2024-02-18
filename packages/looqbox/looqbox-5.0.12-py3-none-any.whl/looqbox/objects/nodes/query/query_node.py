from functools import cached_property
from typing import Optional, List, Any

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node, TreeNode
from looqbox.objects.nodes.node_type import NodeType


# noinspection PyArgumentList
@dataclass(config=PydanticConfiguration.Config)
class QueryNode(TreeNode):
    content: list[Node]
    node_type: NodeType = NodeType.QUERY
    text: Optional[str] = None
    id: Optional[str | dict | int] = None
    query_text: Optional[str] = None
    query_total: Optional[str] = None