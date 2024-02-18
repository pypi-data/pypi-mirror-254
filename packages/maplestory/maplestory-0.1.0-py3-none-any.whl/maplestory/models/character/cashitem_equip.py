from datetime import datetime

from pydantic import BaseModel, Field

from ..types import (
    CharacterClass,
    CharacterGender,
    ExpireDate,
    ItemGender,
    PresetNumber,
)


class CashItemColoringPrism(BaseModel):
    """캐시 장비 컬러링프리즘 정보

    Attributes:
        color_range: 컬러링프리즘 색상 범위
        hue: 컬러링프리즘 색상
        saturation: 컬러링프리즘 채도
        value: 컬러링프리즘 명도

    Examples:
        "color_range": "전체 색상 계열",
        "hue": 307,
        "saturation": -70,
        "value": 15
    """

    color_range: str
    hue: int
    saturation: int
    value: int


class CashitemOption(BaseModel):
    """캐시 장비 옵션

    Attributes:
        type: 옵션 종류
        value: 옵션 값
    """

    # TODO: None Check
    type: str = Field(alias="option_type")
    value: str = Field(alias="option_value")


class BaseCashItemPresetInfo(BaseModel):
    """캐시 장비 프리셋 정보

    Attributes:
        part: 캐시 장비 부위 명
        slot: 캐시 장비 슬롯 위치
        name: 캐시 장비 명
        icon: 캐시 장비 아이콘
        description: 캐시 장비 설명
        option: 캐시 장비 옵션
        date_expire: 아이템 유효기간 (KST)
        date_option_expire: 아이템 옵션 유효기간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기)
        label: 캐시 장비 라벨 정보
        coloring_prism: 캐시 장비 컬러링프리즘 정보
        gender: 아이템 장착 가능 성별
    """

    part: str = Field(alias="cash_item_equipment_part")
    slot: str = Field(alias="cash_item_equipment_slot")
    name: str = Field(alias="cash_item_name")
    icon: str = Field(alias="cash_item_icon")
    description: str | None = Field(alias="cash_item_description")
    option: list[CashitemOption] = Field(alias="cash_item_option")
    date_expire: ExpireDate
    date_option_expire: ExpireDate
    label: str | None = Field(alias="cash_item_label")
    coloring_prism: CashItemColoringPrism | None = Field(
        alias="cash_item_coloring_prism"
    )
    gender: ItemGender = Field(alias="item_gender")


class CashItemPresetInfo(BaseCashItemPresetInfo):
    """캐시 장비 프리셋 정보

    Attributes:
        part: 캐시 장비 부위 명
        slot: 캐시 장비 슬롯 위치
        name: 캐시 장비 명
        icon: 캐시 장비 아이콘
        description: 캐시 장비 설명
        option: 캐시 장비 옵션
        date_expire: 아이템 유효기간 (KST)
        date_option_expire: 아이템 옵션 유효기간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기)
        label: 캐시 장비 라벨 정보
        coloring_prism: 캐시 장비 컬러링프리즘 정보
        item_gender: 아이템 장착 가능 성별
        base_preset_item_disable_flag: 다른 프리셋에서 장비 추가 장착 없이 1번 프리셋의 장비 공유를 비활성화 했는지 여부
    """

    base_preset_item_disable_flag: str | None = None


class CashitemEquipment(BaseModel):
    """캐시 장비 정보

    Attributes:
        date: 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
            "2023-12-21T00:00+09:00"
        character_gender: 캐릭터 성별
        character_class: 캐릭터 직업
        preset_no: 적용 중인 캐시 장비 프리셋 번호
        items: 장착 중인 캐시 장비
        preset_1: 1번 프리셋 장착 캐시 장비 정보
        preset_2: 2번 프리셋 장착 캐시 장비 정보
        preset_3: 3번 프리셋 장착 캐시 장비 정보
        additional_items: 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에서 장착 중인 캐시 장비
        additional_preset_1: 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드의 1번 프리셋 장착 캐시 장비 정보
        additional_preset_2: 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드의 2번 프리셋 장착 캐시 장비 정보
        additional_preset_3: 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드의 3번 프리셋 장착 캐시 장비 정보
    """

    date: datetime
    character_gender: CharacterGender
    character_class: CharacterClass
    preset_no: PresetNumber
    items: list[BaseCashItemPresetInfo] = Field(alias="cash_item_equipment_base")
    preset_1: list[CashItemPresetInfo] = Field(alias="cash_item_equipment_preset_1")
    preset_2: list[CashItemPresetInfo] = Field(alias="cash_item_equipment_preset_2")
    preset_3: list[CashItemPresetInfo] = Field(alias="cash_item_equipment_preset_3")
    additional_items: list[BaseCashItemPresetInfo] = Field(
        alias="additional_cash_item_equipment_base"
    )
    additional_preset_1: list[CashItemPresetInfo] = Field(
        alias="additional_cash_item_equipment_preset_1"
    )
    additional_preset_2: list[CashItemPresetInfo] = Field(
        alias="additional_cash_item_equipment_preset_2"
    )
    additional_preset_3: list[CashItemPresetInfo] = Field(
        alias="additional_cash_item_equipment_preset_3"
    )
