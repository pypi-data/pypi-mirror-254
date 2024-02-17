# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from enum import IntEnum
from functools import total_ordering


def enum_ordering(cls):
    """Add order property to Enum object."""

    def __lt__(self, other):
        if type(other) is type(self):
            return self.value < other.value
        raise ValueError("Cannot compare different Enums")

    cls.__lt__ = __lt__
    return total_ordering(cls)


@enum_ordering
class Status(IntEnum):
    SUCCESS: int = 0
    APPROVED: int = 0
    FAILED: int = 1
    WAITING: int = 2
    PROCESSING: int = 2
    TRIGGERED: int = 2

    def in_process(self) -> bool:
        return self.value == 2
