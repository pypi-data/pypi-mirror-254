from __future__ import annotations

from enum import Enum

from httpx import HTTPStatusError, Response
from pydantic import BaseModel, Field, computed_field


class APIErrorCode(str, Enum):
    """API 에러 코드를 나타내는 Enum 클래스입니다. 각 코드는 특정 API 에러 상황을 나타냅니다.

    References:
        https://openapi.nexon.com/guide/request-api/#error-code-table
    """

    OPENAPI00001 = "서버 내부 오류"
    OPENAPI00002 = "권한이 없는 경우"
    OPENAPI00003 = "유효하지 않은 식별자"
    OPENAPI00004 = "파라미터 누락 또는 유효하지 않음"
    OPENAPI00005 = "유효하지 않은 API KEY"
    OPENAPI00006 = "유효하지 않은 게임 또는 API PATH"
    OPENAPI00007 = "API 호출량 초과"
    OPENAPI00009 = "데이터 준비 중"

    @classmethod
    def from_code(cls, code: str) -> APIErrorCode:
        """
        문자열 코드를 해당 Enum 값으로 변환합니다.

        Args:
            code (str): 변환할 문자열 코드입니다.

        Returns:
            APIErrorCode: 해당하는 Enum 값입니다.
        """
        return cls._member_map_[code]


class ErrorMessage(BaseModel):
    """에러 메시지를 나타내는 클래스입니다.

    각 에러 메시지는 특정 에러 코드(`code`)와 그에 대한 설명(`message`)을 포함합니다.

    Attributes:
        code (str): 에러 코드 (예: OPENAPI00001)
        message (str): 에러 설명

    Examples:
        >>> error = ErrorMessage(name="OPENAPI00004", message="Please input valid parameter")
        >>> error.code
        'OPENAPI00004'
        >>> error.message
        'Please input valid parameter'
    """

    code: str = Field(alias="name")
    message: str


class APIError(HTTPStatusError):
    """API 에러를 나타내는 클래스입니다.

    각 API 에러는 에러 코드(`code`), 에러 메시지(`message`), 그리고 HTTP 상태 코드(`status`)를 포함합니다.

    Attributes:
        code (str): 에러 코드
        message (str): 에러 메시지
        status (int): HTTP 상태 코드
        description (str): 에러 코드에 대한 설명
    """

    code: str
    message: str
    status: int

    def __init__(
        self,
        error: ErrorMessage,
        response: Response,
    ):
        super().__init__(
            f"{error.message} ({error.code})",
            request=response.request,
            response=response,
        )
        self.code = error.code
        self.message = error.message
        self.status = response.status_code

    @computed_field
    @property
    def description(self) -> str:
        """에러 코드에 대한 설명을 반환합니다."""
        return APIErrorCode.from_code(self.code).value
