from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl

from maplestory.models.character.cashitem_equip import CashitemOption

from ..types import PetSkill


class PetAutoSkill(BaseModel):
    """펫 버프 자동 스킬 정보

    Attributes:
        skill_1 (str | None): 첫 번째 슬롯에 등록된 자동 스킬
        skill_1_icon (HttpUrl | None): 첫 번째 슬롯에 등록된 자동 스킬 아이콘
        skill_2 (str | None): 두 번째 슬롯에 등록된 자동 스킬
        skill_2_icon (HttpUrl | None): 두 번째 슬롯에 등록된 자동 스킬 아이콘
    """

    skill_1: str | None
    skill_1_icon: HttpUrl | None
    skill_2: str | None
    skill_2_icon: HttpUrl | None


class PetItemOption(CashitemOption):
    """펫 장비 아이템 옵션

    Attributes:
        type: 옵션 타입
        value: 옵션 값
    """


class PetItem(BaseModel):
    """캐릭터 펫 장착 정보

    Attributes:
        name (str | None): 아이템 명
        icon (HttpUrl | None): 아이템 아이콘
        description (str | None): 아이템 설명
        option (list[PetItemOption]): 아이템 표기상 옵션
        scroll_upgrade (int): 업그레이드 횟수
        scroll_upgradable (int): 업그레이드 가능 횟수
        shape (str | None): 아이템 외형
        shape_icon (HttpUrl | None): 아이템 외형 아이콘
    """

    name: str | None = Field(alias="item_name")
    icon: HttpUrl | None = Field(alias="item_icon")
    description: str | None = Field(alias="item_description")
    option: list[PetItemOption] = Field(alias="item_option")
    scroll_upgrade: int
    scroll_upgradable: int
    shape: str | None = Field(alias="item_shape")
    shape_icon: HttpUrl | None = Field(alias="item_shape_icon")


class CharacterPet(BaseModel):
    """캐릭터 펫 정보
    
    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)

        pet_1_name (str | None): 펫1 명
        pet_1_nickname (str | None): 펫1 닉네임
        pet_1_icon (HttpUrl | None): 펫1 아이콘
        pet_1_description (str | None): 펫1 설명
        pet_1_equipment (PetItem | None): 펫1 장착 정보
        pet_1_auto_skill (PetAutoSkill | None): 펫1 펫 버프 자동스킬 정보
        pet_1_pet_type (str | None): 펫1 원더 펫 종류
        pet_1_skill (list[PetSkill]): 펫1 펫 보유 스킬
        pet_1_date_expire (datetime | None): 펫1 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기)
        pet_1_appearance (str | None): 펫1 외형
        pet_1_appearance_icon (HttpUrl | None): 펫1 외형 아이콘

        pet_2_name (str | None): 펫2 명
        pet_2_nickname (str | None): 펫2 닉네임
        pet_2_icon (HttpUrl | None): 펫2 아이콘
        pet_2_description (str | None): 펫2 설명
        pet_2_equipment (PetItem | None): 펫2 장착 정보
        pet_2_auto_skill (PetAutoSkill | None): 펫2 펫 버프 자동스킬 정보
        pet_2_pet_type (str | None): 펫2 원더 펫 종류
        pet_2_skill (list[PetSkill]): 펫2 펫 보유 스킬
        pet_2_date_expire (datetime | None): 펫2 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기)
        pet_2_appearance (str | None): 펫2 외형
        pet_2_appearance_icon (HttpUrl | None): 펫2 외형 아이콘

        pet_3_name (str | None): 펫3 명
        pet_3_nickname (str | None): 펫3 닉네임
        pet_3_icon (HttpUrl | None): 펫3 아이콘
        pet_3_description (str | None): 펫3 설명
        pet_3_equipment (PetItem | None): 펫3 장착 정보
        pet_3_auto_skill (PetAutoSkill | None): 펫3 펫 버프 자동스킬 정보
        pet_3_pet_type (str | None): 펫3 원더 펫 종류
        pet_3_skill (list[PetSkill]): 펫3 펫 보유 스킬
        pet_3_date_expire (datetime | None): 펫3 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기)
        pet_3_appearance (str | None): 펫3 외형
        pet_3_appearance_icon (HttpUrl | None): 펫3 외형 아이콘
    """

    date: datetime

    pet_1_name: str | None
    pet_1_nickname: str | None
    pet_1_icon: HttpUrl | None
    pet_1_description: str | None
    pet_1_equipment: PetItem | None
    pet_1_auto_skill: PetAutoSkill | None
    pet_1_pet_type: str | None
    pet_1_skill: list[PetSkill]
    pet_1_date_expire: datetime | None
    pet_1_appearance: str | None
    pet_1_appearance_icon: HttpUrl | None

    pet_2_name: str | None
    pet_2_nickname: str | None
    pet_2_icon: HttpUrl | None
    pet_2_description: str | None
    pet_2_equipment: PetItem | None
    pet_2_auto_skill: PetAutoSkill | None
    pet_2_pet_type: str | None
    pet_2_skill: list[PetSkill]
    pet_2_date_expire: datetime | None
    pet_2_appearance: str | None
    pet_2_appearance_icon: HttpUrl | None

    pet_3_name: str | None
    pet_3_nickname: str | None
    pet_3_icon: HttpUrl | None
    pet_3_description: str | None
    pet_3_equipment: PetItem | None
    pet_3_auto_skill: PetAutoSkill | None
    pet_3_pet_type: str | None
    pet_3_skill: list[PetSkill]
    pet_3_date_expire: datetime | None
    pet_3_appearance: str | None
    pet_3_appearance_icon: HttpUrl | None
