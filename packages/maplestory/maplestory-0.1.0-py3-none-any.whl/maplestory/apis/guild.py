"""길드 정보 조회 API를 제공하는 모듈입니다.

Note:
    - 2023년 12월 21일부터 데이터를 조회할 수 있습니다.
    - 캐릭터 정보 조회 API는 일자별 데이터로 매일 오전 1시부터 전일 데이터 조회가 가능합니다.
      (예를 들어, 12월 22일 데이터를 조회하면 22일 00시부터 23일의 00시 사이의 데이터가 조회됩니다.)
    - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
"""

from datetime import datetime

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
from maplestory.models.guild import GuildBasic, GuildModel
from maplestory.models.types import WorldName
from maplestory.utils.network import fetch


def get_guild_id(guild_name: str, world_name: WorldName) -> str:
    """길드 식별자(gcid) 정보를 조회합니다.

    Args:
        guild_name (str): 길드명.
        world_name (str): 월드명.
            Available values: 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움,
                이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3

    Returns:
        str: 길드 식별자(gcid) 정보.
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
    """길드 기본 정보를 조회합니다.

    Args:
        guild_id (str): 길드 식별자.
        date (datetime): 조회 기준일(KST).

    Returns:
        GuildBasic: 길드의 기본 정보.
    """

    path = "/maplestory/v1/guild/basic"
    query = {
        "oguild_id": guild_id,
        "date": dates.to_string(date),
    }
    response = fetch(path, query)

    return GuildBasic.model_validate(response)
