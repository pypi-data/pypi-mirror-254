from abc import ABC, abstractmethod

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.condition.condition_type import ConditionType
from looqbox.objects.response_parameters.token import Token


@PydanticConfiguration.contains_subtypes(json_discriminator="type", class_discriminator="condition_type")
class Condition(ABC):
    condition_type: ConditionType
    text: str

    @abstractmethod
    def as_sql_filter(self, column_name: str) -> str:
        ...

    @abstractmethod
    def get_entity_type(self) -> str | None:
        ...

    @abstractmethod
    def _retrieve_value(self) -> list[any]:
        """
        Method to get only values from token
        """

    @property
    def values(self):
        return self._retrieve_value()

    def to_token(self):
        return Token(
            value=self.values,
            segment=self.text,
            text=self.text,
        )
