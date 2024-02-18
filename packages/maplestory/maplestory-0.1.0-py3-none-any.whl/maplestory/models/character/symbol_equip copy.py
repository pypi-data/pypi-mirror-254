from datetime import datetime

from pydantic import BaseModel, Field

from maplestory.utils.repr import HideZeroStatRepresentation

from ..types import CharacterClass


class SymbolItem(HideZeroStatRepresentation, BaseModel):
    """캐릭터 심볼 장비 상세 정보

    Attributes:
        name: 심볼 이름
        icon: 심볼 아이콘
        description: 심볼 설명
        force: 심볼 포스 증가 수치
        level: 심볼 레벨
        str: 심볼로 증가한 힘(STR)
        dex: 심볼로 증가한 민첩(DEX)
        int: 심볼로 증가한 지력(INT)
        luk: 심볼로 증가한 운(LUK)
        hp: 심볼로 증가한 체력(HP)
        growth_count: 현재 보유 성장치
        require_growth_count: 다음 레벨까지 필요 성장치
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

    @property
    def cumulative_growth_count(self) -> int:
        # TODO: 누적 성장치
        return 0

    @property
    def available_max_level(self) -> int:
        # TODO: 누적 성장치로 달성 가능한 최대 레벨
        return 0

    @property
    def available_max_level_meso(self) -> int:
        # TODO: 누적 성장치로 달성 가능한 최대 레벨까지 내야 하는 메소 (밀린 세금)
        return 0


class SymbolEquipment(BaseModel):
    """캐릭터 심볼 정보

    Attributes:
        date: 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_class: 캐릭터 직업
        symbol: 심볼 정보
    """

    date: datetime
    character_class: CharacterClass
    symbol: list[SymbolItem]
