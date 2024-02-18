from datetime import datetime

from pydantic import BaseModel


class HexaMatrixStatCore(BaseModel):
    """HEXA 코어 스탯 정보

    Attributes:
        slot_id (str): 슬롯 인덱스
        main_stat_name (str): 메인 스탯 명
        sub_stat_name_1 (str): 첫 번째 서브 명
        sub_stat_name_2 (str): 두 번째 서브 명
        main_stat_level (int): 메인 스탯 레벨
        sub_stat_level_1 (int): 첫 번째 서브 레벨
        sub_stat_level_2 (int): 두 번째 서브 레벨
        stat_grade (int): 스탯 코어 등급
    """

    slot_id: str
    main_stat_name: str
    sub_stat_name_1: str
    sub_stat_name_2: str
    main_stat_level: int
    sub_stat_level_1: int
    sub_stat_level_2: int
    stat_grade: int


class HexaMatrixStat(BaseModel):
    """HEXA 코어 스탯

    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        character_class (str | None): 캐릭터 직업
        character_hexa_stat_core (list[HexaMatrixStatCore]): HEXA 코어 스탯 정보
        preset_hexa_stat_core (list[HexaMatrixStatCore]): HEXA 코어 스탯 정보 (프리셋)

    Notes:
        HEXA 코어 스탯 정보가 없는 경우 character_class가 None으로 표기됩니다.
    """

    date: datetime
    character_class: str | None
    character_hexa_stat_core: list[HexaMatrixStatCore]
    preset_hexa_stat_core: list[HexaMatrixStatCore]
