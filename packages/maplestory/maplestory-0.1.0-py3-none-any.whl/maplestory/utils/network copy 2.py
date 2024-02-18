import httpx
from httpx import Response
from tenacity import (
    retry,
    retry_if_exception_message,
    retry_if_exception_type,
    wait_exponential,
)

from maplestory.config import Config
from maplestory.error import APIError, ErrorMessage


# retry=retry_if_exception_type(APIError),
# retry=(retry_if_exception_type(APIError) & retry_if_exception_message(match="^.*Please try again later.*$"))
@retry(
    retry=retry_if_exception_message(match="^.*Please try again later.*$"),
    wait=wait_exponential(multiplier=1, min=4, max=10),
)
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
    # try:
    #     ErrorResponse.model_validate(data)
    # except ValidationError as err:

    if error := data.get("error"):
        em = ErrorMessage.model_validate(error)
        err = APIError(em, resp)
        print("--------------------------------")
        print(repr(err))
        print(repr(err.code))
        print(repr(err.status))
        print(f"request: {resp.request}")
        print(f"request.headers: {resp.request.headers}")
        print("--------------------------------")
        raise err

    return data


# Please input valid parameter
# OPENAPI00004
# 400
# Headers([('content-type', 'application/json;charset=UTF-8'), ('transfer-encoding', 'chunked'), ('connection', 'keep-alive'), ('date', 'Fri, 26 Jan 2024 07:12:40 GMT'), ('vary', 'Origin,Access-Control-Request-Method,Access-Control-Request-Headers'), ('x-content-type-options', 'nosniff'), ('x-xss-protection', '0'), ('cache-control', 'no-cache, no-store, max-age=0, must-revalidate'), ('pragma', 'no-cache'), ('expires', '0'), ('strict-transport-security', 'max-age=31536000 ; includeSubDomains'), ('referrer-policy', 'no-referrer'), ('x-envoy-upstream-service-time', '31'), ('inface-wasm-filter', '1.5.5'), ('server', 'inface'), ('x-request-id', 'ZAdjsYx19504vXRwAlmyRFManOKFp2JBznT-Gz9pBRzR3YS_Dn9KDQ=='), ('x-cache', 'Error from cloudfront'), ('via', '1.1 bca5030f468e569e9304a18600bffc26.cloudfront.net (CloudFront)'), ('x-amz-cf-pop', 'ICN54-C2'), ('x-amz-cf-id', 'ZAdjsYx19504vXRwAlmyRFManOKFp2JBznT-Gz9pBRzR3YS_Dn9KDQ=='), ('vary', 'Origin')])
# {"error":{"name":"OPENAPI00004","message":"Please input valid parameter"}}
# Please try again later (OPENAPI00007)
