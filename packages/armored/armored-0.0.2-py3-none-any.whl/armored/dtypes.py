# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from typing import (
    Annotated,
    Literal,
    Union,
)

from pydantic import BaseModel, Field
from pydantic.functional_validators import field_validator


class BaseType(BaseModel):
    """Base Type"""

    type: str = "base"

    def __str__(self) -> str:
        return self.type


class StringType(BaseType):
    """String Type"""

    type: Literal["string", "str"] = "string"
    max_length: Annotated[int, Field(ge=-1)] = -1

    def __str__(self) -> str:
        _length: str = f"( {self.max_length} )" if self.max_length > -1 else ""
        return f"{self.type}{_length}"


class CharType(StringType):
    """Charactor Type

    Note: fixed-length strings
    """

    type: Literal["char"] = "char"


class VarcharType(StringType):
    """Variable Charactor Type

    Note: variable-length strings with limit
    """

    type: Literal["varchar"] = "varchar"


class TextType(BaseType):
    """Text Type

    Note: variable unlimited length strings
    """

    type: Literal["text"] = "text"


class IntegerType(BaseType):
    """Integer Type

    Note: Storage size, 4 bytes, -2147483648 to +2147483647
    """

    type: Literal["integer", "int"] = "integer"

    @field_validator("type", mode="after")
    def prepare_for_short_name(
        cls,
        value: Literal["integer", "int"],
    ) -> Literal["integer"]:
        return "integer" if value == "int" else value


class SmallIntType(BaseType):
    """Small Range Integer

    Note: Storage size, 2 bytes, -32768 to +32767
    """

    type: Literal["smallint"] = "smallint"


class BigIntType(BaseType):
    """Big Range Integer

    Note: Storage size, 8 bytes, -9223372036854775808 to +9223372036854775807
    """

    type: Literal["bigint"] = "bigint"


class ShortType(BaseType): ...


class LongType(BaseType): ...


class NumericType(BaseType):
    """Numeric Type"""

    type: Literal["numeric"] = "numeric"
    precision: Annotated[int, Field(ge=-1)] = -1
    scale: Annotated[int, Field(ge=-1)] = -1

    def __str__(self) -> str:
        _scale: str = f", {self.scale}" if self.scale > -1 else ""
        return f"{self.type}( {self.precision}{_scale} )"


class DecimalType(NumericType):
    """Decimal Type"""

    type: Literal["decimal"] = "decimal"


class FloatType(BaseType):
    type: Literal["float"] = "float"


class RealType(BaseType):
    type: Literal["real"] = "real"


class DoublePrecisionType(BaseType): ...


class TimestampType(BaseType):
    """Timestamp Type"""

    type: Literal["timestamp"] = "timestamp"
    precision: Annotated[int, Field(ge=-1, le=6)] = -1
    timezone: Annotated[
        bool,
        Field(description="Time zone flag"),
    ] = False


class TimeType(BaseType): ...


class DateType(BaseType): ...


class DateTimeType(BaseType): ...


class SerialType(BaseType):
    """Serial Type"""

    type: Literal["serial"]


DataTypes = Union[
    StringType,
    CharType,
    VarcharType,
    TextType,
    NumericType,
    DecimalType,
    TimestampType,
    IntegerType,
    BigIntType,
    SmallIntType,
    BaseType,
]
