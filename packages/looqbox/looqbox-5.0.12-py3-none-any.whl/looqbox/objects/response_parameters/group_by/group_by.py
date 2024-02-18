from functools import cached_property
from typing import Any

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.condition.temporal_relation import TemporalTraits
from looqbox.objects.response_parameters.token import Token
from looqbox.objects.response_parameters.token_metadata import TokenMetadata


@dataclass(config=PydanticConfiguration.Config)
class GroupBy:
    text: str
    value: TemporalTraits | str
    start: int
    end: int
    metadata: TokenMetadata

    @cached_property
    def is_temporal(self) -> bool:
        return isinstance(self.value, TemporalTraits)

    def _retrieve_value(self) -> list[Any]:
        """
        Method to get only values from token
        """
        return [f"by{self.value.times.capitalize()}"] if self.is_temporal else []

    @property
    def values(self):
        return self._retrieve_value()

    def to_token(self):
        return Token(
            value=self.values,
            segment=self.text,
            text=self.text,
        )
