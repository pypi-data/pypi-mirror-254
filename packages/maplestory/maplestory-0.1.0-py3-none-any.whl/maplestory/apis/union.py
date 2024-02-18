"""유니온 정보 조회 API를 제공하는 모듈입니다.

Note:
    - 2023년 12월 21일 데이터부터 조회할 수 있습니다.
    - 유니온 정보 조회 API는 일자별 데이터로 매일 오전 1시부터 전일 데이터 조회가 가능합니다.
      (예를 들어, 12월 22일 데이터를 조회하면 22일 00시부터 23일의 00시 사이의 데이터가 조회됩니다.)
    - 게임 콘텐츠 변경으로 ocid가 변경될 수 있습니다. ocid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
"""

from datetime import datetime

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
from maplestory.models.union import Union, UnionArtifact, UnionRaider
from maplestory.utils.network import fetch


def get_union_info_by_ocid(
    character_ocid: str,
    date: datetime = kst.yesterday(),
) -> Union:
    """유니온 레벨 및 유니온 등급 정보를 조회합니다.

    Args:
        character_ocid: 캐릭터의 식별자(ocid).
        date: 조회 기준일 (KST).

    Returns:
        Union: 유니온의 레벨 및 등급 정보.
    """

    path = "/maplestory/v1/user/union"
    query = {
        "ocid": character_ocid,
        "date": dates.to_string(date),
    }
    response = fetch(path, query)

    return Union.model_validate(response)


def get_union_raider_info_by_ocid(
    character_ocid: str,
    date: datetime = kst.yesterday(),
) -> UnionRaider:
    """
    유니온에 배치된 공격대원 효과 및 공격대 점령 효과 등 상세 정보를 조회합니다.

    Args:
        character_ocid: 캐릭터의 식별자(ocid).
        date: 조회 기준일 (KST).

    Returns:
        UnionRaider: 유니온에 배치된 공격대원 효과 및 공격대 점령 효과 등의 상세 정보.
    """

    path = "/maplestory/v1/user/union-raider"
    query = {
        "ocid": character_ocid,
        "date": dates.to_string(date),
    }
    response = fetch(path, query)

    return UnionRaider.model_validate(response)


def get_union_artifact_info_by_ocid(
    character_ocid: str,
    date: datetime = kst.yesterday(),
) -> UnionArtifact:
    """
    유니온 아티팩트 정보를 조회합니다.

    Args:
        character_ocid: 캐릭터의 식별자(ocid).
        date: 조회 기준일 (KST).

    Returns:
        UnionArtifact: 유니온 아티팩트 정보.
    """

    path = "/maplestory/v1/user/union-artifact"
    query = {
        "ocid": character_ocid,
        "date": dates.to_string(date),
    }
    response = fetch(path, query)

    return UnionArtifact.model_validate(response)
