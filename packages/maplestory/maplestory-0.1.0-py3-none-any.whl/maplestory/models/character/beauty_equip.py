from datetime import datetime

from pydantic import BaseModel


class HairInfo(BaseModel):
    """캐릭터 헤어 정보

    Attributes:
        hair_name (str): 헤어 명
        base_color (str): 헤어 베이스 컬러
        mix_color (str | None): 헤어 믹스 컬러
        mix_rate (str): 헤어 믹스 컬러의 염색 비율
    """

    hair_name: str
    base_color: str
    mix_color: str | None
    mix_rate: str


class FaceInfo(BaseModel):
    """캐릭터 성형 정보

    Attributes:
        face_name (str): 성형 명
        base_color (str): 성형 베이스 컬러
        mix_color (str | None): 성형 믹스 컬러
        mix_rate (str): 성형 믹스 컬러의 염색 비율
    """

    face_name: str
    base_color: str
    mix_color: str | None
    mix_rate: str


class BeautyEquipment(BaseModel):
    """캐릭터 헤어, 성형, 피부 정보

    Attributes:
        date (datetime): 조회 기준일 (KST)
        character_gender (str): 캐릭터 성별
        character_class (str): 캐릭터 직업
        character_hair (HairInfo): 캐릭터 헤어 정보 (제로인 경우 알파, 엔젤릭버스터인 경우 일반 모드)
        character_face (FaceInfo): 캐릭터 성형 정보 (제로인 경우 알파, 엔젤릭버스터인 경우 일반 모드)
        character_skin_name (str): 캐릭터 피부 명 (제로인 경우 알파, 엔젤릭버스터인 경우 일반 모드)
        additional_character_hair (HairInfo | None): 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에 적용 중인 헤어 정보
        additional_character_face (FaceInfo | None): 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에 적용 중인 성형 정보
        additional_character_skin_name (str | None): 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에 적용 중인 피부 명
    """

    date: datetime
    character_gender: str
    character_class: str
    character_hair: HairInfo
    character_face: FaceInfo
    character_skin_name: str
    additional_character_hair: HairInfo | None
    additional_character_face: FaceInfo | None
    additional_character_skin_name: str | None
