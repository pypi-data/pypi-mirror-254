"""이 모듈은 네트워크 요청을 처리하는 함수를 제공합니다. 

- `fetch` 함수는 주어진 URL 경로와 쿼리 파라미터를 사용하여 GET 요청을 보내고, 응답을 JSON 형태로 반환합니다. 
    만약 응답에 에러가 포함되어 있으면, `APIError`를 발생시킵니다.
"""

import httpx
from httpx import Response
from tenacity import retry, retry_if_exception_message, wait_exponential

from maplestory.config import Config
from maplestory.error import APIError, ErrorMessage


@retry(
    retry=retry_if_exception_message(match="^.*Please try again later.*$"),
    wait=wait_exponential(multiplier=1, min=4, max=10),
)
def fetch(url_path: str, query_params: dict | None = None) -> dict:
    """
    주어진 URL 경로와 쿼리 파라미터를 사용하여 GET 요청을 보내고, 응답을 JSON 형태로 반환합니다. 만약 응답에 에러가 포함되어 있으면, `APIError`를 발생시킵니다.

    Args:
        url_path (str): 요청을 보낼 URL 경로입니다.
        query_params (dict | None, optional): 요청에 포함할 쿼리 파라미터입니다. 기본값은 None입니다.

    Raises:
        APIError: 응답에 에러가 포함되어 있을 경우 발생합니다.

    Returns:
        dict: 응답을 JSON 형태로 변환한 결과입니다.
    """

    config = Config()
    resp: Response = httpx.get(
        f"{config.url}{url_path}",
        params=query_params,
        headers={
            "x-nxopen-api-key": config.key,
            "Accept": "application/json",
        },
        timeout=config.timeout,
    )

    data = resp.json()
    if error := data.get("error"):
        em = ErrorMessage.model_validate(error)
        raise APIError(em, resp)

    return data
