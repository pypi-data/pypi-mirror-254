# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
import re
from typing import (
    Any,
    Optional,
    Union,
)


def catch_str(
    value: str,
    key: str,
    *,
    replace: Optional[str] = None,
    flag: bool = True,
) -> tuple[str, Optional[Union[bool, str]]]:
    """Catch keyword from string value and return True if exits
    Examples:
        >>> catch_str("varchar( 100 ) unique", "unique")
        ('varchar( 100 )', True)
        >>> catch_str("integer primary keys", "primary key")
        ('integer s', True)
    """
    if key in value:
        return (
            " ".join(value.replace(key, (replace or "")).split()),
            (True if flag else key),
        )
    return value, (False if flag else None)


def split_dtype(dtype: str) -> tuple[str, str]:
    """Split the datatype value from long string by null string
    Examples:
    >>> split_dtype("string null")
    ('string', 'null')
    >>> split_dtype("numeric(10, 2) Null")
    ('numeric(10, 2)', 'null')
    >>> split_dtype("timestamp(6) NULL")
    ('timestamp(6)', 'null')
    >>> split_dtype("string not null")
    ('string', 'not null')
    >>> split_dtype("varchar( 20 ) not null null")
    ('varchar( 20 )', 'null')
    >>> split_dtype("string null null")
    ('string', 'null')
    """
    _nullable: str = "null"
    for null_str in (
        "not null",
        "Not Null",
        "NOT NULL",
        "null",
        "Null",
        "NULL",
    ):
        if re.search(null_str, dtype):
            _nullable = null_str
            dtype = dtype.replace(null_str, "")
    return " ".join(dtype.strip().split()), _nullable.lower()


def only_one(
    check_list: list[Any],
    match_list: list[Any],
    default: bool = True,
) -> Any:
    """Get only one value from the checking list that match with ordered value on
    the matching list.
        Examples:
        >>> list_a = ['a', 'a', 'b']
        >>> list_b = ['a', 'b', 'c']
        >>> list_c = ['d', 'f']
        >>> only_one(list_a, list_b)
        'a'
        >>> only_one(list_c, list_b)
        'a'
    """
    if len(exist := set(check_list).intersection(set(match_list))) == 1:
        return list(exist)[0]
    return next(
        (_ for _ in match_list if _ in check_list),
        (match_list[0] if default else None),
    )


def extract_dtype(dtype: str) -> dict[str, Any]:
    """
    Examples:
    >>> extract_dtype("varchar( 255 )")
    {'type': 'varchar', 'max_length': '255'}
    >>> extract_dtype("numeric(19, 2)")
    {'type': 'numeric', 'precision': '19', 'scale': '2'}
    """
    if m := re.search(
        r"(?P<type>\w+)"
        r"(?:\s?\(\s?(?P<max_length>\d+)(?:,\s?(?P<scale>\d+))?\s?\))?",
        dtype.strip(),
    ):
        extract = m.groupdict()
        if (t := extract["type"]) in ("numeric", "decimal"):
            extract["precision"] = extract.pop("max_length")
            extract["scale"] = extract.pop("scale", None) or -1
            return extract

        extract.pop("scale")
        if t in ("timestamp", "time"):
            extract["precision"] = extract.pop("max_length")
            return extract
        return extract
    return {"type": dtype}
