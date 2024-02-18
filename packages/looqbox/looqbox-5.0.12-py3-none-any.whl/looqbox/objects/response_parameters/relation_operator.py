from __future__ import annotations

from enum import Enum


class RelationOperator(Enum):
    GREATER_THAN = ">"
    LESS_THAN = "<"
    EQUAL = "="
    GREATER_THAN_EQUAL = ">="
    LESS_THAN_EQUAL = "<="
    NOT_EQUAL = "!="
    IN = "in"
    NOT_IN = "not in"
    LIKE = "like"

    @classmethod
    def from_str(cls, text: str) -> RelationOperator:
        for relation_operator in cls:
            if relation_operator.value == text or relation_operator.name == text:
                return relation_operator
        raise ValueError(f"Invalid RelationOperator: {text}")
