from datetime import datetime
from typing import Any, Optional
from zoneinfo import ZoneInfo

import httpx
from httpx import Request, Response
from pydantic import BaseModel, Field

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
from maplestory.error import ErrorMessage
from maplestory.models.character import (
    Ability,
    AndroidEquipment,
    BeautyEquipment,
    CashitemEquipment,
    CharacterBasic,
    CharacterDojang,
    CharacterEquipment,
    CharacterId,
    CharacterLinkSkill,
    CharacterPet,
    CharacterSkill,
    CharacterStat,
    HexaMatrix,
    HexaMatrixStat,
    HyperStat,
    Popularity,
    Propensity,
    SetEffect,
    SymbolEquipment,
    VMatrix,
)
from maplestory.models.guild import GuildBasic, GuildModel
from maplestory.models.history import CubeHistory, StarforceHistory
from maplestory.models.ranking import (
    AchievementRanking,
    DojangRanking,
    GuildRanking,
    OverallRanking,
    TheSeedRanking,
    UnionRanking,
)
from maplestory.models.union import Union, UnionRaider
from maplestory.utils.network import fetch


class MapleStoryApi(BaseModel):
    api_key: str
    BASE_URL: str = "https://open.api.nexon.com/"
    timeout: int

    character_name: Optional[str] = Field(None, repr=False)
    character_ocid: Optional[str] = Field(None, repr=False)

    guild_name: Optional[str] = Field(None, repr=False)
    world_name: Optional[str] = Field(None, repr=False)
    oguild_id: Optional[str] = Field(None, repr=False)

    def __init__(self, api_key, timeout: int = 5000):
        super().__init__(
            api_key=api_key,
            timeout=timeout,
        )

    def get_character_id(self, character_name: str) -> CharacterId:
        """
        캐릭터의 식별자(ocid)를 조회합니다.
        Fetches the identifier (ocid) of a character.

        Args:
            character_name : 캐릭터의 이름.
                                  The name of the character.

        Returns:
            Character: 주어진 이름의 캐릭터.
                       The character with the given name.

        Note:
            - 2023년 12월 21일부터 데이터를 조회할 수 있습니다.
            Data can be queried from December 21, 2023.
            - 캐릭터 정보 조회 API는 일자별 데이터로 매일 오전 1시부터 전일 데이터 조회가 가능합니다.
            The character information query API provides daily data, and data for the previous day can be queried from 1 AM every day.
            - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
            The ocid may change due to game content changes. Please be careful when updating services based on ocid.
        """
        path = "/maplestory/v1/id"
        query = {
            "character_name": character_name,
        }
        response = fetch(path, query)

        return CharacterId.model_validate(response)

    def get_basic_character_info(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterBasic:
        """
        캐릭터의 기본 정보를 조회합니다.
        Fetches the basic information of a character.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                    Reference date for the query (KST).

        Returns:
            CharacterBasic: 캐릭터의 기본 정보.
                            The basic information of the character.

        Note:
            - 2023년 12월 21일부터 데이터를 조회할 수 있습니다.
            Data can be queried from December 21, 2023.
            - 캐릭터 정보 조회 API는 일자별 데이터로 매일 오전 1시부터 전일 데이터 조회가 가능합니다. (예를 들어, 12월 22일 데이터를 조회하면 22일 00시부터 23일의 00시 사이의 데이터가 조회됩니다.)
            The character information query API provides daily data, and data for the previous day can be queried from 1 AM every day. (For example, if you query data for December 22, you will get data from 00:00 on the 22nd to 00:00 on the 23rd.)
            - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
            The ocid may change due to game content changes. Please be careful when updating services based on ocid.
        """
        path = "/maplestory/v1/character/basic"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CharacterBasic.model_validate(response)

    def get_character_popularity(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> Popularity:
        """
        캐릭터의 인기도 정보를 조회합니다.
        Fetches the popularity information of a character.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterPopularity: 캐릭터의 인기도 정보.
                                 The popularity information of the character.
        """
        path = "/maplestory/v1/character/popularity"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return Popularity(
            date=api_response.get("date"),
            popularity=api_response.get("popularity"),
        )

    def get_character_stat(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterStat:
        """
        캐릭터의 종합능력치 정보를 조회합니다.
        Fetches the comprehensive ability information of a character.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterStat: 캐릭터의 종합능력치 정보.
                           The comprehensive ability information of the character.
        """
        path = "/maplestory/v1/character/stat"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CharacterStat.model_validate(response)

    def get_character_hyper_stat(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> HyperStat:
        """
        캐릭터의 하이퍼스탯 정보를 조회합니다.
        Fetches the hyper stat information of a character.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterHyperStat: 캐릭터의 하이퍼스탯 정보.
                                The hyper stat information of the character.
        """
        path = "/maplestory/v1/character/hyper-stat"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return HyperStat.model_validate(response)

    def get_character_propensity(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> Propensity:
        """
        캐릭터의 성향 정보를 조회합니다.
        Fetches the propensity information of a character.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterPropensity: 캐릭터의 성향 정보.
                                 The propensity information of the character.
        """
        path = "/maplestory/v1/character/propensity"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return Propensity.model_validate(response)

    def get_character_ability(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> Ability:
        """
        캐릭터의 어빌리티 정보를 조회합니다.
        Fetches the ability information of a character.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterAbility: 캐릭터의 어빌리티 정보.
                              The ability information of the character.
        """
        path = "/maplestory/v1/character/ability"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return Ability.model_validate(response)

    def get_character_equipment(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterEquipment:
        """
        장착한 장비 중 캐시 장비를 제외한 나머지 장비 정보를 조회합니다.
        Fetches the information of equipped items excluding cash items.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterItemEquipment: 캐릭터의 장비 정보.
                                    The equipment information of the character.
        """
        path = "/maplestory/v1/character/item-equipment"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CharacterEquipment.model_validate(response)

    def get_character_cashitem_equipment(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CashitemEquipment:
        """
        장착한 캐시 장비 정보를 조회합니다.
        Fetches the information of equipped cash items.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterCashitemEquipment: 캐릭터의 캐시 장비 정보.
                                        The cash item equipment information of the character.
        """
        path = "/maplestory/v1/character/cashitem-equipment"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CashitemEquipment.model_validate(response)

    def get_character_symbol_equipment(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> SymbolEquipment:
        """
        장착한 심볼 정보를 조회합니다.
        Fetches the equipped symbol information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterSymbolEquipment: 캐릭터의 심볼 장비 정보.
                                      The symbol equipment information of the character.
        """
        path = "/maplestory/v1/character/symbol-equipment"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return SymbolEquipment.model_validate(response)

    def get_character_set_effect(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> SetEffect:
        """
        적용받고 있는 세트 효과 정보를 조회합니다.
        Fetches the applied set effect information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterSetEffect: 캐릭터의 세트 효과 정보.
                                The set effect information of the character.
        """
        path = "/maplestory/v1/character/set-effect"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return SetEffect.model_validate(response)

    def get_character_beauty_equipment(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> BeautyEquipment:
        """
        캐릭터 헤어, 성형, 피부 정보를 조회합니다.
        Fetches the character's hair, plastic surgery, and skin information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterBeautyEquipment: 캐릭터의 미용 장비 정보.
                                      The beauty equipment information of the character.
        """
        path = "/maplestory/v1/character/beauty-equipment"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return BeautyEquipment.model_validate(response)

    def get_character_android_equipment(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> AndroidEquipment:
        """
        장착한 안드로이드 정보를 조회합니다.
        Fetches the equipped android information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterAndroidEquipment: 캐릭터의 안드로이드 장비 정보.
                                       The android equipment information of the character.
        """
        path = "/maplestory/v1/character/android-equipment"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return AndroidEquipment.model_validate(response)

    def get_character_pet_equipment(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterPet:
        """
        장착한 펫 및 펫 스킬, 장비 정보를 조회합니다.
        Fetches the equipped pet and pet skill, equipment information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterPetEquipment: 캐릭터의 펫 장비 정보.
                                   The pet equipment information of the character.
        """
        path = "/maplestory/v1/character/pet-equipment"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CharacterPet.model_validate(response)

    def get_character_skill(
        self,
        character_ocid: str,
        skill_grade: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterSkill:
        """
        캐릭터 스킬과 하이퍼 스킬 정보를 조회합니다.
        Fetches the character's skill and hyper skill information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            skill_grade : 조회하고자 하는 전직 차수.
                               The job advancement grade to query.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterSkill: 캐릭터의 스킬 정보.
                            The skill information of the character.
        """
        path = "/maplestory/v1/character/skill"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
            "character_skill_grade": skill_grade,
        }
        response = fetch(path, query)

        return CharacterSkill.model_validate(response)

    def get_character_link_skill(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterLinkSkill:
        """
        장착 링크 스킬 정보를 조회합니다.
        Fetches the equipped link skill information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterLinkSkill: 캐릭터의 링크 스킬 정보.
                                The link skill information of the character.
        """
        path = "/maplestory/v1/character/link-skill"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CharacterLinkSkill.model_validate(response)

    def get_character_vmatrix(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> VMatrix:
        """
        V매트릭스 슬롯 정보와 장착한 V코어 정보를 조회합니다.
        Fetches the VMatrix slot information and the equipped VCore information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterVMatrix: 캐릭터의 V매트릭스 정보.
                              The VMatrix information of the character.
        """
        path = "/maplestory/v1/character/vmatrix"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return VMatrix.model_validate(response)

    def get_character_hexamatrix(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> HexaMatrix:
        """
        HEXA 매트릭스에 장착한 HEXA 코어 정보를 조회합니다.
        Fetches the HEXA core information equipped in the HEXA matrix.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterHexaMatrix: 캐릭터의 HEXA 매트릭스 정보.
                                 The HEXA matrix information of the character.
        """
        path = "/maplestory/v1/character/hexamatrix"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return HexaMatrix.model_validate(response)

    def get_character_hexamatrix_stat(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> HexaMatrixStat:
        """
        HEXA 매트릭스에 설정한 HEXA 스탯 정보를 조회합니다.
        Fetches the HEXA stat information set in the HEXA matrix.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterHexaMatrixStat: 캐릭터의 HEXA 매트릭스 스탯 정보.
                                     The HEXA matrix stat information of the character.
        """
        path = "/maplestory/v1/character/hexamatrix-stat"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return HexaMatrixStat.model_validate(response)

    def get_character_dojang_record(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> CharacterDojang:
        """
        캐릭터 무릉도장 최고 기록 정보를 조회합니다.
        Fetches the highest record information of the character's Mu Lung Dojang.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            CharacterDojang: 캐릭터의 무릉도장 최고 기록 정보.
                             The highest record information of the character's Mu Lung Dojang.
        """
        path = "/maplestory/v1/character/dojang"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return CharacterDojang.model_validate(response)

    def get_union_info(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> Union:
        """
        유니온 레벨 및 유니온 등급 정보를 조회합니다.
        Fetches the Union level and Union rank information.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            Union: 유니온의 레벨 및 등급 정보.
                   The level and rank information of the Union.
        """
        path = "/maplestory/v1/user/union"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return Union.model_validate(response)

    def get_union_raider_info(
        self,
        character_ocid: str,
        date: datetime = kst.yesterday(),
    ) -> UnionRaider:
        """
        유니온에 배치된 공격대원 효과 및 공격대 점령 효과 등 상세 정보를 조회합니다.
        Fetches the detailed information of the effect of the attack members placed in the Union and the effect of the attack occupation.

        Args:
            character_ocid : 캐릭터의 식별자(ocid).
                                  The identifier (ocid) of the character.
            date : 조회 기준일 (KST).
                                       Reference date for the query (KST).

        Returns:
            UnionRaider: 유니온에 배치된 공격대원 효과 및 공격대 점령 효과 등의 상세 정보.
                         The detailed information of the effect of the attack members placed in the Union and the effect of the attack occupation.
        """
        path = "/maplestory/v1/user/union-raider"
        query = {
            "ocid": character_ocid,
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return UnionRaider.model_validate(response)

    def get_guild_id(self, guild_name: str, world_name: str) -> GuildModel:
        """
        The get_guild_id function fetches the guild identifier (gcid) information.

        :param self: Represent the instance of the class
        :param guild_name: str: Specify the name of the guild
        :param world_name: str: Specify the world name
        :return: A guildmodel object
        :doc-author: Trelent
        """
        """
        길드 식별자(gcid) 정보를 조회합니다.
        Fetches the guild identifier (gcid) information.

        Args:
            guild_name : 길드 명. The name of the guild.
            world_name : 월드 명. The name of the world.

        Returns:
            GuildModel: 길드 식별자(gcid) 정보. The guild identifier (gcid) information.
        """
        path = "/maplestory/v1/guild/id"
        query = {
            "guild_name": guild_name,
            "world_name": world_name,
        }
        response = fetch(path, query)

        return GuildModel.model_validate(response)

    def get_guild_basic_info(
        self,
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
            "date": dates.to_string(date),
        }
        response = fetch(path, query)

        return GuildBasic.model_validate(response)

    def get_cube_usage_history(
        self,
        result_count: int,
        date: datetime | None = None,
        cursor: str | None = None,
    ) -> CubeHistory:
        """
        큐브 사용 결과를 조회합니다.
        Fetches the usage result of the cube.

        Args:
            result_count : 한번에 가져오려는 결과의 갯수. The number of results to fetch at once.
            date : 조회 기준일(KST). Reference date for the query (KST).
            cursor : 페이징 처리를 위한 cursor. Cursor for paging.

        Returns:
            CubeHistory: 큐브 사용 결과. The usage result of the cube.
        """
        path = "/maplestory/v1/history/cube"
        query = {
            "count": result_count,
            "date": dates.to_string(date) if date else date,
            "cursor": cursor,
        }
        response = fetch(path, query)

        return CubeHistory.model_validate(response)

    def get_starforce_history(
        self,
        result_count: int,
        base_date: Optional[datetime] = None,
        page_cursor: Optional[str] = None,
    ) -> StarforceHistory:
        """
        스타포스 강화 결과를 조회합니다.
        Fetches the starforce enhancement results.

        Args:
            result_count : 한번에 가져오려는 결과의 갯수(최소 10, 최대 1000)
                               The number of results to fetch at once (minimum 10, maximum 1000)
            base_date (datetime, optional): 조회 기준일(KST) (cursor가 없는 경우 필수이며 cursor와 함께 사용 불가)
                                            Query base date (KST) (required if cursor is not present and cannot be used with cursor)
            page_cursor (str, optional): 페이징 처리를 위한 cursor (date가 없는 경우 필수이며 date와 함께 사용 불가)
                                         Cursor for pagination (required if date is not present and cannot be used with date)
        """
        path = "/maplestory/v1/history/starforce"
        query = {
            "count": result_count,
            "date": dates.to_string(base_date) if base_date else base_date,
            "cursor": page_cursor,
        }
        response = fetch(path, query)
        return StarforceHistory.model_validate(response)

    def get_overall_ranking(
        self,
        world_name: Optional[str] = None,
        world_type: Optional[int] = None,
        class_name: Optional[str] = None,
        character_id: Optional[str] = None,
        page_number: int = 1,
        base_date: datetime = kst.yesterday(),
    ) -> OverallRanking:
        """
        종합 랭킹 정보를 조회합니다.
        Fetches the overall ranking information.

        Args:
            base_date : 조회 기준일(KST)
                                  Query base date (KST)
            world_name (str, optional): 월드 명
                                        World name
            world_type (int, optional): 월드 타입 (0:일반, 1:리부트) (기본 값은 0이며, world_name 입력 시 미 반영)
                                        World type (0: normal, 1: reboot) (default is 0 and not reflected when world_name is entered)
            class_name (str, optional): 직업 및 전직
                                        Job and pre-job
            character_id (str, optional): 캐릭터 식별자
                                          Character identifier
            page_number : 페이지 번호
                              Page number
        """
        path = "/maplestory/v1/ranking/overall"
        query = {
            "date": dates.to_string(base_date),
            "world_name": world_name,
            "world_type": world_type,
            "class": class_name,
            "ocid": character_id,
            "page": page_number,
        }
        response = fetch(path, query)
        return OverallRanking.model_validate(response)

    def get_union_ranking(
        self,
        world_name: str | None = None,
        ocid: str | None = None,
        page: int = 1,
        date: datetime = kst.yesterday(),
    ) -> UnionRanking:
        """유니온 랭킹 정보를 조회합니다.

        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.

        @param date: 조회 기준일(KST)
        @param world_name: 월드 명
        - 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3

        @param ocid: 캐릭터 식별자
        @param page: 페이지 번호
        """
        path = "/maplestory/v1/ranking/union"
        query = {
            "date": date.to_string(date),
            "world_name": world_name,
            "ocid": ocid,
            "page": page,
        }
        r = fetch(path, query)
        return UnionRanking.model_validate(r)

    def fetch_union_ranking(
        self,
        world: Optional[str] = None,
        character_id: Optional[str] = None,
        page_number: int = 1,
        date: datetime = kst.yesterday(),
    ) -> UnionRanking:
        """
        Fetches the union ranking information.

        Args:
            date : The reference date for the query (KST).
            world (Optional[str]): The name of the world.
                Possible values are: Scania, Bera, Luna, Zenith, Croa, Union, Elysium, Enosis, Red, Aurora, Arcane, Nova, Reboot, Reboot2, Burning, Burning2, Burning3.
            character_id (Optional[str]): The identifier of the character.
            page_number : The page number.

        Returns:
            UnionRanking: The union ranking information.

        Note:
            - Data can be queried from December 22, 2023.
            - Ranking information for the day can be queried from 8:30 AM.
            - Please note that the ocid may change due to game content changes. Please be careful when updating services based on ocid.
        """
        path = "/maplestory/v1/ranking/union"
        query = {
            "date": date.to_string(date),
            "world_name": world,
            "ocid": character_id,
            "page": page_number,
        }
        response = fetch(path, query)
        return UnionRanking.model_validate(response)

    def get_guild_ranking(
        self,
        ranking_type: int,
        world_name: str | None = None,
        guild_name: str | None = None,
        page: int = 1,
        date: datetime = kst.yesterday(),
    ) -> GuildRanking:
        """길드 랭킹 정보를 조회합니다.

        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.

        @param date: 조회 기준일(KST)
        @param ranking_type: 랭킹 타입 (0:주간 명성치, 1:플래그 레이스, 2:지하 수로)

        @param world_name: 월드 명
        - 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3

        @param guild_name: 길드 명
        @param page: 페이지 번호
        """
        path = "/maplestory/v1/ranking/guild"
        query = {
            "date": date.to_string(date),
            "ranking_type": ranking_type,
            "world_name": world_name,
            "guild_name": guild_name,
            "page": page,
        }
        r = fetch(path, query)
        return GuildRanking.model_validate(r)

    def fetch_guild_ranking(
        self,
        ranking_type: int,
        world: Optional[str] = None,
        guild: Optional[str] = None,
        page_number: int = 1,
        date: datetime = kst.yesterday(),
    ) -> GuildRanking:
        """
        Fetches the guild ranking information.

        Args:
            date : The reference date for the query (KST).
            ranking_type : The type of ranking (0: Weekly Fame, 1: Flag Race, 2: Underground Waterway).
            world (Optional[str]): The name of the world.
                Possible values are: Scania, Bera, Luna, Zenith, Croa, Union, Elysium, Enosis, Red, Aurora, Arcane, Nova, Reboot, Reboot2, Burning, Burning2, Burning3.
            guild (Optional[str]): The name of the guild.
            page_number : The page number.

        Returns:
            GuildRanking: The guild ranking information.

        Note:
            - Data can be queried from December 22, 2023.
            - Ranking information for the day can be queried from 8:30 AM.
            - Please note that the ocid may change due to game content changes. Please be careful when updating services based on ocid.
        """
        path = "/maplestory/v1/ranking/guild"
        query = {
            "date": date.to_string(date),
            "ranking_type": ranking_type,
            "world_name": world,
            "guild_name": guild,
            "page": page_number,
        }
        response = fetch(path, query)
        return GuildRanking.model_validate(response)

    def get_dojang_ranking(
        self,
        world_name: str | None = None,
        class_name: str | None = None,
        ocid: str | None = None,
        page: int = 1,
        difficulty: int = 1,
        date: datetime = kst.yesterday(),
    ) -> DojangRanking:
        """무릉도장 랭킹 정보를 조회합니다.

        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.

        @param date: 조회 기준일(KST)
        @param difficulty: 구간 (0:일반, 1:통달)
        @param world_name: 월드 명
        - 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3

        @param class_name: 직업 및 전직
        - 초보자-전체 전직, 전사-전체 전직, 전사-검사, 전사-파이터, 전사-페이지, 전사-스피어맨, 전사-크루세이더, 전사-나이트, 전사-버서커, 전사-히어로, 전사-팔라딘, 전사-다크나이트, 마법사-전체 전직, 마법사-매지션, 마법사-위자드(불,독), 마법사-위자드(썬,콜), 마법사-클레릭, 마법사-메이지(불,독), 마법사-메이지(썬,콜), 마법사-프리스트, 마법사-아크메이지(불,독), 마법사-아크메이지(썬,콜), 마법사-비숍, 궁수-전체 전직, 궁수-아처, 궁수-헌터, 궁수-사수, 궁수-레인저, 궁수-저격수, 궁수-보우마스터, 궁수-신궁, 궁수-아처(패스파인더), 궁수-에인션트아처, 궁수-체이서, 궁수-패스파인더, 도적-전체 전직, 도적-로그, 도적-어쌔신, 도적-시프, 도적-허밋, 도적-시프마스터, 도적-나이트로드, 도적-섀도어, 도적-세미듀어러, 도적-듀어러, 도적-듀얼마스터, 도적-슬래셔, 도적-듀얼블레이더, 해적-전체 전직, 해적-해적, 해적-인파이터, 해적-건슬링거, 해적-캐논슈터, 해적-버커니어, 해적-발키리, 해적-캐논블래스터, 해적-바이퍼, 해적-캡틴, 해적-캐논마스터, 기사단-전체 전직, 기사단-노블레스, 기사단-소울마스터, 기사단-플레임위자드, 기사단-윈드브레이커, 기사단-나이트워커, 기사단-스트라이커, 기사단-미하일, 아란-전체 전직, 에반-전체 전직, 레지스탕스-전체 전직, 레지스탕스-시티즌, 레지스탕스-배틀메이지, 레지스탕스-와일드헌터, 레지스탕스-메카닉, 레지스탕스-데몬슬레이어, 레지스탕스-데몬어벤져, 레지스탕스-제논, 레지스탕스-블래스터, 메르세데스-전체 전직, 팬텀-전체 전직, 루미너스-전체 전직, 카이저-전체 전직, 엔젤릭버스터-전체 전직, 초월자-전체 전직, 초월자-제로, 은월-전체 전직, 프렌즈 월드-전체 전직, 프렌즈 월드-키네시스, 카데나-전체 전직, 일리움-전체 전직, 아크-전체 전직, 호영-전체 전직, 아델-전체 전직, 카인-전체 전직, 라라-전체 전직, 칼리-전체 전직

        @param ocid: 캐릭터 식별자
        @param page: 페이지 번호
        """
        path = "/maplestory/v1/ranking/dojang"
        query = {
            "date": date.to_string(date),
            "world_name": world_name,
            "class": class_name,
            "ocid": ocid,
            "page": page,
            "difficulty": difficulty,
        }
        r = fetch(path, query)
        return DojangRanking.model_validate(r)

    def fetch_dojang_ranking(
        self,
        world: Optional[str] = None,
        job_class: Optional[str] = None,
        character_id: Optional[str] = None,
        page_number: int = 1,
        difficulty_level: int = 1,
        date: datetime = kst.yesterday(),
    ) -> DojangRanking:
        """
        Fetches the Dojang ranking information.

        Args:
            world (Optional[str]): The name of the world.
            job_class (Optional[str]): The name of the job class.
            character_id (Optional[str]): The identifier of the character.
            page_number : The page number.
            difficulty_level : The difficulty level (0: Normal, 1: Mastery).
            date : The reference date for the query (KST).

        Returns:
            DojangRanking: The Dojang ranking information.

        Note:
            - Data can be queried from December 22, 2023.
            - Ranking information can be queried from 8:30 AM.
            - Be careful when updating the service based on ocid, as the ocid may change due to game content changes.
        """
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
        self,
        world_name: str | None = None,
        ocid: str | None = None,
        page: int = 1,
        date: datetime = kst.yesterday(),
    ) -> TheSeedRanking:
        """더 시드 랭킹 정보를 조회합니다.

        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.

        @param date: 조회 기준일(KST)
        @param world_name: 월드 명
        - 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
        @param ocid: 캐릭터 식별자
        @param page: 페이지 번호
        """
        path = "/maplestory/v1/ranking/theseed"
        query = {
            "date": date.to_string(date),
            "world_name": world_name,
            "ocid": ocid,
            "page": page,
        }
        r = fetch(path, query)
        return TheSeedRanking.model_validate(r)

    def fetch_theseed_ranking(
        self,
        world: Optional[str] = None,
        character_id: Optional[str] = None,
        page_number: int = 1,
        date: datetime = kst.yesterday(),
    ) -> TheSeedRanking:
        """
        Fetches the TheSeed ranking information.

        Args:
            world (Optional[str]): The name of the world.
            character_id (Optional[str]): The identifier of the character.
            page_number : The page number.
            date : The reference date for the query (KST).

        Returns:
            TheSeedRanking: The TheSeed ranking information.

        Note:
            - Data can be queried from December 22, 2023.
            - Ranking information can be queried from 8:30 AM.
            - Be careful when updating the service based on ocid, as the ocid may change due to game content changes.
        """
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
        self, ocid: str | None = None, page: int = 1, date: datetime = kst.yesterday()
    ) -> AchievementRanking:
        """업적 랭킹 정보를 조회합니다.

        - 2023년 12월 22일 데이터부터 조회할 수 있습니다.
        - 오전 8시 30분부터 오늘의 랭킹 정보를 조회할 수 있습니다.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.

        @param date: 조회 기준일(KST)
        @param ocid: 캐릭터 식별자
        @param page: 페이지 번호
        """
        path = "/maplestory/v1/ranking/achievement"
        query = {
            "date": date.to_string(date),
            "ocid": ocid,
            "page": page,
        }
        r = fetch(path, query)
        return AchievementRanking.model_validate(r)

    def get_achievement_rankings(
        self,
        character_id: Optional[str] = None,
        page_number: int = 1,
        date: datetime = kst.yesterday(),
    ) -> AchievementRanking:
        """
        Fetches the achievement ranking information.

        Args:
            character_id (Optional[str]): The identifier of the character.
            page_number : The page number.
            date : The reference date for the query (KST).

        Returns:
            AchievementRanking: The achievement ranking information.

        Note:
            - Data can be queried from December 22, 2023.
            - Ranking information can be queried from 8:30 AM.
            - Be careful when updating the service based on ocid, as the ocid may change due to game content changes.
        """
        path = "/maplestory/v1/ranking/achievement"
        query = {
            "date": dates.to_string(date),
            "ocid": character_id,
            "page": page_number,
        }
        response = fetch_data(path, query)
        return AchievementRanking.model_validate(response)
