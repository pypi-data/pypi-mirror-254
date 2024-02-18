from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl

from ..types import CharacterClass, LinkSkillLevel


class LinkSkill(BaseModel):
    """링크 스킬 정보

    Attributes:
        name (str): 스킬 명
        description (str): 스킬 설명
        level (LinkSkillLevel): 스킬 레벨
        effect (str): 스킬 효과
        icon (HttpUrl): 스킬 아이콘
    """

    name: str = Field(alias="skill_name")
    description: str = Field(alias="skill_description")
    level: LinkSkillLevel = Field(alias="skill_level")
    effect: str = Field(alias="skill_effect")
    icon: HttpUrl = Field(alias="skill_icon")


class CharacterLinkSkill(BaseModel):
    """캐릭터 링크 스킬 정보
    
    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_class (CharacterClass): 캐릭터 직업
        link_skill (list[LinkSkill]): 링크 스킬 정보
        owned_link_skill (LinkSkill | None): 내 링크 스킬 정보
        link_skill_preset_1 (list[LinkSkill]): 링크 스킬 1번 프리셋 정보
        link_skill_preset_2 (list[LinkSkill]): 링크 스킬 2번 프리셋 정보
        link_skill_preset_3 (list[LinkSkill]): 링크 스킬 3번 프리셋 정보
        owned_link_skill_preset_1 (LinkSkill | None): 내 링크 스킬 1번 프리셋 정보
        owned_link_skill_preset_2 (LinkSkill | None): 내 링크 스킬 2번 프리셋 정보
        owned_link_skill_preset_3 (LinkSkill | None): 내 링크 스킬 3번 프리셋 정보
    """

    date: datetime
    character_class: CharacterClass
    link_skill: list[LinkSkill] = Field(alias="character_link_skill")
    owned_link_skill: LinkSkill = Field(alias="character_owned_link_skill")
    link_skill_preset_1: list[LinkSkill] = Field(alias="character_link_skill_preset_1")
    link_skill_preset_2: list[LinkSkill] = Field(alias="character_link_skill_preset_2")
    link_skill_preset_3: list[LinkSkill] = Field(alias="character_link_skill_preset_3")
    owned_link_skill_preset_1: LinkSkill | None = Field(
        alias="character_owned_link_skill_preset_1"
    )
    owned_link_skill_preset_2: LinkSkill | None = Field(
        alias="character_owned_link_skill_preset_2"
    )
    owned_link_skill_preset_3: LinkSkill | None = Field(
        alias="character_owned_link_skill_preset_3"
    )
