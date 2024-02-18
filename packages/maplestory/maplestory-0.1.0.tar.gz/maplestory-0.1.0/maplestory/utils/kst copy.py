from __future__ import annotations

from datetime import datetime as _datetime
from datetime import timedelta
from typing import Annotated, Any
from zoneinfo import ZoneInfo

from annotated_types import Timezone
from pydantic import GetCoreSchemaHandler
from pydantic.types import _check_annotated_type
from pydantic_core import core_schema

KST_TZ = ZoneInfo("Asia/Seoul")
KSTdatetime = Annotated[_datetime, Timezone("Asia/Seoul")]


class AwareDatetime:
    """A datetime that requires KST timezone info."""

    KST_TZ_CONSTRAINT = 9 * 60 * 60

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(tz_constraint=cls.KST_TZ_CONSTRAINT)

        schema = handler(source)
        _check_annotated_type(schema["type"], "datetime", cls.__name__)
        schema["tz_constraint"] = cls.KST_TZ_CONSTRAINT
        return schema

    def __repr__(self) -> str:
        return "KstAwareDatetime"


def validate(date: _datetime):
    if date.tzinfo is None:
        raise ValueError("datetime should have timezone info.")

    if date.tzinfo.utcoffset(date) != timedelta(
        seconds=AwareDatetime.KST_TZ_CONSTRAINT
    ):
        raise ValueError("datetime should have KST timezone info.")


def now() -> AwareDatetime:
    """Returns the current datetime in the KST (Korea Standard Time) timezone.

    Returns:
        datetime: The current datetime in the KST timezone.
    """

    return _datetime.now(KST_TZ)


def yesterday() -> AwareDatetime:
    """
    한국 표준시(KST) 기준으로 어제의 날짜를 구합니다.
    Returns the datetime of yesterday in the KST (Korea Standard Time) timezone.

    Returns:
        datetime: 어제의 날짜와 시간(한국 표준시).
                  The datetime of yesterday in the KST timezone.

    Description:
        현재 한국 표준시(KST)를 기준으로 하루를 뺀 날짜를 반환합니다.
        시간대는 'Asia/Seoul'로 설정됩니다.
    """

    today_kst = _datetime.now(KST_TZ)
    return today_kst - timedelta(days=1)


def datetime(
    year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0
) -> AwareDatetime:
    return _datetime(year, month, day, hour, minute, second, microsecond, tzinfo=KST_TZ)
