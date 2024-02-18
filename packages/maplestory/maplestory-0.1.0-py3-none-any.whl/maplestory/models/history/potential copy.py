from datetime import datetime

from pydantic import BaseModel, Field

import maplestory.utils.kst as kst

from ..types import CubePotenialGrade, ItemSlotName, PageCursor, PotentialGrade

# KST_Timezone = Timezone("Asia/Seoul")
# PotentialDatetime = Annotated[datetime, KST_Timezone, Field(..., ge=POTENTIAL_MINIMUM_DATETIME)]
POTENTIAL_MINIMUM_DATETIME = kst.datetime(2024, 1, 25)


class PotentialOption(BaseModel):
    """잠재능력 옵션 정보

    Attributes:
        option: 옵션 명
        grade: 옵션 등급

    Examples:
        {
            "value": "최대 MP : +5%",
            "grade": "에픽"
        },
        {
            "value": "올스탯 : +5",
            "grade": "레어"
        },
        {
            "value": "점프력 : +5",
            "grade": "레어"
        }
        {
            "value": "STR : +6",
            "grade": "노멀"
        }
    """

    option: str = Field(alias="value")
    grade: CubePotenialGrade

    @property
    def name(self) -> str:
        return self.option.split(":")[0].strip()

    @property
    def value(self) -> int:
        return int(self.option.split(":")[1].replace("%", "").strip())

    @property
    def percent(self) -> bool:
        return self.option.endswith("%")


class CubeHistoryInfo(BaseModel):
    """큐브 사용 결과 정보

    Attributes:
        id: 큐브 히스토리 식별자
        character_name: 캐릭터명
        date_create: 사용 일시 (KST)
        cube_type: 사용 큐브
            "수상한 에디셔널 큐브", "수상한 큐브", ...
        item_upgrade_result: 사용 결과
        miracle_time_flag: 미라클 타임 적용 여부
            "이벤트 적용되지 않음", ...
        item_equipment_part: 장비 분류
        item_level: 장비 레벨
        target_item: 큐브 사용한 장비
        potential_option_grade: 잠재능력 등급
        additional_potential_option_grade: 에디셔널 잠재능력 등급
        upgrade_guarantee: 천장에 도달하여 확정 등급 상승한 여부
        upgrade_guarantee_count: 현재까지 쌓은 스택
        before_potential_option: 사용 전 잠재능력 옵션
        before_additional_potential_option: 사용 전 에디셔널 잠재능력 옵션
        after_potential_option: 사용 후 잠재능력 옵션
        after_additional_potential_option: 사용 후 에디셔널 잠재능력 옵션
    """

    id: str
    character_name: str
    date_create: datetime
    cube_type: str
    item_upgrade_result: str
    miracle_time_flag: str
    item_equipment_part: ItemSlotName
    item_level: int
    target_item: str
    potential_option_grade: PotentialGrade
    additional_potential_option_grade: PotentialGrade
    upgrade_guarantee: bool
    upgrade_guarantee_count: int
    before_potential_option: list[PotentialOption]
    before_additional_potential_option: list[PotentialOption]
    after_potential_option: list[PotentialOption]
    after_additional_potential_option: list[PotentialOption]

    @property
    def is_miracle_time(self) -> bool:
        return self.miracle_time_flag != "이벤트 적용되지 않음"


class CubeHistory(BaseModel):
    """큐브 사용 결과

    Attributes:
        count: 결과 건 수
        next_cursor: 페이징 처리를 위한 cursor
        history: 큐브 히스토리
    """

    count: int
    next_cursor: PageCursor | None
    history: list[CubeHistoryInfo] = Field(alias="cube_history")


class PotentialHistoryInfo(BaseModel):
    """

    Attributes:
        id: 잠재능력 재설정 히스토리 식별자
        character_name: 캐릭터 명
        date_create: 사용 일시 (KST), '2024-01-25T17:28:31.000+09:00'
        potential_type: 대상 잠재능력 타입 (잠재능력, 에디셔널 잠재능력)
        item_upgrade_result: 사용 결과
        miracle_time_flag: 미라클 타임 적용 여부
        item_equipment_part: 장비 분류
        item_level: 장비 레벨
        target_item: 잠재능력 재설정 장비 명
        potential_option_grade: 잠재능력 등급
        additional_potential_option_grade: 에디셔널 잠재능력 등급
        upgrade_guarantee: 천장에 도달하여 확정 등급 상승한 여부
        upgrade_guarantee_count: 현재까지 쌓은 스택
        before_potential_option: 사용 전 잠재능력 옵션
        before_additional_potential_option: 사용 전 에디셔널 잠재능력 옵션
        after_potential_option: 사용 후 잠재능력 옵션
        after_additional_potential_option: 사용 후 에디셔널 잠재능력 옵션
    """

    id: str
    character_name: str
    date_create: datetime
    potential_type: str
    item_upgrade_result: str
    miracle_time_flag: str
    item_equipment_part: str
    item_level: float
    target_item: str
    potential_option_grade: str
    additional_potential_option_grade: str
    upgrade_guarantee: bool
    upgrade_guarantee_count: float
    before_potential_option: list[PotentialOption]
    before_additional_potential_option: list[PotentialOption]
    after_potential_option: list[PotentialOption]
    after_additional_potential_option: list[PotentialOption]


class PotentialHistory(BaseModel):
    """

    Attributes:
        count: 결과 건 수
        next_cursor: 페이징 처리를 위한 cursor
        history: 잠재능력 재설정 히스토리
    """

    count: float
    next_cursor: PageCursor | None
    history: list[PotentialHistoryInfo] = Field(alias="potential_history")
