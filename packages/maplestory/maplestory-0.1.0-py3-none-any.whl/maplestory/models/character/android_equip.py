from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, HttpUrl, field_validator

from ..types import AndroidGender, ExpireDate, ItemGender, LabelName, PresetNumber


class AndroidHair(BaseModel):
    """안드로이드 헤어 정보

    Attributes:
        hair_name: 안드로이드 헤어 명
        base_color: 안드로이드 헤어 베이스 컬러
        mix_color: 안드로이드 헤어 믹스 컬러
        mix_rate: 안드로이드 헤어 믹스 컬러의 염색 비율

    Examples:
        "hair_name": "검은색 방울꽃 헤어",
        "base_color": "검은색",
        "mix_color": null,
        "mix_rate": "0"
    """

    hair_name: str | None
    base_color: str | None
    mix_color: str | None
    mix_rate: int


class AndroidFace(BaseModel):
    """안드로이드 성형 정보

    Attributes:
        face_name: 안드로이드 성형 명
        base_color: 안드로이드 성형 베이스 컬러
        mix_color: 안드로이드 성형 믹스 컬러
        mix_rate: 안드로이드 성형 믹스 컬러의 염색 비율

    Examples:
        "face_name": "어제 울었어 얼굴",
        "base_color": "검은색",
        "mix_color": null,
        "mix_rate": "0"
    """

    face_name: str | None
    base_color: str | None
    mix_color: str | None
    mix_rate: int


class AndroidCashItemColoringPrism(BaseModel):
    """안드로이드 캐시아이템 컬러링프리즘 정보

    Attributes:
        color_range: 컬러링프리즘 색상 범위
        hue: 컬러링프리즘 색조
        saturation: 컬러링프리즘 채도
        value: 컬러링프리즘 명도
    """

    color_range: str
    hue: int
    saturation: int
    value: int


class AndroidCashItemOption(BaseModel):
    """안드로이드 캐시아이템 옵션

    Attributes:
        type: 옵션 타입
        value: 옵션 값
    """

    type: str = Field(alias="option_type")
    value: str = Field(alias="option_value")


class AndroidCashItem(BaseModel):
    """안드로이드 캐시 아이템 장착 정보

    Attributes:
        part: 안드로이드 캐시 아이템 부위 명
        slot: 안드로이드 캐시 아이템 슬롯 위치
        name: 안드로이드 캐시 아이템 명
        icon: 안드로이드 캐시 아이템 아이콘
        description: 안드로이드 캐시 아이템 옵션
        option: 안드로이드 캐시 아이템 옵션
        date_expire: 안드로이드 캐시 아이템 유효기간 (KST)
        date_option_expire: 안드로이드 캐시 아이템 옵션 유효기간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기)
        label: 안드로이드 캐시 아이템 라벨 정보 (스페셜라벨, 레드라벨, 블랙라벨, 마스터라벨)
        coloring_prism: 안드로이드 아이템 컬러링프리즘 정보
        gender: 아이템 장착 가능 성별
    """

    part: str = Field(alias="cash_item_equipment_part")
    slot: str = Field(alias="cash_item_equipment_slot")
    name: str = Field(alias="cash_item_name")
    icon: str = Field(alias="cash_item_icon")
    description: str | None = Field(alias="cash_item_description")
    option: list[AndroidCashItemOption] = Field(alias="cash_item_option")
    date_expire: ExpireDate
    date_option_expire: ExpireDate
    label: LabelName = Field(alias="cash_item_label")
    coloring_prism: AndroidCashItemColoringPrism | None = Field(
        alias="cash_item_coloring_prism"
    )
    gender: ItemGender = Field(alias="android_item_gender")


class AndroidPreset(BaseModel):
    """안드로이드 프리셋 정보

    Attributes:
        name: 안드로이드 명
        nickname: 안드로이드 닉네임
        icon: 안드로이드 아이콘
        description: 안드로이드 아이템 설명
        gender: 안드로이드 성별
        grade: 안드로이드 등급
        skin_name: 안드로이드 피부
        hair: 안드로이드 헤어 정보
        face: 안드로이드 성형 정보
        ear_sensor_clip_flag: 안드로이드 이어센서 클립 적용 여부
        non_humanoid_flag: 비인간형 안드로이드 여부
        shop_usable_flag: 잡화상점 기능 이용 가능 여부
    """

    name: str = Field(alias="android_name")
    nickname: str | None = Field(alias="android_nickname")
    icon: str = Field(alias="android_icon")
    description: str = Field(alias="android_description")
    gender: str = Field(alias="android_gender")
    grade: str = Field(alias="android_grade")
    skin_name: str | None = Field(alias="android_skin_name")
    hair: AndroidHair = Field(alias="android_hair")
    face: AndroidFace = Field(alias="android_face")
    ear_sensor_clip_flag: str = Field(alias="android_ear_sensor_clip_flag")
    non_humanoid_flag: str = Field(alias="android_non_humanoid_flag")
    shop_usable_flag: str = Field(alias="android_shop_usable_flag")


# FIXME: android_non_humanoid_flag가 null로 잘못 나오는 경우가 있음.
# FIXME: android_shop_usable_flag가 null로 잘못 나오는 경우가 있음.
# FIXME: android_preset_1에는 인간형, 가능인데, 현재 적용되어 있는 값에는 null, null임.
class AndroidEquipment(BaseModel):
    """안드로이드 장비 정보

    Attributes:
        date: 조회 기준일 (KST)
        name: 안드로이드 명
        nickname: 안드로이드 닉네임
        icon: 안드로이드 아이콘
        description: 안드로이드 아이템 설명
        hair: 안드로이드 헤어 정보
        face: 안드로이드 성형 정보
        skin_name: 안드로이드 피부 명
        cash_item_equipment: 안드로이드 캐시 아이템 장착 정보
        ear_sensor_clip_flag: 안드로이드 이어센서 클립 적용 여부 (미적용, 적용)
        gender: 안드로이드 성별
        grade: 안드로이드 등급
        non_humanoid_flag: 비인간형 안드로이드 여부 (인간형, 비인간형)
        shop_usable_flag: 잡화상점 기능 이용 가능 여부 (가능, 불가능)
        preset_no: 적용 중인 장비 프리셋 번호(number)
        preset_1: 1번 프리셋 안드로이드 정보
        preset_2: 2번 프리셋 안드로이드 정보
        preset_3: 3번 프리셋 안드로이드 정보
    """

    date: datetime
    name: str | None = Field(alias="android_name")
    nickname: str | None = Field(alias="android_nickname")
    icon: HttpUrl | None = Field(alias="android_icon")
    description: str | None = Field(alias="android_description")
    hair: AndroidHair = Field(alias="android_hair")
    face: AndroidFace = Field(alias="android_face")
    skin_name: str | None = Field(alias="android_skin_name")
    cash_item_equipment: list[AndroidCashItem] = Field(
        alias="android_cash_item_equipment"
    )
    ear_sensor_clip: bool = Field(alias="android_ear_sensor_clip_flag")
    gender: AndroidGender = Field(alias="android_gender")
    grade: str | None = Field(alias="android_grade")
    non_humanoid: str | None = Field(alias="android_non_humanoid_flag")
    shop_usable: bool | None = Field(alias="android_shop_usable_flag")
    preset_no: PresetNumber
    preset_1: AndroidPreset | None = Field(alias="android_preset_1")
    preset_2: AndroidPreset | None = Field(alias="android_preset_2")
    preset_3: AndroidPreset | None = Field(alias="android_preset_3")

    @field_validator("ear_sensor_clip", mode="before")
    @classmethod
    def change_ear_sensor_clip(cls, v: Any) -> bool | None:
        match v:
            case "미적용" | "0" | 0:
                return False
            case "적용" | "1" | 1:
                return True
            case _:
                return v

    @field_validator("shop_usable", mode="before")
    @classmethod
    def change_shop_usable(cls, v: Any) -> bool | None:
        match v:
            case "불가능" | "0" | 0:
                return False
            case "가능" | "1" | 1:
                return True
            case _:
                return v

    @property
    def is_humanoid(self) -> bool:
        return self.non_humanoid == "인간형"


# E       pydantic_core._pydantic_core.ValidationError: 2 validation errors for AndroidEquipment
# E       android_ear_sensor_clip_flag
# E         Input should be a valid string [type=string_type, input_value=False, input_type=bool]
# E           For further information visit https://errors.pydantic.dev/2.5/v/string_type
# E       android_shop_usable_flag
# E         Value error, Unexpected value on shop_usable_flag: None [type=value_error, input_value=None, input_type=NoneType]
# E           For further information visit https://errors.pydantic.dev/2.5/v/value_error
