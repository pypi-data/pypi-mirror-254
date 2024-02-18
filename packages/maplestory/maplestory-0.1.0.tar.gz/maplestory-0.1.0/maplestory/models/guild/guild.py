from pydantic import BaseModel


class GuildModel(BaseModel):
    """길드 식별자(oguild_id) 정보

    Attributes:
        oguild_id: 길드 식별자
    """

    oguild_id: str

    @property
    def id(self) -> str:
        return self.oguild_id
