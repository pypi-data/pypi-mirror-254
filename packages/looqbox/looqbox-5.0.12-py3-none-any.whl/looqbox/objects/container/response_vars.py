from typing import Optional

from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration


@dataclass(config=PydanticConfiguration.Config)
class FeatureFlags:
    file_sync: dict[str, int]


@dataclass(config=PydanticConfiguration.Config)
class ResponseVars:
    test_mode: bool
    home: str
    temp_dir: str
    jdbc_path: str
    response_timeout: int
    response_path: str
    entity_sync_path: str
    feature_flags: Optional[FeatureFlags] = None
