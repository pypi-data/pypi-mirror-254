from __future__ import annotations

from datetime import datetime, date
from functools import cached_property
from typing import List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.nodes.node import Node
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.condition.condition_type import ConditionType
from looqbox.objects.response_parameters.date_operations import DateDeltaOperation
from looqbox.objects.response_parameters.relation_operator import RelationOperator
from looqbox.objects.response_parameters.temporal_granularity import TemporalGranularity
from looqbox.objects.response_parameters.token import Token
from looqbox.utils.dot_notation import Functional


@dataclass(config=PydanticConfiguration.Config)
class TemporalValue:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    millisecond: int
    dayOfYear: int
    dayOfWeek: str
    date: str
    segment: str

    @cached_property
    def as_datetime(self):
        return datetime(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second
        )

    @cached_property
    def as_date(self):
        return date(
            self.year,
            self.month,
            self.day
        )


@dataclass(config=PydanticConfiguration.Config)
class TemporalRelationValue:
    value: TemporalValue
    _operator: str = Field(..., alias="operator")

    @property
    def operator(self) -> RelationOperator:
        return RelationOperator.from_str(self._operator)


@dataclass(config=PydanticConfiguration.Config)
class TemporalTraits:
    """
    Dataclass that represents the traits of a temporal relation.

    Attributes:
        --------
        :param List[TemporalGranularity] granularity: The granularity of the temporal relation.
        :param str hemisphere: The hemisphere of the temporal relation.
        :param str time_zone: The time zone of the temporal relation.
        :param str zone_offset: The zone offset of the temporal relation.
    """
    granularity: Optional[List[TemporalGranularity]] = None
    times: Optional[str] = None
    hemisphere: Optional[str] = None
    time_zone: Optional[str] = None
    zone_offset: Optional[str] = None


# noinspection PyArgumentList
@dataclass(config=PydanticConfiguration.Config)
class TemporalRelation(Condition, Node):
    condition_type = ConditionType.TEMPORAL_RELATION
    traits: TemporalTraits
    relations: List[List[TemporalRelationValue]]
    id: int
    parameter_name: Optional[str] = None
    text: Optional[str] = None

    def _evaluate_date_boundaries(self, relation: TemporalRelationValue, requested_entity=None):
        operation_delta_available = {
            RelationOperator.GREATER_THAN_EQUAL: 0,
            RelationOperator.LESS_THAN_EQUAL: 0,
            RelationOperator.GREATER_THAN: 1,
            RelationOperator.LESS_THAN: -1
        }
        first_granularity: TemporalGranularity = Functional(self.traits.granularity).first()
        date_operation = DateDeltaOperation.get_for_text(first_granularity.name)
        delta_length = operation_delta_available.get(relation.operator)
        casted_relation = self._get_casted_temporal_relation_value(relation, requested_entity)
        return str(casted_relation + date_operation(delta_length))

    def _get_casted_temporal_relation_value(self, relation, requested_entity=None):
        return {
            "$date": lambda: relation.value.as_date,
            "$datetime": lambda: relation.value.as_datetime
        }.get(requested_entity or self.parameter_name, lambda: relation.value.as_datetime)()

    def as_sql_filter(self, column_name: str) -> str:
        flattened_relations: List[TemporalRelationValue] = Functional(self.relations).flatten_to_list()
        return "\n".join(
            f"AND {column_name} {relation.operator.value} \"{relation.value.date}\""
            for relation in flattened_relations
        )

    def get_entity_type(self):
        return self.parameter_name

    @cached_property
    def date_str_by_granularity(self) -> List[List[str]]:
        day_granularity_set = {TemporalGranularity.MINUTES, TemporalGranularity.MINUTES, TemporalGranularity.HOURS}
        within_day_range = any(granularity in self.traits.granularity for granularity in day_granularity_set)
        entity = ["$date", "$datetime"][within_day_range]  # False -> $date, True -> $datetime
        return self._retrieve_value_with_evaluated_boundaries(requested_entity=entity).to_list()

    def _retrieve_value(self, requested_entity=None) -> list[any]:
        retrieve_function_map = {
            "$date": self._retrieve_date,
            "$datetime": self._retrieve_datetime
        }
        return retrieve_function_map.get(requested_entity or self.parameter_name, lambda: None)()

    def _retrieve_value_with_evaluated_boundaries(self, requested_entity=None):  # Functional[List[List[str]]]
        return Functional(self.relations).map_nested_not_none(lambda relation: self._evaluate_date_boundaries(relation, requested_entity))

    @property
    def date_with_evaluated_boundaries(self) -> List[str]:
        return self._retrieve_value_with_evaluated_boundaries().flatten_to_list()

    def _retrieve_datetime(self) -> list[any]:
        return Functional(self.relations).map_nested_not_none_to_list(
            lambda relation: "{year:04}-{month:02}-{day:02} {hour:02}:{minute:02}:{second:02}".format(
                year=relation.value.year,
                month=relation.value.month,
                day=relation.value.day,
                hour=relation.value.hour,
                minute=relation.value.minute,
                second=relation.value.second
            )
        )

    def _retrieve_date(self):
        return Functional(self.relations).map_nested_not_none_to_list(lambda relation: relation.value.date)

    def to_token(self, should_evaluate_date_boundaries = False):
        return Token(
            value= self.date_with_evaluated_boundaries if should_evaluate_date_boundaries else self.values,
            segment=self.text,
            text=self.text,
            entity_name=self.parameter_name,
        )
