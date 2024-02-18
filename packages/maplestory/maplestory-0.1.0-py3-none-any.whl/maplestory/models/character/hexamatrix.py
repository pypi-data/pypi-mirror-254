from datetime import datetime

from pydantic import BaseModel


class HexaMatrixLinkedSkill(BaseModel):
    """연결된 스킬 정보

    Attributes:
        hexa_skill_id (str): HEXA 스킬 ID
    """

    hexa_skill_id: str


class HexaMatrixCore(BaseModel):
    """HEXA 코어 상세 정보

    Attributes:
        hexa_core_name (str): 코어 명
        hexa_core_level (int): 코어 레벨
        hexa_core_type (str): 코어 타입
        linked_skill (list[HexaMatrixLinkedSkill]): 연결된 스킬
    """

    hexa_core_name: str
    hexa_core_level: int
    hexa_core_type: str
    linked_skill: list[HexaMatrixLinkedSkill]


class HexaMatrix(BaseModel):
    """HEXA 코어 정보

    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_hexa_core_equipment (list[HexaMatrixCore] | None): HEXA 코어 정보

    Notes:
        HEXA 코어 정보가 없는 경우 None으로 표기됩니다.
    """

    date: datetime
    character_hexa_core_equipment: list[HexaMatrixCore] | None
