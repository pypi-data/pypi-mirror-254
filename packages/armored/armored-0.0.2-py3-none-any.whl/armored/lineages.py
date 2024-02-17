# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from datetime import date, datetime
from typing import (
    Annotated,
    Optional,
)
from zoneinfo import ZoneInfo

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)

from .__base import BaseUpdatableModel
from .enums.status import Status
from .settings import TSSetting


class TS(BaseModel):
    """Time Model"""

    ts: Annotated[
        datetime,
        Field(default_factory=lambda: datetime.utcnow(), alias="Timestamp"),
    ]
    tz: Annotated[str, Field(alias="TimeZone")] = TSSetting.tz

    @property
    def upts(self) -> datetime:
        """Return updated timestamp"""
        return datetime.now(tz=self.tz)

    @model_validator(mode="after")
    def prepare_time(self):
        self.ts: datetime = self.ts.astimezone(ZoneInfo(self.tz))
        return self


class Tag(TS):
    """Tag Model"""

    author: Annotated[
        Optional[str],
        Field(validate_default=True, description="Author"),
    ] = None
    desc: Annotated[
        Optional[str],
        Field(repr=False, description="Description"),
    ] = None
    labels: Annotated[
        list[str],
        Field(default_factory=list, description="Labels"),
    ]
    vs: Annotated[
        Optional[date],
        Field(validate_default=True, alias="TagVersion"),
    ] = None

    @field_validator("author")
    def set_author(cls, value: Optional[str]):
        return value or "undefined"

    @field_validator("vs")
    def set_version(cls, value: Optional[date]):
        """Pre initialize the `version` value that parsing from default"""
        return value if value else date(year=1990, month=1, day=1)


class BaseTask(BaseUpdatableModel):
    """Base Task Model"""

    st: Status


class BaseMsg(BaseUpdatableModel):
    level: int
    msg: str


class Msg(BaseMsg): ...


class Log(BaseUpdatableModel):
    msgs: list[Msg]
