from __future__ import annotations

import re
from enum import Enum
from typing import Type, Any, Literal

from looqbox.config.logger import Logger
from looqbox.utils.dot_notation import Functional


# noinspection PyTypeHints
class PydanticConfiguration:
    logger = Logger.get_logger(__name__)

    class Config:
        @staticmethod
        def snake_case_to_camel_case(text: str):
            return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)

        alias_generator = snake_case_to_camel_case
        populate_by_name = True

    @classmethod
    def contains_subtypes(cls, json_discriminator: str = "type", class_discriminator: str = "type", default=None):

        if isinstance(default, Enum):
            default = default.value

        def decorator(super_cls: Type) -> Type:
            super_cls.__ref_classes__ = set()
            super_cls.__model__ = None

            def __init_subclass__(clz) -> None:
                clz.__ref_classes__.add(clz)
                clz.__annotations__[json_discriminator] = Literal[vars(clz)[class_discriminator]]
                setattr(clz, json_discriminator, vars(clz)[class_discriminator])

            def __get_validators__(clz) -> Any:
                yield clz.__validate__

            def __validate__(clz, cls_values: Any, values: dict, *args, **kwargs) -> Any:
                discriminator_value = cls_values.get(json_discriminator, None)
                discriminator_and_class = Functional(clz.__ref_classes__).associate_by(lambda sub: (cls._get_discriminator(sub, json_discriminator)))
                chosen_class = discriminator_and_class.get(discriminator_value, discriminator_and_class.get(default))
                if chosen_class is None:
                    error = f"Subtype {discriminator_value} not contained in {clz.__name__}"
                    cls.logger.error(error)
                    return
                try:
                    for key, value in cls_values.items():
                        should_recursively_validate = ((isinstance(value, dict) and json_discriminator in value)
                                                       and not getattr(chosen_class, "_skip_child_type_check", False))
                        if should_recursively_validate:
                            cls_values[key] = clz.__validate__(value, values, key)
                    cls_values.pop(json_discriminator)
                    return chosen_class(**cls_values)
                except AttributeError:
                    error = f"Error instantiating {chosen_class.__name__} with values {cls_values}"
                    cls.logger.error(error)
                    raise Exception(error)

            for method in __init_subclass__, __get_validators__, __validate__:
                setattr(super_cls, method.__name__, classmethod(method))

            return super_cls

        return decorator

    @classmethod
    def _get_discriminator(cls, sub, json_discriminator):
        val = getattr(sub, json_discriminator)
        if isinstance(val, Enum):
            val = val.value
        return val
