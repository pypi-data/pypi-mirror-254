from datetime import datetime

from pydantic import BaseModel


class SetEffectOptionInfo(BaseModel):
    """세트 효과 옵션 정보

    Attributes:
        set_count (int): 세트 효과 레벨 (장비 수)
        set_option (str): 적용 중인 세트 효과
    """

    set_count: int
    set_option: str


class SetEffectInfo(BaseModel):
    """세트 효과 정보

    Attributes:
        set_name (str): 세트 효과 명
        total_set_count (int): 세트 개수 (럭키 아이템 포함)
        set_effect_info (list[SetEffectOptionInfo]): 세트 효과 옵션
    """

    set_name: str
    total_set_count: int
    set_effect_info: list[SetEffectOptionInfo]


class SetEffect(BaseModel):
    """세트 효과 정보

    Attributes:
        date (datetime): 조회 기준일
        set_effect (list[SetEffectInfo]): 세트 효과 정보
    """

    date: datetime
    set_effect: list[SetEffectInfo]
