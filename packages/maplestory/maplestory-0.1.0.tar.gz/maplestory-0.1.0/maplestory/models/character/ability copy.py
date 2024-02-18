from datetime import datetime
from pydantic import BaseModel, Field

from maplestory.types.character import AbilityNumber

from ..types import Grade, PresetNumber


class AbilityInfoItem(BaseModel):
    """어빌리티 한 줄 정보

    Attributes:
        number (int): 어빌리티 번호 (몇 번째 줄인지)
        grade (str): 어빌리티 등급
        value (str): 어빌리티 옵션 및 수치
    """

    number: AbilityNumber = Field(alias="ability_no")
    grade: Grade = Field(alias="ability_grade")
    value: str = Field(alias="ability_value")


class AbilityPreset(BaseModel):
    """어빌리티 프리셋 정보

    Attributes:
        grade (str): 어빌리티 프리셋의 어빌리티 등급
        info: 어빌리티 프리셋 정보
    """

    grade: Grade = Field(alias="ability_preset_grade")
    info: list[AbilityInfoItem] = Field(alias="ability_info")


class Ability(BaseModel):
    """어빌리티 정보

    Attributes:
        date: 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        grade: 어빌리티 등급
        info: 어빌리티 정보
        remain_fame: 보유 명성치
        preset_no: 적용 중인 어빌리티 프리셋 번호(number)
        preset1: 어빌리티 1번 프리셋 정보
        preset2: 어빌리티 2번 프리셋 정보
        preset3: 어빌리티 3번 프리셋 정보
    """

    date: datetime
    grade: Grade = Field(alias="ability_grade")
    info: list[AbilityInfoItem] = Field(alias="ability_info")
    remain_fame: int
    preset_no: PresetNumber
    preset1: AbilityPreset = Field(alias="ability_preset_1")
    preset2: AbilityPreset = Field(alias="ability_preset_2")
    preset3: AbilityPreset = Field(alias="ability_preset_3")

    # TODO: 어빌리티 재설정 몇 번 가능한지
    # @property
