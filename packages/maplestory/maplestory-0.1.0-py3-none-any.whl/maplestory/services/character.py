from datetime import datetime

from pydantic import BaseModel, computed_field

from maplestory.apis.character import (
    get_basic_character_info_by_ocid,
    get_character_ability_by_ocid,
    get_character_android_equipment_by_ocid,
    get_character_beauty_equipment_by_ocid,
    get_character_cashitem_equipment_by_ocid,
    get_character_dojang_record_by_ocid,
    get_character_equipment_by_ocid,
    get_character_hexamatrix_by_ocid,
    get_character_hexamatrix_stat_by_ocid,
    get_character_hyper_stat_by_ocid,
    get_character_link_skill_by_ocid,
    get_character_ocid,
    get_character_pet_equipment_by_ocid,
    get_character_propensity_by_ocid,
    get_character_set_effect_by_ocid,
    get_character_skill_by_ocid,
    get_character_stat_by_ocid,
    get_character_symbol_equipment_by_ocid,
    get_character_vmatrix_by_ocid,
    get_popularity_by_ocid,
)
from maplestory.models.character import (
    Ability,
    AndroidEquipment,
    BeautyEquipment,
    CashitemEquipment,
    CharacterBasic,
    CharacterDojang,
    CharacterEquipment,
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
from maplestory.utils.kst import yesterday


class Character(BaseModel):
    """캐릭터 식별자(ocid)

    Attributes:
        name: 캐릭터명
        date: 조회 기준일 (KST)
    """

    name: str
    date: datetime = yesterday()

    @computed_field
    @property
    def id(self) -> str:
        return get_character_id(self.name)

    @property
    def ocid(self) -> str:
        return self.id

    @computed_field
    @property
    def basic(self) -> CharacterBasic:
        return get_basic_character_info(self.name, self.date)

    @property
    def popularity(self) -> Popularity:
        return get_popularity(self.name, self.date)

    @property
    def stat(self) -> CharacterStat:
        return get_character_stat(self.name, self.date)

    @property
    def hyper_stat(self) -> HyperStat:
        return get_character_hyper_stat(self.name, self.date)

    @property
    def propensity(self) -> Propensity:
        return get_character_propensity(self.name, self.date)

    @property
    def ability(self) -> Ability:
        return get_character_ability(self.name, self.date)

    @property
    def equipment(self) -> CharacterEquipment:
        return get_character_equipment(self.name, self.date)

    @property
    def cashitem_equipment(self) -> CashitemEquipment:
        return get_character_cashitem_equipment(self.name, self.date)

    @property
    def symbol_equipment(self) -> SymbolEquipment:
        return get_character_symbol_equipment(self.name, self.date)

    @property
    def set_effect(self) -> SetEffect:
        return get_character_set_effect(self.name, self.date)

    @property
    def beauty_equipment(self) -> BeautyEquipment:
        return get_character_beauty_equipment(self.name, self.date)

    @property
    def android_equipment(self) -> AndroidEquipment:
        return get_character_android_equipment(self.name, self.date)

    @property
    def pet_equipment(self) -> CharacterPet:
        return get_character_pet_equipment(self.name, self.date)

    @property
    def skill_0th(self) -> CharacterSkill:
        return get_character_skill(self.name, 0, self.date)

    @property
    def skill_1st(self) -> CharacterSkill:
        return get_character_skill(self.name, 1, self.date)

    @property
    def skill_2nd(self) -> CharacterSkill:
        return get_character_skill(self.name, 2, self.date)

    @property
    def skill_3rd(self) -> CharacterSkill:
        return get_character_skill(self.name, 3, self.date)

    @property
    def skill_4th(self) -> CharacterSkill:
        return get_character_skill(self.name, 4, self.date)

    @property
    def skill_5th(self) -> CharacterSkill:
        return get_character_skill(self.name, 5, self.date)

    @property
    def skill_6th(self) -> CharacterSkill:
        return get_character_skill(self.name, 6, self.date)

    @property
    def link_skill(self) -> CharacterLinkSkill:
        return get_character_link_skill(self.name, self.date)

    @property
    def vmatrix(self) -> VMatrix:
        return get_character_vmatrix(self.name, self.date)

    @property
    def hexamatrix(self) -> HexaMatrix:
        return get_character_hexamatrix(self.name, self.date)

    @property
    def hexamatrix_stat(self) -> HexaMatrixStat:
        return get_character_hexamatrix_stat(self.name, self.date)

    @property
    def dojang_record(self) -> CharacterDojang:
        return get_character_dojang_record(self.name, self.date)


def get_character_id(character_name: str) -> str:
    """
    캐릭터의 식별자(ocid)를 조회합니다.
    Fetches the identifier (ocid) of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.

    Returns:
        str: 주어진 이름의 캐릭터 식별자.
             The character with the given name.

    Note:
        - 2023년 12월 21일부터 데이터를 조회할 수 있습니다.
          Data can be queried from December 21, 2023.
        - 캐릭터 정보 조회 API는 일자별 데이터로 매일 오전 1시부터 전일 데이터 조회가 가능합니다.
          The character information query API provides daily data, and data for the previous day can be queried from 1 AM every day.
        - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
          The ocid may change due to game content changes. Please be careful when updating services based on ocid.
    """

    return get_character_ocid(character_name)


def get_basic_character_info(
    character_name: str,
    date: datetime = yesterday(),
) -> CharacterBasic:
    """
    캐릭터의 기본 정보를 조회합니다.
    Fetches the basic information of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
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

    character_ocid = get_character_id(character_name)
    return get_basic_character_info_by_ocid(character_ocid, date)


def get_popularity(
    character_name: str,
    date: datetime = yesterday(),
) -> Popularity:
    """
    캐릭터의 인기도 정보를 조회합니다.
    Fetches the popularity information of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterPopularity: 캐릭터의 인기도 정보.
                             The popularity information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_popularity_by_ocid(character_ocid, date)


def get_character_stat(
    character_name: str,
    date: datetime = yesterday(),
) -> CharacterStat:
    """
    캐릭터의 종합능력치 정보를 조회합니다.
    Fetches the comprehensive ability information of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterStat: 캐릭터의 종합능력치 정보.
                       The comprehensive ability information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_stat_by_ocid(character_ocid, date)


def get_character_hyper_stat(
    character_name: str,
    date: datetime = yesterday(),
) -> HyperStat:
    """
    캐릭터의 하이퍼스탯 정보를 조회합니다.
    Fetches the hyper stat information of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterHyperStat: 캐릭터의 하이퍼스탯 정보.
                            The hyper stat information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_hyper_stat_by_ocid(character_ocid, date)


def get_character_propensity(
    character_name: str,
    date: datetime = yesterday(),
) -> Propensity:
    """
    캐릭터의 성향 정보를 조회합니다.
    Fetches the propensity information of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterPropensity: 캐릭터의 성향 정보.
                             The propensity information of the character.
    """
    character_ocid = get_character_id(character_name)
    return get_character_propensity_by_ocid(character_ocid, date)


def get_character_ability(
    character_name: str,
    date: datetime = yesterday(),
) -> Ability:
    """
    캐릭터의 어빌리티 정보를 조회합니다.
    Fetches the ability information of a character.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterAbility: 캐릭터의 어빌리티 정보.
                          The ability information of the character.
    """
    character_ocid = get_character_id(character_name)
    return get_character_ability_by_ocid(character_ocid, date)


def get_character_equipment(
    character_name: str,
    date: datetime = yesterday(),
) -> CharacterEquipment:
    """
    장착한 장비 중 캐시 장비를 제외한 나머지 장비 정보를 조회합니다.
    Fetches the information of equipped items excluding cash items.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterItemEquipment: 캐릭터의 장비 정보.
                                The equipment information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_equipment_by_ocid(character_ocid, date)


def get_character_cashitem_equipment(
    character_name: str,
    date: datetime = yesterday(),
) -> CashitemEquipment:
    """
    장착한 캐시 장비 정보를 조회합니다.
    Fetches the information of equipped cash items.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterCashitemEquipment: 캐릭터의 캐시 장비 정보.
                                    The cash item equipment information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_cashitem_equipment_by_ocid(character_ocid, date)


def get_character_symbol_equipment(
    character_name: str,
    date: datetime = yesterday(),
) -> SymbolEquipment:
    """
    장착한 심볼 정보를 조회합니다.
    Fetches the equipped symbol information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterSymbolEquipment: 캐릭터의 심볼 장비 정보.
                                  The symbol equipment information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_symbol_equipment_by_ocid(character_ocid, date)


def get_character_set_effect(
    character_name: str,
    date: datetime = yesterday(),
) -> SetEffect:
    """
    적용받고 있는 세트 효과 정보를 조회합니다.
    Fetches the applied set effect information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterSetEffect: 캐릭터의 세트 효과 정보.
                            The set effect information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_set_effect_by_ocid(character_ocid, date)


def get_character_beauty_equipment(
    character_name: str,
    date: datetime = yesterday(),
) -> BeautyEquipment:
    """
    캐릭터 헤어, 성형, 피부 정보를 조회합니다.
    Fetches the character's hair, plastic surgery, and skin information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterBeautyEquipment: 캐릭터의 미용 장비 정보.
                                  The beauty equipment information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_beauty_equipment_by_ocid(character_ocid, date)


def get_character_android_equipment(
    character_name: str,
    date: datetime = yesterday(),
) -> AndroidEquipment:
    """
    장착한 안드로이드 정보를 조회합니다.
    Fetches the equipped android information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterAndroidEquipment: 캐릭터의 안드로이드 장비 정보.
                                   The android equipment information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_android_equipment_by_ocid(character_ocid, date)


def get_character_pet_equipment(
    character_name: str,
    date: datetime = yesterday(),
) -> CharacterPet:
    """
    장착한 펫 및 펫 스킬, 장비 정보를 조회합니다.
    Fetches the equipped pet and pet skill, equipment information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterPetEquipment: 캐릭터의 펫 장비 정보.
                               The pet equipment information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_pet_equipment_by_ocid(character_ocid, date)


def get_character_skill(
    character_name: str,
    skill_grade: int,
    date: datetime = yesterday(),
) -> CharacterSkill:
    """
    캐릭터 스킬과 하이퍼 스킬 정보를 조회합니다.
    Fetches the character's skill and hyper skill information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        skill_grade : 조회하고자 하는 전직 차수.
                      The job advancement grade to query.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterSkill: 캐릭터의 스킬 정보.
                        The skill information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_skill_by_ocid(character_ocid, skill_grade, date)


def get_character_link_skill(
    character_name: str,
    date: datetime = yesterday(),
) -> CharacterLinkSkill:
    """
    장착 링크 스킬 정보를 조회합니다.
    Fetches the equipped link skill information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterLinkSkill: 캐릭터의 링크 스킬 정보.
                            The link skill information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_link_skill_by_ocid(character_ocid, date)


def get_character_vmatrix(
    character_name: str,
    date: datetime = yesterday(),
) -> VMatrix:
    """
    V매트릭스 슬롯 정보와 장착한 V코어 정보를 조회합니다.
    Fetches the VMatrix slot information and the equipped VCore information.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterVMatrix: 캐릭터의 V매트릭스 정보.
                          The VMatrix information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_vmatrix_by_ocid(character_ocid, date)


def get_character_hexamatrix(
    character_name: str,
    date: datetime = yesterday(),
) -> HexaMatrix:
    """
    HEXA 매트릭스에 장착한 HEXA 코어 정보를 조회합니다.
    Fetches the HEXA core information equipped in the HEXA matrix.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterHexaMatrix: 캐릭터의 HEXA 매트릭스 정보.
                             The HEXA matrix information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_hexamatrix_by_ocid(character_ocid, date)


def get_character_hexamatrix_stat(
    character_name: str,
    date: datetime = yesterday(),
) -> HexaMatrixStat:
    """
    HEXA 매트릭스에 설정한 HEXA 스탯 정보를 조회합니다.
    Fetches the HEXA stat information set in the HEXA matrix.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterHexaMatrixStat: 캐릭터의 HEXA 매트릭스 스탯 정보.
                                 The HEXA matrix stat information of the character.
    """

    character_ocid = get_character_id(character_name)
    return get_character_hexamatrix_stat_by_ocid(character_ocid, date)


def get_character_dojang_record(
    character_name: str,
    date: datetime = yesterday(),
) -> CharacterDojang:
    """
    캐릭터 무릉도장 최고 기록 정보를 조회합니다.
    Fetches the highest record information of the character's Dojang.

    Args:
        character_name : 캐릭터의 이름.
                         The name of the character.
        date : 조회 기준일 (KST).
                         Reference date for the query (KST).

    Returns:
        CharacterDojang: 캐릭터의 무릉도장 최고 기록 정보.
                         The highest record information of the character's Dojang.
    """

    character_ocid = get_character_id(character_name)
    return get_character_dojang_record_by_ocid(character_ocid, date)
