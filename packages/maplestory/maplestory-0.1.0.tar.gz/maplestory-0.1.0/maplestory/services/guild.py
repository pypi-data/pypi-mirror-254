from datetime import datetime

from pydantic import BaseModel, Field, computed_field

from maplestory.apis.guild import get_basic_info_by_id, get_guild_id
from maplestory.models.guild import GuildBasic
from maplestory.models.guild.basic import GuildSkill
from maplestory.services.character import get_basic_character_info
from maplestory.utils.kst import yesterday


class Guild(BaseModel):
    name: str = Field(frozen=True)
    world: str = Field(frozen=True)

    @computed_field
    def id(self) -> str:
        return get_guild_id(self.name, self.world).id

    def oguild_id(self) -> str:
        return self.id

    @computed_field
    def basic(self) -> GuildBasic:
        return get_basic_info(self.id)

    @property
    def level(self) -> int:
        return self.basic.level

    @property
    def point(self) -> int:
        return self.basic.point

    @property
    def fame(self) -> int:
        return self.basic.fame

    @property
    def member_count(self) -> int:
        return self.basic.member_count

    @property
    def members(self) -> list[str]:
        # TODO: Add character model
        return self.basic.members

    @property
    def master_name(self) -> str:
        return self.basic.master_name

    @property
    def master(self) -> str:
        # TODO: Add character model
        return self.basic.master_name

    @property
    def master_character(self) -> str:
        # TODO: Add character model
        return self.basic.master_character

    @property
    def skills(self) -> list[GuildSkill]:
        return self.basic.skills

    @property
    def noblesse_skills(self) -> list[GuildSkill]:
        return self.basic.noblesse_skills

    @property
    def mark(self) -> str:
        return self.basic.mark

    @property
    def custom_mark(self) -> str:
        return self.basic.custom_mark


def get_basic_info(
    guild_name: str,
    world_name: str,
    date: datetime = yesterday(),
) -> GuildBasic:
    """
    길드 기본 정보를 조회합니다.
    Fetches the basic information of the guild.

    Args:
        guild_name : 길드 명. The name of the guild.
        world_name : 월드 명. The name of the world.
        date : 조회 기준일(KST). Reference date for the query (KST).

    Returns:
        GuildBasic: 길드의 기본 정보. The basic information of the guild.
    """

    guild_id = get_guild_id(guild_name, world_name)
    return get_basic_info_by_id(guild_id, date)


def get_basic_info_in_details(
    guild_name: str,
    world_name: str,
    date: datetime = yesterday(),
) -> GuildBasic:
    """
    길드 기본 정보를 조회합니다.
    Fetches the basic information of the guild.

    Args:
        guild_name : 길드명. The name of the guild.
        world_name : 월드명. The name of the world.
        date : 조회 기준일(KST). Reference date for the query (KST).

    Returns:
        GuildBasic: 길드의 기본 정보. The basic information of the guild.
    """

    guild_basic: GuildBasic = get_basic_info(guild_name, world_name, date)

    # Add master character info
    guild_basic.master = get_basic_character_info(guild_basic.master_name, date)

    # TODO: Add members character info

    return guild_basic
