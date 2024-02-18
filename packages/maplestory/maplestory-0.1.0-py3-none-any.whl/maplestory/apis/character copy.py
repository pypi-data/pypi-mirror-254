"""

Note:
    - 2023년 12월 21일부터 데이터를 조회할 수 있습니다.
        Data can be queried from December 21, 2023.
    - 캐릭터 정보 조회 API는 일자별 데이터로 매일 오전 1시부터 전일 데이터 조회가 가능합니다. (예를 들어, 12월 22일 데이터를 조회하면 22일 00시부터 23일의 00시 사이의 데이터가 조회됩니다.)
        The character information query API provides daily data, and data for the previous day can be queried from 1 AM every day. (For example, if you query data for December 22, you will get data from 00:00 on the 22nd to 00:00 on the 23rd.)
    - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
        The ocid may change due to game content changes. Please be careful when updating services based on ocid.
"""
from datetime import datetime

from rich import print

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
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
from maplestory.utils.network import fetch


def get_basic_character_info_by_ocid(
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


def get_popularity_by_ocid(
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


def get_character_stat_by_ocid(
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


def get_character_hyper_stat_by_ocid(
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


def get_character_propensity_by_ocid(
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


def get_character_ability_by_ocid(
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


def get_character_equipment_by_ocid(
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


def get_character_cashitem_equipment_by_ocid(
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

    try:
        _ = CashitemEquipment.model_validate(response)
    except Exception as e:
        print(e)
        print(f"{api_response = }")

    return CashitemEquipment.model_validate(response)


def get_character_symbol_equipment_by_ocid(
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


def get_character_set_effect_by_ocid(
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


def get_character_beauty_equipment_by_ocid(
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


def get_character_android_equipment_by_ocid(
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


def get_character_pet_equipment_by_ocid(
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


def get_character_skill_by_ocid(
    character_ocid: str,
    skill_grade: int,
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

    # print(f"api_response: {api_response}")
    # FIXME: 6차 전직을 하지 않았을 경우, 아래와 같이 결과가 온다.
    # {'date': '2024-01-19T00:00+09:00', 'character_class': '아델',
    #  'character_skill_grade': None, 'character_skill': []}
    if api_response.get("character_skill_grade") is None:
        api_response["character_skill_grade"] = skill_grade

    return CharacterSkill.model_validate(response)


def get_character_link_skill_by_ocid(
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


def get_character_vmatrix_by_ocid(
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


def get_character_hexamatrix_by_ocid(
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


def get_character_hexamatrix_stat_by_ocid(
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


def get_character_dojang_record_by_ocid(
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
