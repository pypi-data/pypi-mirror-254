"""Utilities for working with datetime objects."""

from datetime import datetime
from enum import Enum
from typing import Type
from zoneinfo import ZoneInfo

__all__ = ["apply_tz", "iso2dmy", "iso2format", "iso2ymd", "round_by"]

DMY: str = "%d.%m.%Y"
YMD: str = "%Y-%m-%d"


class RoundByEnum(Enum):
    """Available datetime rounding options."""

    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"

    @classmethod
    def values(cls: Type["RoundByEnum"]) -> list[str]:
        """Get enum elements values."""
        return [_.value for _ in cls]


def apply_tz(dt: datetime, tz: str = "UTC", /) -> datetime:
    """Apply timezone context to datetime object.

    Args:
        dt: Source datetime object.
        tz: Name of timezone for correction (UTC by default).

    Returns:
        A new datetime object in specified timezone.

    Usage:

    .. code-block:: python

        from datetime import datetime, UTC
        from pure_utils import apply_tz

        datetime_with_tz_context = apply_tz(datetime.now(UTC), "Europe/Moscow")
    """
    return dt.astimezone(ZoneInfo(tz))


def iso2format(isostr: str, fmt: str, /) -> str:
    """Convert ISO-8601 datetime string into a string of specified format.

    Args:
        isostr: ISO-8601 datetime string.
        fmt: New datetime format.

    Returns:
        Datetime string in specified format.

    Usage:

    .. code-block:: python

        from pure_utils import iso2format, YMD

        formatted_dt = iso2format("2005-08-09T18:31:42/P3Y6M4DT12H30M17S", YMD)

        print(formatted_dt)  # 2005-08-09
    """
    return datetime.fromisoformat(isostr).strftime(fmt)


def iso2dmy(isostr: str, /) -> str:
    """Convert ISO-8601 datetime string into a string of DMY (DD.MM.YYYY) format.

    Args:
        isostr: ISO-8601 datetime string.

    Returns:
        Datetime string in DMY format (DD.MM.YYYY).

    Usage:

    .. code-block:: python

        from pure_utils import iso2dmy

        formatted_dt = iso2dmy("2005-08-09T18:31:42")

        print(formatted_dt)  # 09.08.2005
    """
    return iso2format(isostr, DMY)


def iso2ymd(isostr: str, /) -> str:
    """Convert ISO-8601 datetime string into a string of YMD (YYYY-MM-DD) format.

    Args:
        isostr: ISO-8601 datetime string.

    Returns:
        Datetime string in YMD format (YYYY-MM-DD).

    Usage:

    .. code-block:: python

        from pure_utils import iso2ymd

        formatted_dt = iso2ymd("20080809T183142+0")

        print(formatted_dt)  # 2008-08-09
    """
    return iso2format(isostr, YMD)


def round_by(dt: datetime, /, *, boundary: str) -> datetime:
    """Round datetime, discarding excessive precision.

    Args:
        dt: Datetime object.
        boundary: Rounding boundary.
                  Available values: day, hour, minute, second.

    Returns:
        Rounded datetime object.

    Raises:
        ValueError: If `boundary` is invalid.

    Usage:

    .. code-block:: python

        from datetime import datetime
        from pure_utils import round_by

        exact_datatime = datetime.now()
        print(exact_datatime)  # 2024-02-03 17:54:37.472482

        rounded_datetime = round_by(exact_datatime, boundary="hour")
        print(rounded_datetime)  # 2024-02-03 17:00:00
    """
    replace = {}

    match boundary:
        case RoundByEnum.DAY.value:
            for _ in ("hour", "minute", "second", "microsecond"):
                replace[_] = 0
        case RoundByEnum.HOUR.value:
            for _ in ("minute", "second", "microsecond"):
                replace[_] = 0
        case RoundByEnum.MINUTE.value:
            replace["second"] = 0
            replace["microsecond"] = 0
        case RoundByEnum.SECOND.value:
            replace["microsecond"] = 0
        case _:
            raise ValueError(
                f"Invalid boundary value ({boundary}). Available only: {RoundByEnum.values()}."
            )

    return dt.replace(**replace, tzinfo=dt.tzinfo)
