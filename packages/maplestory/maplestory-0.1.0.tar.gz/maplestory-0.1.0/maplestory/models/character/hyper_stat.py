from datetime import datetime
from pydantic import BaseModel, Field

class HyperStatItem(BaseModel):
    """캐릭터 하이퍼스탯 한 줄 정보

    Attributes:
        type (str): 스탯 종류
        point (int | None): 스탯 투자 포인트
        level (int): 스탯 레벨
        increase (str | None): 스탯 상승량
    """

    type: str = Field(alias="stat_type")
    point: int | None = Field(alias="stat_point")
    level: int = Field(alias="stat_level")
    increase: str | None = Field(alias="stat_increase")


class HyperStat(BaseModel):
    """캐릭터 하이퍼스탯 정보

    Attributes:
        date (datetime): 조회 기준일
        character_class (str): 캐릭터 직업
        preset_no (str): 적용 중인 프리셋 번호
        use_available (int): 사용 가능한 최대 하이퍼스탯 포인트
        preset1 (list[HyperStatItem]): 프리셋 1번 하이퍼 스탯 정보
        preset1_remain_point (int): 프리셋 1번 하이퍼 스탯 잔여 포인트
        preset2 (list[HyperStatItem]): 프리셋 2번 하이퍼 스탯 정보
        preset2_remain_point (int): 프리셋 2번 하이퍼 스탯 잔여 포인트
        preset3 (list[HyperStatItem]): 프리셋 3번 하이퍼 스탯 정보
        preset3_remain_point (int): 프리셋 3번 하이퍼 스탯 잔여 포인트
    """

    date: datetime
    character_class: str
    preset_no: str = Field(alias="use_preset_no")
    use_available: int = Field(alias="use_available_hyper_stat")
    preset1: list[HyperStatItem] = Field(alias="hyper_stat_preset_1")
    preset1_remain_point: int = Field(alias="hyper_stat_preset_1_remain_point")
    preset2: list[HyperStatItem] = Field(alias="hyper_stat_preset_2")
    preset2_remain_point: int = Field(alias="hyper_stat_preset_2_remain_point")
    preset3: list[HyperStatItem] = Field(alias="hyper_stat_preset_3")
    preset3_remain_point: int = Field(alias="hyper_stat_preset_3_remain_point")
