from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class CharacterSkillInfo(BaseModel):
    """스킬 정보

    Attributes:
        name (str): 스킬 명
        description (str): 스킬 설명
        level (int): 스킬 레벨
        effect (str | None): 스킬 레벨 별 효과 설명
        icon (str): 스킬 아이콘
    """

    name: str = Field(alias='skill_name')
    description: str = Field(alias='skill_description')
    level: int = Field(alias='skill_level')
    effect: str | None = Field(alias='skill_effect')
    icon: str = Field(alias='skill_icon')


class CharacterSkill(BaseModel):
    """캐릭터 스킬 정보

    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_class (str): 캐릭터 직업
        character_skill_grade (int): 스킬 전직 차수
        skills (list[CharacterSkillInfo]): 스킬 정보
    """

    date: datetime
    character_class: str
    character_skill_grade: int
    skills: list[CharacterSkillInfo] = Field(alias='character_skill')

    @field_validator("character_skill_grade", mode="before")
    @classmethod
    def skill_grade_must_be_between_0_and_6(cls, v: str | int) -> int:
        """스킬 전직 차수 유효성 검사
        스킬 전직 차수가 0과 6 사이인지 확인

        Raises:
            ValueError: 스킬 전직 차수가 0 미만이거나 6 초과인 경우, 정수로 변환할 수 없는 경우
        """
        try:
            v = int(v)
        except ValueError as e:
            raise ValueError("skill_grade must be an integer.") from e

        if v < 0 or v > 6:
            raise ValueError("skill_grade must be in 0 ~ 6.")

        return v
