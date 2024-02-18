from enum import Enum


class ConditionType(Enum):
    POTENTIAL_CONDITION = "potentialCondition"
    TEMPORAL_RELATION = "temporalRelation"
    SET_RELATION = "setRelation"
    RELATION = "relation"
    QUANTITY = "quantity"
