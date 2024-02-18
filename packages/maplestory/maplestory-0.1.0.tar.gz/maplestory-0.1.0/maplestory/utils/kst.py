"""이 모듈은 한국 표준시(KST)에 대한 날짜와 시간을 처리하는 함수와 클래스를 제공합니다. 

- `AwareDatetime` 클래스는 한국 표준시(KST) 시간대 정보를 요구하는 datetime을 나타냅니다. 
- `validate` 함수는 주어진 datetime이 한국 표준시(KST) 시간대 정보를 가지고 있는지 확인합니다.
- `now`, `yesterday`, `datetime` 함수는 각각 현재, 어제, 주어진 시간의 한국 표준시(KST)을 반환합니다.
"""

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
    """한국 표준시(KST) 시간대 정보를 요구하는 datetime을 나타냅니다."""

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
    """주어진 날짜가 한국 표준시(KST) 시간대 정보를 가지고 있는지 확인합니다."""
    if date.tzinfo is None:
        raise ValueError("datetime should have timezone info.")

    if date.tzinfo.utcoffset(date) != timedelta(
        seconds=AwareDatetime.KST_TZ_CONSTRAINT
    ):
        raise ValueError("datetime should have KST timezone info.")


def now() -> AwareDatetime:
    """현재 한국 표준시(KST) 시간을 반환합니다."""
    return _datetime.now(KST_TZ)


def yesterday() -> AwareDatetime:
    """어제의 한국 표준시(KST) 시간을 반환합니다."""
    today_kst = _datetime.now(KST_TZ)
    return today_kst - timedelta(days=1)


def datetime(
    year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0
) -> AwareDatetime:
    """주어진 시간의 한국 표준시(KST)를 반환합니다."""
    return _datetime(year, month, day, hour, minute, second, microsecond, tzinfo=KST_TZ)
