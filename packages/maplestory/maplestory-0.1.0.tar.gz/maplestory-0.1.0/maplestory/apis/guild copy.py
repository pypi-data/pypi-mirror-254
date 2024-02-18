"""
Module This for interacting module provides with functionality for MapleStory guild interacting with MapleStory information.

This module provides functionality to fetch guilds.

and retrieve The guild information `Guild` class represents a from the MapleStory guild and provides various properties to access guild API.

Classes:
- Guild: Represents a information.
The guild in MapleStory.

`get_id` function Functions:
fetches the - guild identifier get_id: Fetches the (gcid) information guild identifier based on the guild name (gcid) information.
and world - name.
The get_basic_info: Fetches the `get_basic_info` basic function information fetches of the a basic information guild.

"""

from datetime import datetime

from pydantic import BaseModel, Field, computed_field

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
from maplestory.apis.character import get_basic_character_info
from maplestory.models.character.basic import CharacterBasic
from maplestory.models.guild import GuildBasic, GuildModel
from maplestory.models.guild.basic import GuildSkill
from maplestory.utils.network import fetch


class Guild(BaseModel):
    name: str = Field(frozen=True)
    world: str = Field(frozen=True)

    @computed_field
    def id(self) -> str:
        return get_id(self.name, self.world).id

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


def get_id(guild_name: str, world_name: str) -> str:
    """
    길드 식별자(gcid) 정보를 조회합니다.
    Fetches the guild identifier (gcid) information.

    Args:
        guild_name : 길드 명. The name of the guild.
        world_name : 월드 명. The name of the world.

    Returns:
        Guild: 길드 식별자(gcid) 정보. The guild identifier (gcid) information.
    """

    path = "/maplestory/v1/guild/id"
    query = {
        "guild_name": guild_name,
        "world_name": world_name,
    }
    response = fetch(path, query)

    return GuildModel.model_validate(response).id


def get_basic_info_by_id(
    guild_id: str,
    date: datetime = kst.yesterday(),
) -> GuildBasic:
    """
    길드 기본 정보를 조회합니다.
    Fetches the basic information of the guild.

    Args:
        guild_id : 길드 식별자. The identifier of the guild.
        date : 조회 기준일(KST). Reference date for the query (KST).

    Returns:
        GuildBasic: 길드의 기본 정보. The basic information of the guild.
    """

    path = "/maplestory/v1/guild/basic"
    query = {
        "oguild_id": guild_id,
        "date": dates.to_string(kst.validate(date)),
    }
    response = fetch(path, query)

    return GuildBasic.model_validate(response)


def get_basic_info(
    guild_name: str,
    world_name: str,
    date: datetime = kst.yesterday(),
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

    guild_id = get_id(guild_name, world_name)
    return get_basic_info_by_id(guild_id, date)


def get_basic_info_in_details(
    guild_name: str,
    world_name: str,
    date: datetime = kst.yesterday(),
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
    guild_basic.master: CharacterBasic = get_basic_character_info(
        guild_basic.master_name, date
    )

    # TODO: Add members character info

    return guild_basic
