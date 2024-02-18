from datetime import datetime
from enum import Enum

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
from maplestory.enum import GuildRankType, QueryableDate, WorldType
from maplestory.models.ranking import (
    AchievementRanking,
    DojangRanking,
    GuildRanking,
    OverallRanking,
    TheSeedRanking,
    UnionRanking,
)
from maplestory.models.types import JobClass, WorldName
from maplestory.utils.network import fetch

# def validate_ranking_date(date: kst.KSTdatetime | None) -> None:
#     if date is not None and date < RANK_MINIMUM_DATETIME:
#         raise ValueError("date must be after 2023-12-22 KST.")


def get_overall_ranking(
    world: WorldName | None = None,
    world_type: int | WorldType | None = None,
    job_class: JobClass | None = None,
    character_id: str | None = None,
    page_number: int = 1,
    base_date: kst.KSTdatetime = kst.yesterday(),
) -> OverallRanking:
    """
    종합 랭킹 정보를 조회합니다.
    Fetches the overall ranking information.

    Args:
        base_date : 조회 기준일(KST) Example : 2023-12-22
                    Query base date (KST)
        world (str, optional): 월드 명
                               World name
                               Available values : 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
        world_type (int, optional): 월드 타입 (0:일반, 1:리부트) (기본 값은 0이며, world_name 입력 시 미 반영)
                                    World type (0: normal, 1: reboot) (default is 0 and not reflected when world_name is entered)
        job_class (str, optional): 직업 및 전직
                                   Job and class
                                    Available values : 초보자-전체 전직, 전사-전체 전직, 전사-검사, 전사-파이터, 전사-페이지, 전사-스피어맨, 전사-크루세이더, 전사-나이트, 전사-버서커, 전사-히어로, 전사-팔라딘, 전사-다크나이트, 마법사-전체 전직, 마법사-매지션, 마법사-위자드(불,독), 마법사-위자드(썬,콜), 마법사-클레릭, 마법사-메이지(불,독), 마법사-메이지(썬,콜), 마법사-프리스트, 마법사-아크메이지(불,독), 마법사-아크메이지(썬,콜), 마법사-비숍, 궁수-전체 전직, 궁수-아처, 궁수-헌터, 궁수-사수, 궁수-레인저, 궁수-저격수, 궁수-보우마스터, 궁수-신궁, 궁수-아처(패스파인더), 궁수-에인션트아처, 궁수-체이서, 궁수-패스파인더, 도적-전체 전직, 도적-로그, 도적-어쌔신, 도적-시프, 도적-허밋, 도적-시프마스터, 도적-나이트로드, 도적-섀도어, 도적-세미듀어러, 도적-듀어러, 도적-듀얼마스터, 도적-슬래셔, 도적-듀얼블레이더, 해적-전체 전직, 해적-해적, 해적-인파이터, 해적-건슬링거, 해적-캐논슈터, 해적-버커니어, 해적-발키리, 해적-캐논블래스터, 해적-바이퍼, 해적-캡틴, 해적-캐논마스터, 기사단-전체 전직, 기사단-노블레스, 기사단-소울마스터, 기사단-플레임위자드, 기사단-윈드브레이커, 기사단-나이트워커, 기사단-스트라이커, 기사단-미하일, 아란-전체 전직, 에반-전체 전직, 레지스탕스-전체 전직, 레지스탕스-시티즌, 레지스탕스-배틀메이지, 레지스탕스-와일드헌터, 레지스탕스-메카닉, 레지스탕스-데몬슬레이어, 레지스탕스-데몬어벤져, 레지스탕스-제논, 레지스탕스-블래스터, 메르세데스-전체 전직, 팬텀-전체 전직, 루미너스-전체 전직, 카이저-전체 전직, 엔젤릭버스터-전체 전직, 초월자-전체 전직, 초월자-제로, 은월-전체 전직, 프렌즈 월드-전체 전직, 프렌즈 월드-키네시스, 카데나-전체 전직, 일리움-전체 전직, 아크-전체 전직, 호영-전체 전직, 아델-전체 전직, 카인-전체 전직, 라라-전체 전직, 칼리-전체 전직
        character_id (str, optional): 캐릭터 식별자
                                        Character identifier
        page_number : 페이지 번호
                      Page number

    Note:
        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
          Data can be queried from December 22, 2023.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
          Ranking information for the day can be queried from 8:30 AM.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다.
          Please note that the ocid may change due to game content changes.
          ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
          Please be careful when updating services based on ocid.
    """
    dates.is_valid(date, QueryableDate.랭킹)

    if isinstance(world_type, int):
        try:
            world_type = WorldType(world_type)
        except ValueError as err:
            raise ValueError("world_type must be 0 or 1.") from err

    if isinstance(world_type, WorldType):
        world_type = world_type.value

    path = "/maplestory/v1/ranking/overall"
    query = {
        "date": dates.to_string(base_date),
        "world_name": world,
        "world_type": world_type,
        "class": job_class,
        "ocid": character_id,
        "page": page_number,
    }
    response = fetch(path, query)

    return OverallRanking.model_validate(response)


def get_union_ranking(
    world: WorldName | None = None,
    character_id: str | None = None,
    page_number: int = 1,
    date: kst.KSTdatetime = kst.yesterday(),
) -> UnionRanking:
    """유니온 랭킹 정보를 조회합니다.
    Fetches the union ranking information.

    Args:
        date (datetime): 조회 기준일(KST)
               The reference date for the query (KST).
        world (str, optional): 월드 명
                               The name of the world.
            가능한 값은 (스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3)
            Possible values are: 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
        character_id (str, optional): 캐릭터 식별자
                                      The identifier of the character.
        page_number (int): 페이지 번호
                           The page number.

    Returns:
        UnionRanking: 유니온 랭킹 정보
                      The union ranking information.

    Note:
        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
          Data can be queried from December 22, 2023.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
          Ranking information for the day can be queried from 8:30 AM.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다.
          Please note that the ocid may change due to game content changes.
          ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
          Please be careful when updating services based on ocid.
    """

    dates.is_valid(date, QueryableDate.랭킹)

    path = "/maplestory/v1/ranking/union"
    query = {
        "date": dates.to_string(dates),
        "world_name": world,
        "ocid": character_id,
        "page": page_number,
    }
    response = fetch(path, query)

    return UnionRanking.model_validate(response)


def get_guild_ranking(
    ranking_type: int | GuildRankType = GuildRankType.주간명성치,
    world: WorldName | None = None,
    guild: str | None = None,
    page_number: int = 1,
    date: kst.KSTdatetime = kst.yesterday(),
) -> GuildRanking:
    """길드 랭킹 정보를 조회합니다.
    Fetches the guild ranking information.

    Args:
        date : 조회 기준일(KST)
               The reference date for the query (KST).
        ranking_type (int | GuildRankType): 랭킹 타입
                                            The type of ranking
            (0:주간 명성치, 1:플래그 레이스, 2:지하 수로)
            (0: Weekly Fame, 1: Flag Race, 2: Underground Waterway).
        world (str, optional): 월드 명
                               The name of the world.
            Possible values are: 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
        guild (str, optional): 길드 명
                               The name of the guild.
        page_number : 페이지 번호
                      The page number.

    Returns:
        GuildRanking: 길드 랭킹 정보
                      The guild ranking information.

    Note:
        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
          Data can be queried from December 22, 2023.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
          Ranking information for the day can be queried from 8:30 AM.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다.
          Please note that the ocid may change due to game content changes.
          ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
          Please be careful when updating services based on ocid.
    """

    dates.is_valid(date, QueryableDate.랭킹)

    if isinstance(ranking_type, GuildRankType):
        ranking_type = ranking_type.value

    if ranking_type not in [0, 1, 2]:
        raise ValueError("ranking_type must be 0, 1, or 2.")

    # if isinstance(ranking_type, int):
    #     try:
    #         ranking_type = GuildRankType(ranking_type)
    #     except ValueError as err:
    #         raise ValueError("ranking_type must be 0 or 1.") from err

    path = "/maplestory/v1/ranking/guild"
    query = {
        "date": dates.to_string(date),
        "ranking_type": ranking_type,
        "world_name": world,
        "guild_name": guild,
        "page": page_number,
    }
    response = fetch(path, query)

    return GuildRanking.model_validate(response)


def get_dojang_ranking(
    world: str | None = None,
    job_class: str | None = None,
    character_id: str | None = None,
    page_number: int = 1,
    difficulty_level: int = 1,
    date: kst.AwareDatetime = kst.yesterday(),
) -> DojangRanking:
    """무릉도장 랭킹 정보를 조회합니다.
    Fetches the Dojang ranking information.

    Args:
        world (Optional[str]): 월드 명
            The name of the world.
            - 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
        job_class (Optional[str]): 직업 및 전직
                    The name of the job class.
                    - 초보자-전체 전직, 전사-전체 전직, 전사-검사, 전사-파이터, 전사-페이지, 전사-스피어맨, 전사-크루세이더, 전사-나이트, 전사-버서커, 전사-히어로, 전사-팔라딘, 전사-다크나이트, 마법사-전체 전직, 마법사-매지션, 마법사-위자드(불,독), 마법사-위자드(썬,콜), 마법사-클레릭, 마법사-메이지(불,독), 마법사-메이지(썬,콜), 마법사-프리스트, 마법사-아크메이지(불,독), 마법사-아크메이지(썬,콜), 마법사-비숍, 궁수-전체 전직, 궁수-아처, 궁수-헌터, 궁수-사수, 궁수-레인저, 궁수-저격수, 궁수-보우마스터, 궁수-신궁, 궁수-아처(패스파인더), 궁수-에인션트아처, 궁수-체이서, 궁수-패스파인더, 도적-전체 전직, 도적-로그, 도적-어쌔신, 도적-시프, 도적-허밋, 도적-시프마스터, 도적-나이트로드, 도적-섀도어, 도적-세미듀어러, 도적-듀어러, 도적-듀얼마스터, 도적-슬래셔, 도적-듀얼블레이더, 해적-전체 전직, 해적-해적, 해적-인파이터, 해적-건슬링거, 해적-캐논슈터, 해적-버커니어, 해적-발키리, 해적-캐논블래스터, 해적-바이퍼, 해적-캡틴, 해적-캐논마스터, 기사단-전체 전직, 기사단-노블레스, 기사단-소울마스터, 기사단-플레임위자드, 기사단-윈드브레이커, 기사단-나이트워커, 기사단-스트라이커, 기사단-미하일, 아란-전체 전직, 에반-전체 전직, 레지스탕스-전체 전직, 레지스탕스-시티즌, 레지스탕스-배틀메이지, 레지스탕스-와일드헌터, 레지스탕스-메카닉, 레지스탕스-데몬슬레이어, 레지스탕스-데몬어벤져, 레지스탕스-제논, 레지스탕스-블래스터, 메르세데스-전체 전직, 팬텀-전체 전직, 루미너스-전체 전직, 카이저-전체 전직, 엔젤릭버스터-전체 전직, 초월자-전체 전직, 초월자-제로, 은월-전체 전직, 프렌즈 월드-전체 전직, 프렌즈 월드-키네시스, 카데나-전체 전직, 일리움-전체 전직, 아크-전체 전직, 호영-전체 전직, 아델-전체 전직, 카인-전체 전직, 라라-전체 전직, 칼리-전체 전직
        character_id (Optional[str]): 캐릭터 식별자
                    The identifier of the character.
        page_number : 페이지 번호
                    The page number.
        difficulty_level : 구간 (0:일반, 1:통달)
            The difficulty level (0: Normal, 1: Mastery).
        date : 조회 기준일(KST)
            The reference date for the query (KST).

    Returns:
        DojangRanking: The Dojang ranking information.

    Note:
        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
          Data can be queried from December 22, 2023.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
          Ranking information for the day can be queried from 8:30 AM.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다.
          Please note that the ocid may change due to game content changes.
          ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
          Please be careful when updating services based on ocid.
    """
    dates.is_valid(date, QueryableDate.랭킹)

    path = "/maplestory/v1/ranking/dojang"
    query = {
        "date": dates.to_string(date),
        "world_name": world,
        "class": job_class,
        "ocid": character_id,
        "page": page_number,
        "difficulty": difficulty_level,
    }
    response = fetch(path, query)

    return DojangRanking.model_validate(response)


def get_theseed_ranking(
    world: WorldName | None = None,
    character_id: str | None = None,
    page_number: int = 1,
    date: kst.AwareDatetime = kst.yesterday(),
) -> TheSeedRanking:
    """
    Fetches the TheSeed ranking information.
    더 시드 랭킹 정보를 조회합니다.

    Args:
        world (str): The name of the world.
                     월드명.
        character_id (str): The identifier of the character.
                            캐릭터 식별자(ocid).
        page_number (int): The page number.
                           페이지 번호.
        date (datetime): The reference date for the query (KST).
                                   조회 기준일(KST)

    Returns:
        TheSeedRanking: The TheSeed ranking information.
                        더 시드 랭킹 정보.

    Note:
        - Data can be queried from December 22, 2023.
          2023년 12월 22일 데이터부터 조회할 수 있습니다.
        - Ranking information can be queried from 8:30 AM.
          오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
        - Be careful when updating the service based on ocid, as the ocid may change due to game content changes.
          게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
    """

    dates.is_valid(date, QueryableDate.랭킹)

    path = "/maplestory/v1/ranking/theseed"
    query = {
        "date": dates.to_string(date),
        "world_name": world,
        "ocid": character_id,
        "page": page_number,
    }
    response = fetch(path, query)

    return TheSeedRanking.model_validate(response)


def get_achievement_ranking(
    character_id: str | None = None,
    page_number: int = 1,
    date: kst.AwareDatetime = kst.yesterday(),
) -> AchievementRanking:
    """
    Fetches the achievement ranking information.
    조회 기준일(KST)과 캐릭터 식별자를 사용하여 업적 랭킹 정보를 조회합니다.

    Args:
        character_id (str): 캐릭터 식별자(ocid).
                            The identifier of the character.

        page_number (int): 페이지 번호.
                           The page number.

        date (datetime): 조회 기준일(KST)
                                   The reference date for the query (KST).

    Returns:
        AchievementRanking: 업적 랭킹 정보.
                            The achievement ranking information.

    Note:
        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
          Data can be queried from December 22, 2023.

        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
          Ranking information can be queried from 8:30 AM.

        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
          Be careful when updating the service based on ocid, as the ocid may change due to game content changes.

    """

    dates.is_valid(date, QueryableDate.랭킹)

    path = "/maplestory/v1/ranking/achievement"
    query = {
        "date": dates.to_string(date),
        "ocid": character_id,
        "page": page_number,
    }
    response = fetch(path, query)

    return AchievementRanking.model_validate(response)
