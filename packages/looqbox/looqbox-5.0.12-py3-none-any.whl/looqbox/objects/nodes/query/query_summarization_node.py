from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import TreeNode
from looqbox.objects.nodes.node_type import NodeType
from looqbox.objects.nodes.query.query_node import QueryNode


@dataclass(config=PydanticConfiguration.Config)
class QuerySummarizationNode(TreeNode):
    node_type: NodeType = NodeType.QUERY_SUMMARIZATION
    text: Optional[str] = None
    content: Optional[list[QueryNode]] = None
    id: Optional[str | int] = None
    operator: Optional[str] = None
    main_metric: Optional[str] = None
