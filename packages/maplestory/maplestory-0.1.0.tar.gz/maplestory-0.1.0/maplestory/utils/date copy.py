from __future__ import annotations

from datetime import datetime

import maplestory.utils.kst as kst
from maplestory.enum import QueryableDate

DATE_FORMAT = "%Y-%m-%d"

# BASIC_MINIMUM_DATE = datetime(2023, 12, 21)

# # 캐릭터 정보 조회
# CHARACTER_MINIMUM_DATE = BASIC_MINIMUM_DATE

# # 길드 정보 조회
# GUILD_MINIMUM_DATE = BASIC_MINIMUM_DATE

# # 유니온 정보 조회
# UNION_MINIMUM_DATE = BASIC_MINIMUM_DATE

# # 랭킹 정보 조회
# RANK_MINIMUM_DATE = datetime(2023, 12, 22)

# # 큐브 정보 조회
# CUBE_MINIMUM_DATE = datetime(2022, 11, 25)

# # 스타포스 정보 조회
# STARFORCE_MINIMUM_DATE = datetime(2023, 12, 27)

# # 잠재능력 정보 조회
# POTENTIAL_MINIMUM_DATE = datetime(2024, 1, 25)


def to_string(date: datetime | None, format=DATE_FORMAT) -> str | None:
    return None if date is None else date.strftime(format)


def is_valid(date: kst.AwareDatetime, category: QueryableDate) -> bool:
    kst.validate(date)

    if date < category.value:
        dt = category.value.strftime(DATE_FORMAT)
        raise ValueError(f"{category.name}은 {dt}부터 데이터를 조회할 수 있습니다.")


# def validate(date: Kstkst.AwareDatetime, minimum_date: Kstkst.AwareDatetime) -> bool:
#     """
#     입력된 날짜가 지정된 최소 날짜 이후인지 검증합니다.
#     Validates the date and ensures it is after the minimum allowed date.

#     Args:
#         date (datetime): 검증할 날짜.
#                          The date to be validated.
#         minimum_date (datetime): 최소 날짜.
#                                  The minimum allowed date.

#     Returns:
#         datetime: 검증이 통과된 날짜.
#                   The validated date.

#     Raises:
#         ValueError: 입력된 날짜가 최소 날짜 이전인 경우 발생.
#                     If the date is before the minimum allowed date.

#     Example:
#         >>> validate_date(datetime(2023, 1, 1, tzinfo=ZoneInfo("Asia/Seoul")))
#         ValueError: 2023-12-21부터 데이터를 조회할 수 있습니다.

#         >>> validate_date(datetime(2024, 1, 1, tzinfo=ZoneInfo("Asia/Seoul")))
#         datetime(2024, 1, 1, tzinfo=ZoneInfo("Asia/Seoul"))

#     Description:
#         입력된 날짜가 MINIMUM_DATETIME 이전인 경우 ValueError를 발생시킵니다.
#         그렇지 않은 경우 입력된 날짜를 반환합니다.
#     """

#     if date < minimum_date:
#         raise ValueError(f"{minimum_date.strftime(DATE_FORMAT)}부터 데이터를 조회할 수 있습니다.")

#     return date

# def is_character_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= CHARACTER_MINIMUM_DATE

# def is_guild_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= GUILD_MINIMUM_DATE


# def is_union_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= UNION_MINIMUM_DATE


# def is_rank_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= RANK_MINIMUM_DATE


# def is_cube_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= CUBE_MINIMUM_DATE


# def is_starforce_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= STARFORCE_MINIMUM_DATE


# def is_potential_available_date(date: kst.AwareDatetime) -> bool:
#     kst.validate(date)
#     return date >= POTENTIAL_MINIMUM_DATE
