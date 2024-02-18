from datetime import datetime

from pydantic import BaseModel

from maplestory.types.character import CharacterGender

from ..types import WorldName


class CharacterBasic(BaseModel):
    """캐릭터 기본 정보

    Attributes:
        date (datetime): 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) example: 2023-12-21T00:00+09:00
        character_name (str): 캐릭터 명
        world_name (str): 월드 명
        character_gender (str): 캐릭터 성별
        character_class (str): 캐릭터 직업
        character_class_level (int): 캐릭터 직업 차수
        character_level (int): 캐릭터 레벨
        character_exp (int): 현재 레벨에서 보유한 경험치
        character_exp_rate (str): 현재 레벨에서 경험치 퍼센트
        character_guild_name (str | None): 캐릭터 소속 길드 명
        character_image (str): 캐릭터 외형 이미지
    """

    date: datetime
    character_name: str
    world_name: str
    character_gender: str
    character_class: str
    character_class_level: int
    character_level: int
    character_exp: int
    character_exp_rate: str
    character_guild_name: str | None
    character_image: str

    @property
    def 조회기준일(self) -> str:
        return self.date

    @property
    def 캐릭터명(self) -> str:
        return self.character_name

    @property
    def 월드명(self) -> str:
        return self.world_name

    @property
    def 캐릭터성별(self) -> str:
        return self.character_gender

    @property
    def 캐릭터직업(self) -> str:
        return self.character_class

    @property
    def 캐릭터직업차수(self) -> str:
        return self.character_class_level

    @property
    def 레벨(self) -> int:
        return self.character_level

    @property
    def 현재레벨경험치(self) -> int:
        return self.character_exp

    @property
    def 누적경험치(self) -> int:
        # TODO: 누적 경험치 계산
        return self.character_exp

    @property
    def 현재레벨경험치퍼센트(self) -> str:
        return self.character_exp_rate

    @property
    def 길드(self) -> str:
        return self.character_guild_name

    @property
    def 이미지(self) -> str:
        return self.character_image


# character_image = "https://open.api.nexon.com/static/maplestory/Character/HDLDFHOOPBEBJBCFGPJIADFOMCOHAHLBBNFJGDENBFADHHPMBKKIDKBDNNGDBOJLMFIFFDDHFGOIMDIIAHKHGLDIELPAAHCGCCBKBFGKFOCMONOIKEMAOABKIBEBPHAAKADNLOMJEEHMDDDBJMELIINOAGIBEHMIPIBJKMJMOKAEGAJFNFFEJCGDDAFBBNFLODBGEEMHGNMKIPKHFIFBDCOIBMEDCAALIDLEEHIPCMNBCPDCAJHFKJABPHCCPHII.png"

# https://docs.pydantic.dev/latest/concepts/json_schema/#field-customisation
# num: int = Field(..., gt=0, le=10)
# foo: int = Field(..., gt=0, lt=10)
# character_level: conint(min=1, max=300)
# snap: int = Field(
#     42,
#     title='The Snap',
#     description='this is the value of snap',
#     gt=30,
#     lt=50,
# )


# https://docs.pydantic.dev/1.10/usage/types/#constrained-types
