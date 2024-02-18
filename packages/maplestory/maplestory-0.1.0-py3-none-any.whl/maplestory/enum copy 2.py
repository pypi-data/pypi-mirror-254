from enum import Enum

import maplestory.utils.kst as kst


class BaseEnum(Enum):
    @classmethod
    def keys(cls):
        return list(cls.__members__)

    @classmethod
    def values(cls):
        return [c.value for c in cls]


class WorldType(BaseEnum):
    일반 = 0  # normal
    리부트 = 1  # reboot

    # NORMAL = 0 # 일반
    # REBOOT = 1 # 리부트


class GuildRankType(BaseEnum):
    주간명성치 = 0  # Weekly Fame
    플레그레이스 = 1  # Flag Race
    지하수로 = 2  # Underground Waterway

    # WEEKLY_FAME = 0  # 주간 명성치
    # FLAG_RACE = 1  # 플래그 레이스
    # UNDERGROUND_WATERWAY = 2  # 지하 수로


class MinimumDate(BaseEnum):
    # CHARACTER = kst.datetime(2023, 12, 21)
    # RANK = kst.datetime(2023, 12, 22)

    # CUBE = kst.datetime(2022, 11, 25)
    # STARFORCE = kst.datetime(2023, 12, 27)
    # POTENTIAL = kst.datetime(2024, 1, 25)

    캐릭터 = kst.datetime(2023, 12, 21)
    유니온 = kst.datetime(2023, 12, 21)
    길드 = kst.datetime(2023, 12, 21)
    랭킹 = kst.datetime(2023, 12, 22)
    큐브 = kst.datetime(2022, 11, 25)
    스타포스 = kst.datetime(2023, 12, 27)
    잠재능력 = kst.datetime(2024, 1, 25)


# from enum import Enum
# from datetime import datetime
# from dataclasses import dataclass

# @dataclass
# class MinimumDate(Enum):
#     CHARACTER = CHARACTER_MINIMUM_DATE
#     GUILD = GUILD_MINIMUM_DATE
#     UNION = UNION_MINIMUM_DATE
#     RANK = RANK_MINIMUM_DATE
#     CUBE = CUBE_MINIMUM_DATE
#     STARFORCE = STARFORCE_MINIMUM_DATE
#     POTENTIAL = POTENTIAL_MINIMUM_DATE

# def is_available_date(date: kst.AwareDatetime, category: MinimumDate) -> bool:
#     kst.validate(date)

#     return match category:
#         case MinimumDate.CHARACTER:
#             return date >= MinimumDate.CHARACTER.value
#         case MinimumDate.GUILD:
#             return date >= MinimumDate.GUILD.value
#         case MinimumDate.UNION:
#             return date >= MinimumDate.UNION.value
#         case MinimumDate.RANK:
#             return date >= MinimumDate.RANK.value
#         case MinimumDate.CUBE:
#             return date >= MinimumDate.CUBE.value
#         case MinimumDate.STARFORCE:
#             return date >= MinimumDate.STARFORCE.value
#         case MinimumDate.POTENTIAL:
#             return date >= MinimumDate.POTENTIAL.value


# class TestEnum(Enum):
#     NORMAL = '0' # 일반
#     REBOOT = '1' # 리부트

# print(f"{TestEnum.NORMAL == '0' = }")


# class DateEnum(datetime, ReprEnum):
#     """
#     Enum where members are also (and must be) ints
#     """

# class TestDateEnum(DateEnum):
#     NORMAL = datetime(2023, 12, 21) # 일반

# print(f"{TestDateEnum.NORMAL == datetime(2023, 12, 21) = }")
# # TypeError: 'datetime.datetime' object cannot be interpreted as an integer

# class TestIntEnum(IntEnum):
#     NORMAL = 0 # 일반
#     REBOOT = 1 # 리부트

# print(f"{TestIntEnum.NORMAL == 0 = }")


# class TestStrEnum(StrEnum):
#     NORMAL = "0" # 일반
#     REBOOT = "1" # 리부트

# print(f"{TestStrEnum.NORMAL == "0" = }")
