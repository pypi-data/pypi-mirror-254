from enum import Enum

import maplestory.utils.kst as kst


class BaseEnum(Enum):
    """확장된 Enum 클래스로 키와 값에 대한 메서드를 제공합니다."""

    @classmethod
    def keys(cls) -> list[str]:
        """Enum 클래스의 모든 키를 리스트로 반환합니다.

        Returns:
            list: Enum 클래스의 모든 키를 포함하는 리스트입니다.
        """

        return list(cls.__members__)

    @classmethod
    def values(cls) -> list:
        """Enum 클래스의 모든 값을 리스트로 반환합니다.

        Returns:
            list: Enum 클래스의 모든 값을 포함하는 리스트입니다.
        """

        return [c.value for c in cls]


class WorldType(BaseEnum):
    """게임 내의 월드 타입을 나타내는 Enum 클래스입니다."""

    일반 = 0
    리부트 = 1


class GuildRankType(BaseEnum):
    """길드 랭킹 타입을 나타내는 Enum 클래스입니다."""

    주간명성치 = 0
    플레그레이스 = 1
    지하수로 = 2


class DojangDifficulty(BaseEnum):
    """무릉도장 구간를 나타내는 Enum 클래스입니다."""

    일반 = 0  # 105 ~ 200 레벨 (입문?)
    통달 = 1  # 201 이상 레벨


class QueryableDate(BaseEnum):
    """각 카테고리별 조회 가능한 최소 날짜를 나타내는 Enum 클래스입니다."""

    캐릭터 = kst.datetime(2023, 12, 21)
    유니온 = kst.datetime(2023, 12, 21)
    길드 = kst.datetime(2023, 12, 21)
    랭킹 = kst.datetime(2023, 12, 22)
    큐브 = kst.datetime(2022, 11, 25)
    스타포스 = kst.datetime(2023, 12, 27)
    잠재능력 = kst.datetime(2024, 1, 25)
