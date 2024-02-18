from dataclasses import asdict
from typing import Any

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration
from looqbox.objects.response_parameters.token_metadata import TokenMetadata
from looqbox.objects.response_parameters.token import Token


@dataclass(config=PydanticConfiguration.Config)
class Keyword:
    text: str
    value: Any
    start: int
    end: int
    metadata: TokenMetadata

    def _retrieve_value(self) -> int:
        """
        Method to get only values from token
        """
        return self.metadata.entity.id

    @property
    def values(self):
        return self._retrieve_value()

    def to_token(self):
        return Token(
            id=self.metadata.entity.id,
            segment=self.text,
            text=self.text,
        )
