from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl, field_validator

from ..types import (
    CharacterClass,
    CharacterGender,
    ItemGender,
    ItemOptionValue,
    ItemSlotName,
    PotentialGrade,
    PotentialOption,
    PresetNumber,
)


class ItemAddOption(BaseModel):
    """장비 추가 옵션

    Attributes:
        STR: STR
        DEX: DEX
        INT: INT
        LUK: LUK
        max_hp: 최대 HP
        max_mp: 최대 MP
        attack_power: 공격력
        magic_power: 마력
        armor: 방어력
        speed: 이동속도
        jump: 점프력
        boss_damage: 보스 몬스터 공격 시 데미지(%)
        damage: 데미지(%)
        all_stat: 올스탯(%)
        equipment_level_decrease: 장비 레벨 감소
    """

    str: ItemOptionValue
    int: ItemOptionValue
    dex: ItemOptionValue
    luk: ItemOptionValue
    max_hp: ItemOptionValue
    max_mp: ItemOptionValue
    attack_power: ItemOptionValue
    magic_power: ItemOptionValue
    armor: ItemOptionValue
    speed: ItemOptionValue
    jump: ItemOptionValue
    boss_damage: ItemOptionValue
    damage: ItemOptionValue
    all_stat: ItemOptionValue
    equipment_level_decrease: ItemOptionValue


class ItemBaseOption(BaseModel):
    """캐릭터 장비 기본 옵션 정보

    Attributes:
        str: STR
        dex: DEX
        int: INT
        luk: LUK
        max_hp: 최대 HP
        max_mp: 최대 MP
        attack_power: 공격력
        magic_power: 마력
        armor: 방어력
        speed: 이동속도
        jump: 점프력
        boss_damage: 보스 몬스터 공격 시 데미지(%)
        ignore_monster_armor: 몬스터방어율 무시(%)
        all_stat: 올스탯(%)
        max_hp_rate: 최대 HP(%)
        max_mp_rate: 최대 MP(%)
        base_equipment_level: 기본 착용 레벨
    """

    str: ItemOptionValue
    int: ItemOptionValue
    dex: ItemOptionValue
    luk: ItemOptionValue
    max_hp: ItemOptionValue
    max_mp: ItemOptionValue
    attack_power: ItemOptionValue
    magic_power: ItemOptionValue
    armor: ItemOptionValue
    speed: ItemOptionValue
    jump: ItemOptionValue
    boss_damage: ItemOptionValue
    ignore_monster_armor: ItemOptionValue
    all_stat: ItemOptionValue
    max_hp_rate: ItemOptionValue
    max_mp_rate: ItemOptionValue
    base_equipment_level: ItemOptionValue


class ItemEtcOption(BaseModel):
    """장비 기타 옵션 정보

    Attributes:
        str: STR
        dex: DEX
        int: INT
        luk: LUK
        max_hp: 최대 HP
        max_mp: 최대 MP
        attack_power: 공격력
        magic_power: 마력
        armor: 방어력
        speed: 이동속도
        jump: 점프력
    """

    str: ItemOptionValue
    int: ItemOptionValue
    dex: ItemOptionValue
    luk: ItemOptionValue
    max_hp: ItemOptionValue
    max_mp: ItemOptionValue
    attack_power: ItemOptionValue
    magic_power: ItemOptionValue
    armor: ItemOptionValue
    speed: ItemOptionValue
    jump: ItemOptionValue


class ItemExceptionalOption(BaseModel):
    """장비 익셉셔널 옵션 정보

    Attributes:
        STR: STR
        DEX: DEX
        INT: INT
        LUK: LUK
        max_hp: 최대 HP
        max_mp: 최대 MP
        attack_power: 공격력
        magic_power: 마력
    """

    str: ItemOptionValue
    int: ItemOptionValue
    dex: ItemOptionValue
    luk: ItemOptionValue
    max_hp: ItemOptionValue
    max_mp: ItemOptionValue
    attack_power: ItemOptionValue
    magic_power: ItemOptionValue


class ItemTotalOption(BaseModel):
    """장비 최종 옵션 정보

    Attributes:
        STR: STR
        INT: INT
        DEX: DEX
        LUK: LUK
        max_hp: 최대 HP
        max_mp: 최대 MP
        attack_power: 공격력
        magic_power: 마력
        armor: 방어력
        speed: 이동속도
        jump: 점프력
        boss_damage: 보스 몬스터 공격 시 데미지(%)
        ignore_monster_armor: 몬스터방어율 무시(%)
        all_stat: 올스탯(%)
        damage: 데미지(%)
        max_hp_rate: 최대 HP(%)
        max_mp_rate: 최대 MP(%)
        equipment_level_decrease: 장비 레벨 감소
    """

    str: ItemOptionValue
    int: ItemOptionValue
    dex: ItemOptionValue
    luk: ItemOptionValue
    max_hp: ItemOptionValue
    max_mp: ItemOptionValue
    attack_power: ItemOptionValue
    magic_power: ItemOptionValue
    armor: ItemOptionValue
    speed: ItemOptionValue
    jump: ItemOptionValue
    boss_damage: ItemOptionValue
    ignore_monster_armor: ItemOptionValue
    all_stat: ItemOptionValue
    damage: ItemOptionValue
    max_hp_rate: ItemOptionValue
    max_mp_rate: ItemOptionValue
    equipment_level_decrease: ItemOptionValue


class ItemStarforceOption(BaseModel):
    """캐릭터 장비 스타포스 옵션 정보

    Attributes:
        STR: STR
        DEX: DEX
        INT: INT
        LUK: LUK
        max_hp: 최대 HP
        max_mp: 최대 MP
        attack_power: 공격력
        magic_power: 마력
        armor: 방어력
        speed: 이동속도
        jump: 점프력
    """

    str: ItemOptionValue
    int: ItemOptionValue
    dex: ItemOptionValue
    luk: ItemOptionValue
    max_hp: ItemOptionValue
    max_mp: ItemOptionValue
    attack_power: ItemOptionValue
    magic_power: ItemOptionValue
    armor: ItemOptionValue
    speed: ItemOptionValue
    jump: ItemOptionValue


class BaseEquipmentInfo(BaseModel):
    """기본 장비 정보

    Attributes:
        item_equipment_part: 장비 부위 명
        item_equipment_slot: 장비 슬롯 위치
        item_name: 장비 명
        item_icon: 장비 아이콘
        item_description: 장비 설명
        item_shape_name: 장비 외형
        item_shape_icon: 장비 외형 아이콘
        item_gender: 장비 전용 성별
        item_total_option: 장비 최종 옵션
        item_base_option: 장비 기본 옵션
        item_add_option: 장비 추가 옵션
        item_etc_option: 장비 기타 옵션
        item_exceptional_option: 장비 익셉셔널 옵션
        equipment_level_increase: 장비 레벨 증가
        growth_exp: 성장 경험치
        growth_level: 성장 레벨
        scroll_upgrade: 업그레이드 횟수
        cuttable_count: 가위 사용 가능 횟수 (교환 불가 장비, 가위 횟수가 없는 교환 가능 장비는 255)
        golden_hammer_flag: 황금 망치 재련 적용 (1:적용, 이외 미 적용)
        scroll_resilience_count: 복구 가능 횟수
        scroll_upgradeable_count: 업그레이드 가능 횟수
        soul_name: 소울 명
        soul_option: 소울 옵션
        starforce: 스타포스 강화 단계
        starforce_scroll_flag: 놀라운 장비 강화 주문서 사용 여부 (0:미사용, 1:사용)
        item_starforce_option 장비 스타포스 옵션
        special_ring_level: 특수 반지 레벨
        date_expire: 장비 유효 기간 (KST) '2023-12-21T17:28+09:00'
    """

    part: str = Field(alias="item_equipment_part")
    slot: ItemSlotName = Field(alias="item_equipment_slot")
    name: str = Field(alias="item_name")
    icon: HttpUrl = Field(alias="item_icon")
    description: str | None = Field(alias="item_description")
    shape_name: str = Field(alias="item_shape_name")
    shape_icon: HttpUrl = Field(alias="item_shape_icon")
    gender: ItemGender = Field(alias="item_gender")
    total_option: ItemTotalOption = Field(alias="item_total_option")
    base_option: ItemBaseOption = Field(alias="item_base_option")
    add_option: ItemAddOption = Field(alias="item_add_option")
    etc_option: ItemEtcOption = Field(alias="item_etc_option")
    exceptional_option: ItemExceptionalOption = Field(alias="item_exceptional_option")
    starforce_option: ItemStarforceOption = Field(alias="item_starforce_option")
    equipment_level_increase: int
    growth_exp: int
    growth_level: int
    scroll_upgrade: int
    cuttable_count: int | None
    golden_hammer_flag: bool
    scroll_resilience_count: int
    scroll_upgradeable_count: int
    soul_name: str | None
    soul_option: str | None
    starforce: int
    starforce_scroll_flag: bool
    special_ring_level: int
    date_expire: datetime | None

    @field_validator("cuttable_count", mode="before")
    @classmethod
    def validate_cuttable_count(cls, v: str | int) -> int | None:
        v = int(v)
        return None if v == 255 else v

    @field_validator("golden_hammer_flag", mode="before")
    @classmethod
    def validate_golden_hammer_flag(cls, v: str | int) -> bool:
        match v:
            case "미적용" | "0" | 0:
                return False
            case "적용" | "1" | 1:
                return True
            case _:
                raise ValueError(f"Unexpected value on golden_hammer_flag: {v!r}")

    @field_validator("starforce_scroll_flag", mode="before")
    @classmethod
    def validate_starforce_scroll_flag(cls, v: str | int) -> bool:
        match v:
            case "미사용" | "0" | 0:
                return False
            case "사용" | "1" | 1:
                return True
            case _:
                raise ValueError(f"Unexpected value on starforce_scroll_flag: {v!r}")


class DragonEquipmentInfo(BaseEquipmentInfo):
    """에반 드래곤 장비 정보"""

class MechanicEquipmentInfo(BaseEquipmentInfo):
    """메카닉 장비 정보"""

class EquipmentInfo(BaseEquipmentInfo):
    """장비 정보

    Attributes:
        potential_grade: 잠재 옵션 등급
        potential_option_1: 잠재 옵션 첫번째 옵션
        potential_option_2: 잠재 옵션 두번째 옵션
        potential_option_3: 잠재 옵션 세번째 옵션
        additional_grade: 에디셔널 잠재 옵션 등급
        additional_option_1: 에디셔널 잠재 첫번째 옵션
        additional_option_2: 에디셔널 잠재 두번째 옵션
        additional_option_3: 에디셔널 잠재 세번째 옵션

        -- 이후는 상속된 속성
        item_equipment_part: 장비 부위 명
        item_equipment_slot: 장비 슬롯 위치
        item_name: 장비 명
        item_icon: 장비 아이콘
        item_description: 장비 설명
        item_shape_name: 장비 외형
        item_shape_icon: 장비 외형 아이콘
        item_gender: 장비 전용 성별
        item_total_option: 장비 최종 옵션
        item_base_option: 장비 기본 옵션
        equipment_level_increase: 장비 레벨 증가
        item_exceptional_option: 장비 익셉셔널 옵션
        item_add_option: 장비 추가 옵션
        growth_exp: 성장 경험치
        growth_level: 성장 레벨
        scroll_upgrade: 업그레이드 횟수
        cuttable_count: 가위 사용 가능 횟수 (교환 불가 장비, 가위 횟수가 없는 교환 가능 장비는 255)
        golden_hammer_flag: 황금 망치 재련 적용 (1:적용, 이외 미 적용)
        scroll_resilience_count: 복구 가능 횟수
        scroll_upgradeable_count: 업그레이드 가능 횟수
        soul_name: 소울 명
        soul_option: 소울 옵션
        item_etc_option: 장비 기타 옵션
        starforce: 스타포스 강화 단계
        starforce_scroll_flag: 놀라운 장비 강화 주문서 사용 여부 (0:미사용, 1:사용)
        item_starforce_option 장비 스타포스 옵션
        special_ring_level: 특수 반지 레벨
        date_expire: 장비 유효 기간 (KST)
    """

    potential_grade: PotentialGrade = Field(alias="potential_option_grade")
    potential_option_1: PotentialOption = Field(alias="potential_option_1")
    potential_option_2: PotentialOption = Field(alias="potential_option_2")
    potential_option_3: PotentialOption = Field(alias="potential_option_3")

    additional_grade: PotentialGrade = Field(alias="additional_potential_option_grade")
    additional_option_1: PotentialOption = Field(alias="additional_potential_option_1")
    additional_option_2: PotentialOption = Field(alias="additional_potential_option_2")
    additional_option_3: PotentialOption = Field(alias="additional_potential_option_3")

    @property
    def potential_options(self) -> list[PotentialOption]:
        return [
            self.potential_option_1,
            self.potential_option_2,
            self.potential_option_3,
        ]

    @property
    def additional_options(self) -> list[PotentialOption]:
        return [
            self.additional_option_1,
            self.additional_option_2,
            self.additional_option_3,
        ]


class EquipmentTitle(BaseModel):
    """캐릭터 칭호 아이템 정보

    Attributes:
        name (str): 칭호 명
        icon (HttpUrl): 칭호 아이콘
        description (str): 칭호 설명
        date_expire (datetime | None): 칭호 유효 기간
        date_option_expire (datetime | Literal["expired"] | None): 칭호 옵션 유효 기간 (expired:만료, null:무제한) (KST)
    """

    name: str = Field(alias="title_name")
    icon: HttpUrl = Field(alias="title_icon")
    description: str = Field(alias="title_description")
    date_expire: datetime | None
    date_option_expire: datetime | Literal["expired"] | None


class CharacterEquipment(BaseModel):
    """캐릭터 장비 정보

    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_gender (CharacterGender): 캐릭터 성별
        character_class (CharacterClass): 캐릭터 직업
        items (list[EquipmentInfo]): 장비 정보
        dragon_items (list[DragonEquipmentInfo]): 에반 드래곤 장비 정보 (에반인 경우 응답)
        mechanic_items (list[MechanicEquipmentInfo]): 메카닉 장비 정보 (메카닉인 경우 응답)
        title (EquipmentTitle | None): 칭호 정보
        preset_no (PresetNumber): 적용 중인 어빌리티 프리셋 번호
        preset1 (list[EquipmentInfo]): 1번 프리셋 장비 정보
        preset2 (list[EquipmentInfo]): 2번 프리셋 장비 정보
        preset3 (list[EquipmentInfo]): 3번 프리셋 장비 정보
    """

    date: datetime
    character_gender: CharacterGender
    character_class: CharacterClass
    items: list[EquipmentInfo] = Field(alias="item_equipment")
    dragon_items: list[DragonEquipmentInfo] = Field(alias="dragon_equipment")
    mechanic_items: list[MechanicEquipmentInfo] = Field(alias="mechanic_equipment")
    title: EquipmentTitle | None
    preset_no: PresetNumber
    preset1: list[EquipmentInfo] = Field(alias="item_equipment_preset1")
    preset2: list[EquipmentInfo] = Field(alias="item_equipment_preset2")
    preset3: list[EquipmentInfo] = Field(alias="item_equipment_preset3")
