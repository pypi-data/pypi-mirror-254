from typing import Any, TypeVar, Type

from pydantic import TypeAdapter

T = TypeVar("T")


class ObjectMapper:
    @classmethod
    def map(cls, source: Any, target_class: Type[T]) -> T:
        return cls.validate_python(source, target_class)

    @staticmethod
    def validate_python(obj: Any, type_: Type[T]) -> T:
        return TypeAdapter(type_).validate_python(obj)
