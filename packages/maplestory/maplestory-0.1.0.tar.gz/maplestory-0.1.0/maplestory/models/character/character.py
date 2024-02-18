from pydantic import BaseModel


class CharacterId(BaseModel):
    """캐릭터 식별자(ocid)

    Attributes:
        ocid (str): 캐릭터 식별자
    """

    ocid: str
