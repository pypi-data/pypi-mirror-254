"""
이 모듈은 메이플스토리 게임의 유니온 정보를 가져오고 처리하는 함수를 제공합니다.
This module provides functions to fetch and handle Union information in the MapleStory game.

이 모듈에는 주어진 캐릭터 식별자(ocid)와 참조 날짜에 대한 유니온 레벨과 유니온 등급 정보를 가져오는 `get_union_info` 함수가 포함되어 있습니다.
It includes a function `get_union_info` which fetches the Union level and Union rank information 
for a given character identifier (ocid) and reference date.

이 모듈은 `maplestory.models.union` 패키지의 `Union`과 `UnionRaider` 모델과 `maplestory.utils.date`와 `maplestory.utils.network` 패키지의 유틸리티 함수를 사용합니다.
The module uses the `Union` and `UnionRaider` models from the `maplestory.models.union` package 
and utility functions from the `maplestory.utils.date` and `maplestory.utils.network` packages.
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
    """
    유니온 레벨 및 유니온 등급 정보를 조회합니다.
    Fetches the Union level and Union rank information.

    Args:
        character_ocid: 캐릭터의 식별자(ocid).
                        The identifier (ocid) of the character.
        date: 조회 기준일 (KST).
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


def get_union_raider_info_by_ocid(
    character_ocid: str,
    date: datetime = kst.yesterday(),
) -> UnionRaider:
    """
    유니온에 배치된 공격대원 효과 및 공격대 점령 효과 등 상세 정보를 조회합니다.
    Fetches the detailed information of the effect of the attack members placed in the Union and the effect of the attack occupation.

    Args:
        character_ocid: 캐릭터의 식별자(ocid).
                        The identifier (ocid) of the character.
        date: 조회 기준일 (KST).
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


def get_union_artifact_info_by_ocid(
    character_ocid: str,
    date: datetime = kst.yesterday(),
) -> UnionArtifact:
    """
    유니온 아티팩트 정보를 조회합니다.
    Fetches the Union Artifact information.

    Args:
        character_ocid: 캐릭터의 식별자(ocid).
                        The identifier (ocid) of the character.
        date: 조회 기준일 (KST).
                        Reference date for the query (KST).

    Returns:
        UnionArtifact: 유니온 아티팩트 정보.
                       The information of the Union Artifact.
    """

    path = "/maplestory/v1/user/union-artifact"
    query = {
        "ocid": character_ocid,
        "date": dates.to_string(date),
    }
    response = fetch(path, query)

    return UnionArtifact.model_validate(response)
