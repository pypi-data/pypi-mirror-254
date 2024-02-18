from abc import ABC
from typing import Optional, Any

from pydantic import Field
from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node_type import NodeType
from looqbox.utils.dot_notation import Functional


# noinspection PyArgumentList
@PydanticConfiguration.contains_subtypes(json_discriminator="type", class_discriminator="node_type", default=NodeType.TREE_NODE)
class Node(ABC):
    text: Optional[str]
    node_type: NodeType = Field(..., alias='type')

    def recursively_get_self_and_children_nodes(self):
        if hasattr(self, "content"):
            if isinstance(self.content, int):
                return [self]
            children_nodes = Functional(self.content).filter(lambda it: isinstance(it, Node))
            if not children_nodes:
                return [self]
            return [self] + children_nodes.flat_map_not_none_to_list(lambda it: it.recursively_get_self_and_children_nodes())
        if hasattr(self, "apply"):
            children_nodes = Functional(self.apply).filter(lambda it: isinstance(it, Node))
            if not children_nodes:
                return [self]
            return [self] + children_nodes.flat_map_not_none_to_list(lambda it: it.recursively_get_self_and_children_nodes())
        return [self]


@dataclass(config=PydanticConfiguration.Config)
class TreeNode(Node):
    node_type: NodeType = NodeType.TREE_NODE
    text: Optional[str] = None
    content: Optional[list[Node] | Any] = None
