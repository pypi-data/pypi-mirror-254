from __future__ import annotations

from enum import Enum

from httpx import HTTPStatusError, Response
from pydantic import BaseModel, Field, computed_field


# https://stackoverflow.com/questions/50473951/how-can-i-attach-documentation-to-members-of-a-python-enum
class DocEnum(Enum):
    def __new__(cls, value, doc=None):
        self = object.__new__(cls)  # calling super().__new__(value) here would fail
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self


class APIErrorCode(str, Enum):
    """API 에러 코드를 나타내는 Enum 클래스입니다. 각 코드는 특정 API 에러 상황을 나타냅니다.

    Attributes:
        OPENAPI00001: 서버 내부 오류
        OPENAPI00002: 권한이 없는 경우
        OPENAPI00003: 유효하지 않은 식별자
        OPENAPI00004: 파라미터 누락 또는 유효하지 않음
        OPENAPI00005: 유효하지 않은 API KEY
        OPENAPI00006: 유효하지 않은 게임 또는 API PATH
        OPENAPI00007: API 호출량 초과
        OPENAPI00009: 데이터 준비 중
    """

    """Enum class representing API error codes. 
    
    Each code represents a specific API error situation.
    
    Attributes:
        OPENAPI00001: Server internal error
        OPENAPI00002: No permission
        OPENAPI00003: Invalid identifier
        OPENAPI00004: Missing or invalid parameter
        OPENAPI00005: Invalid API KEY
        OPENAPI00006: Invalid game or API PATH
        OPENAPI00007: API call limit exceeded
        OPENAPI00009: Data preparation in progress
    """
    """API 에러 코드를 나타내는 Enum 클래스입니다. 각 코드는 특정 API 에러 상황을 나타냅니다.
    
    Attributes:
        OPENAPI00001: 서버 내부 오류
        OPENAPI00002: 권한이 없는 경우
        OPENAPI00003: 유효하지 않은 식별자
        OPENAPI00004: 파라미터 누락 또는 유효하지 않음
        OPENAPI00005: 유효하지 않은 API KEY
        OPENAPI00006: 유효하지 않은 게임 또는 API PATH
        OPENAPI00007: API 호출량 초과
        OPENAPI00009: 데이터 준비 중    
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
        """
        Converts a string code to its corresponding Enum value.
        
        Args:
            code (str): The string code to convert.
        
        Returns:
            APIErrorCode: The corresponding Enum value.
        """
        return cls._member_map_[code]


class ErrorMessage(BaseModel):
    """에러 메세지

    Attributes:
        code: 에러 코드 (예: OPENAPI00001)
        message: 에러 설명

    Examples:
        >>> error = ErrorMessage(name="OPENAPI00004", message="Please input valid parameter")
        >>> error.code
        'OPENAPI00004'
        >>> error.message
        'Please input valid parameter'
    """

    code: str = Field(alias="name")
    message: str


class ErrorResponse(BaseModel):
    error: ErrorMessage


class APIError(HTTPStatusError):
    """MapleStory API Exception"""

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
        return APIErrorCode.from_code(self.code).value


# ERROR_LIST = [
#     ("OPENAPI00001", 500, "Internal Server Error", "서버 내부 오류")
#     ("OPENAPI00002", 403, "Forbidden", "권한이 없는 경우")
#     ("OPENAPI00003", 400, "Bad Request", "유효하지 않은 식별자")
#     ("OPENAPI00004", 400, "Bad Request", "파라미터 누락 또는 유효하지 않음")
#     ("OPENAPI00005", 400, "Bad Request", "유효하지 않은 API KEY")
#     ("OPENAPI00006", 400, "Bad Request", "유효하지 않은 게임 또는 API PATH")
#     ("OPENAPI00007", 429, "Too Many Requests", "API 호출량 초과")
#     ("OPENAPI00009", 400, "Bad Request", "데이터 준비 중")
# ]
# class APIException(Exception):
#     def __init__(self, error: ErrorMessage):
#         self.error_code = error.code
#         self.message = error.message
#         super().__init__(error.message)


# ("에러 코드", "응답 코드", "응답명", "설명")
# ("OPENAPI00001", 500, "Internal Server Error", "서버 내부 오류")
# ("OPENAPI00002", 403, "Forbidden", "권한이 없는 경우")
# ("OPENAPI00003", 400, "Bad Request", "유효하지 않은 식별자")
# ("OPENAPI00004", 400, "Bad Request", "파라미터 누락 또는 유효하지 않음")
# ("OPENAPI00005", 400, "Bad Request", "유효하지 않은 API KEY")
# ("OPENAPI00006", 400, "Bad Request", "유효하지 않은 게임 또는 API PATH")
# ("OPENAPI00007", 429, "Too Many Requests", "API 호출량 초과")
# ("OPENAPI00009", 400, "Bad Request", "데이터 준비 중")


# class APIErrorCode(str, Enum):
#     Unauthorized = "unauthorized"
#     """The bearer token is not valid."""

#     RestrictedResource = "restricted_resource"
#     """Given the bearer token used, the client doesn't have permission to
#     perform this operation."""

#     ObjectNotFound = "object_not_found"
#     """Given the bearer token used, the resource does not exist.
#     This error can also indicate that the resource has not been shared with owner
#     of the bearer token."""

#     RateLimited = "rate_limited"
#     """This request exceeds the number of requests allowed. Slow down and try again."""

#     InvalidJSON = "invalid_json"
#     """The request body could not be decoded as JSON."""

#     InvalidRequestURL = "invalid_request_url"
#     """The request URL is not valid."""

#     InvalidRequest = "invalid_request"
#     """This request is not supported."""

#     ValidationError = "validation_error"
#     """The request body does not match the schema for the expected parameters."""

#     ConflictError = "conflict_error"
#     """The transaction could not be completed, potentially due to a data collision.
#     Make sure the parameters are up to date and try again."""

#     InternalServerError = "internal_server_error"
#     """An unexpected error occurred. Reach out to Notion support."""

#     ServiceUnavailable = "service_unavailable"
#     """Notion is unavailable. Try again later.
#     This can occur when the time to respond to a request takes longer than 60 seconds,
#     the maximum request timeout."""


# ("에러 코드", "응답 코드", "응답명", "설명")
# ("OPENAPI00001", 500, "Internal Server Error", "서버 내부 오류")
# ("OPENAPI00002", 403, "Forbidden", "권한이 없는 경우")
# ("OPENAPI00003", 400, "Bad Request", "유효하지 않은 식별자")
# ("OPENAPI00004", 400, "Bad Request", "파라미터 누락 또는 유효하지 않음")
# ("OPENAPI00005", 400, "Bad Request", "유효하지 않은 API KEY")
# ("OPENAPI00006", 400, "Bad Request", "유효하지 않은 게임 또는 API PATH")
# ("OPENAPI00007", 429, "Too Many Requests", "API 호출량 초과")
# ("OPENAPI00009", 400, "Bad Request", "데이터 준비 중")


# code = "OPENAPI00001"

# # code 변수의 값으로 APIErrorCode 열거형 멤버 생성
# # error_code = APIErrorCode(code)

# # # 생성된 열거형 멤버 출력
# # print(error_code)

# # print(APIErrorCode._name_)
# print(APIErrorCode._member_names_)
# print(APIErrorCode._value2member_map_)
# print(APIErrorCode._member_map_)
# print(APIErrorCode.from_code(code))
