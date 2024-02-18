from pydantic.dataclasses import dataclass

from looqbox.config.pydantic_configuration import PydanticConfiguration


@dataclass(config=PydanticConfiguration.Config)
class ResponseQuestion:
    original: str
    clean: str

    def __str__(self):
        return self.clean

    def __repr__(self):
        return self.clean

    def to_dict(self):
        return {
            "original": self.original,
            "clean": self.clean
        }
