from dataclasses import asdict
from enum import Enum
from typing import Set, Optional, Any, Dict

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration


class EntityVocabularyScope(Enum):
    FILTER = "FILTER"
    GROUP_BY = "GROUP_BY"
    KEYWORD = "KEYWORD"


@dataclass(config=PydanticConfiguration.Config)
class TokenEntity:
    id: str | int
    prefix: Dict[str, str]
    type: str
    flags: Optional[Set[str]] = None
    token_type: Optional[str] = None


@dataclass(config=PydanticConfiguration.Config)
class TokenMetadata:
    entity: TokenEntity
    category: str
    matched_prefix: bool
    scope: EntityVocabularyScope
    is_comparative: Optional[bool] = None
    is_admin_command: Optional[bool] = None



