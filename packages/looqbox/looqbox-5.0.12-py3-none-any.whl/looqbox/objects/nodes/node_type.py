from enum import Enum


class NodeType(Enum):
    QUESTION = "question"
    QUERY = "query"
    QUERY_ARGUMENTS = "queryArguments"
    QUERY_ARGUMENTS_TO_MAP = "queryArgumentsToMap"
    QUERY_COMPARISON = "queryComparison"
    QUERY_SUMMARIZATION = "querySummarization"
    MATHEMATICAL_OPERATION = "mathematicalOperation"
    RESULT_NUMBER = "resultNumber"
    NUMBER = "number"
    RELATION = "relation"
    SQL_CONDITION_OPERATION = "sqlConditionOperation"
    METRIC_REFERENCE = "metricReference"
    TREE_NODE = "treeNode"
    TEMPORAL_STATEMENTS_TO_COMPARE = "temporalStatementsToCompare"
    ATEMPORAL_STATEMENTS_TO_COMPARE = "atemporalStatementsToCompare"
    COMPARISON_NODE = "comparisonNodes"
    RELATIONS = "relations"
