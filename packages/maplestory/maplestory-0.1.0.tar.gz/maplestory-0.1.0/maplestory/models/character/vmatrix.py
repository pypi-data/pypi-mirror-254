from datetime import datetime

from pydantic import BaseModel, Field

from maplestory.utils.repr import HideNoneRepresentation


class VMatrixCore(HideNoneRepresentation, BaseModel):
    """V코어 정보

    Attributes:
        slot_id: 슬롯 인덱스
        slot_level: 슬롯 레벨
        v_core_name: 코어 명
        v_core_type: 코어 타입
            "강화코어" | "스킬코어" | "특수코어" | null
        v_core_level: 코어 레벨
        v_core_skill_1: 코어에 해당하는 스킬 명
        v_core_skill_2: (강화 코어인 경우) 코어에 해당하는 두 번째 스킬 명
        v_core_skill_3: (강화 코어인 경우) 코어에 해당하는 세 번째 스킬 명

    Notes:
        슬롯에 장작한 코어가 없는 경우, 코어 명과 코어 레벨도 None으로 표기합니다.
    """

    slot_id: int
    slot_level: int
    v_core_name: str | None
    v_core_type: str | None
    v_core_level: int
    v_core_skill_1: str | None
    v_core_skill_2: str | None
    v_core_skill_3: str | None


class VMatrix(BaseModel):
    """V매트릭스 정보

    Attributes:
        date: 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_class: 캐릭터 직업
        cores: V코어 정보
        remain_slot_upgrade_point: 캐릭터 잔여 매트릭스 강화 포인트
    """

    date: datetime
    character_class: str | None
    cores: list[VMatrixCore] = Field(alias="character_v_core_equipment")
    remain_slot_upgrade_point: int | None = Field(
        alias="character_v_matrix_remain_slot_upgrade_point"
    )
