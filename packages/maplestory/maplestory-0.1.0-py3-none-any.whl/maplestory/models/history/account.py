from pydantic import BaseModel


class Account(BaseModel):
    """계정 식별자(ouid) 정보

    Attributes:
        ouid: 계정 식별자
    """

    ouid: str
