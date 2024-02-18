import httpx
from httpx import Request, Response
from tenacity import retry, wait_random_exponential

from maplestory.config import Config
from maplestory.error import APIError, ErrorMessage


# @retry(retry=retry_if_exception_type(IOError))
# @retry(wait=wait_random_exponential(multiplier=1, max=8))
def fetch(url_path: str, query_params: dict | None = None) -> dict:
    """
    Fetches data from the API.

    Args:
        url_path : The API path.
        query_params (dict): The query parameters.

    Returns:
        dict: The response data.

    Raises:
        APIError: If an API error occurs.
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
