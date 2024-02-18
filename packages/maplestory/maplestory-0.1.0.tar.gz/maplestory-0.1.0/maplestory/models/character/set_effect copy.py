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
    
    Examples:
        {
            "date": "2024-01-25T00:00+09:00",
            "set_effect": [
                {
                    "set_name": "루타비스 세트(전사)",
                    "total_set_count": 2,
                    "set_effect_info": [
                        {
                            "set_count": 2,
                            "set_option": "STR : +20, DEX : +20, 최대 HP : +1000, 최대 MP : +1000"
                        }
                    ]
                },
                {
                    "set_name": "마이스터 세트",
                    "total_set_count": 1,
                    "set_effect_info": []
                },
                {
                    "set_name": "보스 장신구 세트",
                    "total_set_count": 6,
                    "set_effect_info": [
                        {
                            "set_count": 3,
                            "set_option": "올스탯 : +10, 최대 HP : +5%, 최대 MP : +5%, 공격력 : +5, 마력 : +5"
                        },
                        {
                            "set_count": 5,
                            "set_option": "올스탯 : +10, 최대 HP : +5%, 최대 MP : +5%, 공격력 : +5, 마력 : +5"
                        }
                    ]
                },
                {
                    "set_name": "앱솔랩스 세트(전사)",
                    "total_set_count": 4,
                    "set_effect_info": [
                        {
                            "set_count": 2,
                            "set_option": "최대 HP : +1500, 최대 MP : +1500, 공격력 : +20, 마력 : +20, 보스 몬스터 공격 시 데미지 : +10%"
                        },
                        {
                            "set_count": 3,
                            "set_option": "올스탯 : +30, 공격력 : +20, 마력 : +20, 보스 몬스터 공격 시 데미지 : +10%"
                        },
                        {
                            "set_count": 4,
                            "set_option": "공격력 : +25, 마력 : +25, 방어력 : +200, 몬스터 방어율 무시 : +10%"
                        }
                    ]
                },
                {
                    "set_name": "아케인셰이드 세트(전사)",
                    "total_set_count": 1,
                    "set_effect_info": []
                }
            ]
        }
    """

    date: datetime
    set_effect: list[SetEffectInfo]
