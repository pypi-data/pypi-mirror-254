from datetime import datetime, date
from typing import Any, Callable, Annotated, Type

from bson import ObjectId
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema


class _ObjectIdPydanticAnnotation:
    # Based on https://docs.pydantic.dev/latest/usage/types/custom/#handling-third-party-types.
    # https://stackoverflow.com/a/76837550

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        def validate_from_str(input_value: str) -> ObjectId:
            return ObjectId(input_value)

        return core_schema.union_schema(
            [
                # check if it's an instance first before doing any further work
                core_schema.is_instance_schema(ObjectId),
                core_schema.no_info_plain_validator_function(
                    validate_from_str),
            ],
            serialization=core_schema.to_string_ser_schema(),
        )


PydanticObjectId = Annotated[
    ObjectId, _ObjectIdPydanticAnnotation
]


class Date(date):
    """
    Date class

    Args:
        date (date): Concrete date type.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(),
            serialization=core_schema.format_ser_schema('%Y-%m-%d')
        )

    @classmethod
    def validate(cls, v: str):
        try:
            date_obj = datetime.fromisoformat(v)
            return date_obj
        except ValueError:
            raise ValueError("Invalid ISO 8601 date format")
