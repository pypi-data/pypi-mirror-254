"""이 모듈은 날짜와 관련된 유틸리티 함수를 제공합니다. 

- `to_string` 함수는 datetime 객체를 문자열로 변환합니다.
- `is_valid` 함수는 주어진 날짜가 특정 카테고리에 대해 유효한지 확인합니다.
"""

from datetime import datetime

import maplestory.utils.kst as kst
from maplestory.enum import QueryableDate

DATE_FORMAT = "%Y-%m-%d"


def to_string(date: datetime | None, format=DATE_FORMAT) -> str | None:
    """datetime 객체를 주어진 포맷의 문자열로 변환합니다. 만약 date가 None이면 None을 반환합니다.

    Args:
        date (datetime | None): 변환할 datetime 객체입니다.
        format (str, optional): 날짜를 문자열로 변환할 때 사용할 포맷입니다. 기본값은 "%Y-%m-%d"입니다.

    Returns:
        str | None: datetime 객체를 문자열로 변환한 결과입니다. date가 None이면 None을 반환합니다.
    """
    return None if date is None else date.strftime(format)


def is_valid(date: kst.AwareDatetime, category: QueryableDate) -> None:
    """주어진 날짜가 특정 카테고리에 대해 유효한지 확인합니다. 만약 날짜가 카테고리의 조회 가능한 날짜보다 이전이면 ValueError를 발생시킵니다.

    Args:
        date (kst.AwareDatetime): 확인할 날짜
        category (MinimumDate): 확인할 카테고리

    Raises:
        ValueError: 날짜가 카테고리의 조회 가능한 날짜보다 이전인 경우 발생합니다.
    """

    kst.validate(date)

    if date < category.value:
        queryable_date = category.value.strftime(DATE_FORMAT)
        raise ValueError(f"{category.name}은 {queryable_date}부터 데이터를 조회할 수 있습니다.")
