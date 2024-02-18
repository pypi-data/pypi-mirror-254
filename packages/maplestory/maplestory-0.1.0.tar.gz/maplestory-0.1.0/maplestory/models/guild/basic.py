import base64
from datetime import datetime
from io import BytesIO

from PIL import Image
from pydantic import BaseModel, Field, HttpUrl

from ..types import GuildLevel, WorldName


class GuildSkill(BaseModel):
    """길드 스킬 정보. Guild skill information.

    Attributes:
        name (str): 스킬명. The name of the guild skill.
        description (str): 스킬 설명. The description of the guild skill.
        level (int): 스킬 레벨. The level of the guild skill.
        effect (str): 스킬 레벨별 효과. The effect of the guild skill.
        icon (HttpUrl): 스킬 아이콘. The icon of the guild skill.
    """

    name: str = Field(alias="skill_name")
    description: str = Field(alias="skill_description")
    level: int = Field(alias="skill_level")
    effect: str = Field(alias="skill_effect")
    icon: HttpUrl = Field(alias="skill_icon")

    @property
    def desc(self) -> str:
        return self.description

    @property
    def 이름(self) -> str:
        return self.name

    @property
    def 설명(self) -> str:
        return self.description

    @property
    def 레벨(self) -> int:
        return self.level

    @property
    def 효과(self) -> str:
        return self.effect

    @property
    def 아이콘(self) -> HttpUrl:
        return self.icon


class GuildBasic(BaseModel):
    """길드 기본 정보. Basic information of the guild.

    Attributes:
        date: 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        world: 월드 명
        name: 길드 명
        level: 길드 레벨
        fame: 길드 명성치
        point: 길드 포인트(GP)
        master_name: 길드 마스터 캐릭터 명
        member_count: 길드원 수
        members: 길드원 목록
        skill: 길드 스킬 목록
        noblesse_skill: 노블레스 스킬 목록
        mark: 조합형 길드 마크
        mark_custom: 커스텀 길드 마크 (base64 인코딩 형식)
    """

    date: datetime
    world: WorldName = Field(alias="world_name")
    name: str = Field(alias="guild_name")
    level: GuildLevel = Field(alias="guild_level")
    fame: int = Field(alias="guild_fame")
    point: int = Field(alias="guild_point")
    master_name: str = Field(alias="guild_master_name")
    member_count: int = Field(alias="guild_member_count")
    members: list[str] = Field(alias="guild_member")
    skills: list[GuildSkill] = Field(alias="guild_skill")
    noblesse_skills: list[GuildSkill] = Field(alias="guild_noblesse_skill")
    mark: str | None = Field(alias="guild_mark")
    custom_mark: str | None = Field(alias="guild_mark_custom")

    @property
    def custom_mark_img(self) -> Image.Image | None:
        if self.custom_mark is None:
            return None

        im_bytes = base64.b64decode(self.custom_mark)
        im_file = BytesIO(im_bytes)
        return Image.open(im_file)

    @property
    def 노블포인트(self) -> int:
        return sum(skill.level for skill in self.noblesse_skills)
