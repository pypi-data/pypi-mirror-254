from dataclasses import dataclass
from typing import Optional


@dataclass
class Token:
    segment: str
    text: str
    id: Optional[int] = None
    value: Optional[list[list[any]] | list[any] | str] = None
    entity_name: Optional[str] = None

