# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from typing import (
    Annotated,
    Optional,
)

from pydantic import BaseModel, Field


class Const(BaseModel):
    """Constraint Model"""

    of: Annotated[
        Optional[str],
        Field(description="Owner of this Constraint"),
    ] = None

    @property
    def name(self) -> str:
        if not self.of:
            raise ValueError(
                "This constraint does not pass `of` value for take ownership."
            )
        return f"{self.of}_const"


class Pk(Const):
    """Primary Key Model.

    Examples:
        *   {
                "of": "foo",
                "cols": ["bar", "baz"],
            }
    """

    cols: Annotated[
        list[str],
        Field(default_factory=list, description="List of primary key columns"),
    ]

    @property
    def name(self) -> str:
        if not self.of:
            raise ValueError(
                "This constraint does not pass `of` value for take ownership."
            )
        if self.cols:
            return f'{self.of}_{"_".join(self.cols)}_pk'
        raise ValueError("This primary key does not have any columns.")


class Ref(BaseModel):
    """Reference Model

    Examples:
        *   {
                "tbl": "foo",
                "col": "bar",
            }
    """

    tbl: str
    col: str


class Fk(Const):
    """Foreign Key Model.

    Examples:
        *   {
                "of": "foo",
                "to": "bar",
                "ref": {
                    "table": "ref_table",
                    "column": "ref_column"
                }
            }
        *   {
                "to": "bar",
                "ref": {
                    "table": "ref_table",
                    "column": "ref_column"
                }
            }
    """

    to: str
    ref: Ref

    @property
    def name(self) -> str:
        if not self.of:
            raise ValueError(
                "This constraint does not pass `of` value for take ownership."
            )
        return f"{self.of}_{self.to}_{self.ref.tbl}_{self.ref.col}_fk"
