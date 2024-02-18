from datetime import datetime

from pydantic import BaseModel, Field

from maplestory.utils.repr import HideZeroStatRepresentation

from ..types import CharacterClass


class SymbolItem(HideZeroStatRepresentation, BaseModel):
    """캐릭터 심볼 장비 상세 정보

    Attributes:
        name (str): 심볼 이름
        icon (str): 심볼 아이콘
        description (str): 심볼 설명
        force (int): 심볼 포스 증가 수치
        level (int): 심볼 레벨
        STR (int): 심볼로 증가한 힘(STR)
        DEX (int): 심볼로 증가한 민첩(DEX)
        INT (int): 심볼로 증가한 지력(INT)
        LUK (int): 심볼로 증가한 운(LUK)
        HP (int): 심볼로 증가한 체력(HP)
        growth_count (int): 현재 보유 성장치
        require_growth_count (int): 다음 레벨까지 필요 성장치
    """

    name: str = Field(alias="symbol_name")
    icon: str = Field(alias="symbol_icon")
    description: str = Field(alias="symbol_description")
    force: int = Field(alias="symbol_force")
    level: int = Field(alias="symbol_level")
    STR: int = Field(alias="symbol_str")
    DEX: int = Field(alias="symbol_dex")
    INT: int = Field(alias="symbol_int")
    LUK: int = Field(alias="symbol_luk")
    HP: int = Field(alias="symbol_hp")
    growth_count: int = Field(alias="symbol_growth_count")
    require_growth_count: int = Field(alias="symbol_require_growth_count")


class SymbolEquipment(BaseModel):
    """캐릭터 심볼 정보

    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_class (CharacterClass): 캐릭터 직업
        symbol (list[SymbolItem]): 심볼 정보
    """

    date: datetime
    character_class: CharacterClass
    symbol: list[SymbolItem]
