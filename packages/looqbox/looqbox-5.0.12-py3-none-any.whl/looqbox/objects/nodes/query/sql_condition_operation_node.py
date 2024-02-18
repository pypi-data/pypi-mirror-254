from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import TreeNode
from looqbox.objects.nodes.node_type import NodeType


@dataclass(config=PydanticConfiguration.Config)
class SqlConditionOperationNode(TreeNode):
    node_type: NodeType = NodeType.SQL_CONDITION_OPERATION
    text: Optional[str] = None
