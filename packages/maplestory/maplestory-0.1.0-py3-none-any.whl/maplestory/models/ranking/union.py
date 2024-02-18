from pydantic import BaseModel

from maplestory.types.union import UnionWorldName


class UnionRankingInfo(BaseModel):
    """유니온 랭킹 상세 정보

    Attributes:
        date: 랭킹 업데이트 일자 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        ranking: 유니온 랭킹 순위
        character_name: 캐릭터 명
        world_name: 월드 명
        class_name: 직업 명
        sub_class_name: 전직 직업 명
        union_level: 유니온 레벨
        union_power: 유니온 파워
    """

    date: str
    ranking: int
    character_name: str
    world_name: UnionWorldName
    class_name: str
    sub_class_name: str
    union_level: int
    union_power: int


class UnionRanking(BaseModel):
    """유니온 랭킹 정보

    Attributes:
        ranking: 유니온 랭킹 정보
    """

    ranking: list[UnionRankingInfo]
