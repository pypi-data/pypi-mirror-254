"""확률 정보 조회 API를 제공하는 모듈입니다.

Note:
    - 큐브, 스타포스, 잠재능력 각각 조회 가능한 날짜가 다릅니다.
"""

from datetime import datetime

import maplestory.utils.date as dates
import maplestory.utils.kst as kst
from maplestory.enum import QueryableDate
from maplestory.models.history import Account, CubeHistory, StarforceHistory
from maplestory.models.history.potential import PotentialHistory
from maplestory.models.types import PageCursor
from maplestory.utils.network import fetch


def get_account_id() -> str:
    """계정 식별자(ouid) 조회

    Returns:
        str: 계정 식별자(ouid)
    """

    path = "/maplestory/v1/ouid"
    response = fetch(path)

    return Account.model_validate(response).ouid


def validate_date_and_cursor(
    date: datetime | None = None,
    cursor: PageCursor | None = None,
) -> None:
    """date와 cursor의 유효성을 확인하는 함수입니다.

    Args:
        date (datetime): 날짜 정보.
        cursor (str): 페이지 커서 정보.

    Raises:
        ValueError: date와 cursor가 동시에 제공되는 경우 또는 둘 다 제공되지 않는 경우 발생합니다.
    """

    if date is not None and cursor is not None:
        raise ValueError("date and cursor cannot be used together")

    if date is None and cursor is None:
        raise ValueError("date or cursor must be provided")


def validate_count(count: int) -> None:
    """count의 유효성을 확인하는 함수입니다.

    Args:
        count (int): 한번에 가져오려는 결과의 갯수.

    Raises:
        ValueError: count가 10보다 작거나 1000보다 클 경우 발생합니다.
    """

    if count < 10 or count > 1000:
        raise ValueError("count must be between 10 and 1000")


def get_starforce_history(
    result_count: int = 1000,
    date: datetime | None = kst.yesterday(),
    page_cursor: PageCursor | None = None,
) -> StarforceHistory:
    """스타포스 강화 결과를 조회합니다.

    Args:
        result_count (int): 한번에 가져오려는 결과의 갯수. (최소 10, 최대 1000)
        date (datetime, optional): 조회 기준일(KST). (cursor가 없는 경우 필수이며 cursor와 함께 사용 불가)
        page_cursor (str, optional): 페이징 처리를 위한 cursor. (date가 없는 경우 필수이며 date와 함께 사용 불가)

    Notes:
        - 스타포스 확률 정보는 최대 5분 후 확인 가능합니다.
        - 2023년 12월 27일 데이터부터 조회할 수 있습니다.
    """

    validate_count(result_count)

    if page_cursor is not None:
        date = None

    validate_date_and_cursor(date, page_cursor)

    if isinstance(date, datetime):
        dates.is_valid(date, QueryableDate.스타포스)

    path = "/maplestory/v1/history/starforce"
    query = {
        "count": result_count,
        "date": dates.to_string(date),
        "cursor": page_cursor,
    }
    response = fetch(path, query)

    return StarforceHistory.model_validate(response)


def get_cube_usage_history(
    result_count: int = 1000,
    date: datetime = kst.yesterday(),
    page_cursor: PageCursor | None = None,
) -> CubeHistory:
    """큐브 사용 결과를 조회합니다.

    Args:
        result_count (int): 한번에 가져오려는 결과의 갯수.
        date (datetime): 조회 기준일(KST).
        page_cursor (str) : 페이징 처리를 위한 cursor.

    Returns:
        CubeHistory: 큐브 사용 결과.

    Notes:
        - 데이터는 매일 오전 4시, 전일 데이터가 갱신됩니다.
        - 2022년 11월 25일 데이터부터 조회할 수 있습니다.
    """

    validate_count(result_count)

    if page_cursor is not None:
        date = None

    validate_date_and_cursor(date, page_cursor)

    if isinstance(date, datetime):
        dates.is_valid(date, QueryableDate.큐브)

    path = "/maplestory/v1/history/cube"
    query = {
        "count": result_count,
        "date": dates.to_string(date),
        "cursor": page_cursor,
    }
    response = fetch(path, query)

    return CubeHistory.model_validate(response)


def get_potential_history(
    result_count: int = 1000,
    date: datetime = kst.yesterday(),
    page_cursor: PageCursor | None = None,
) -> PotentialHistory:
    """잠재능력 재설정 이용 결과를 조회합니다.

    Attributes:
        count: 한번에 가져오려는 결과의 갯수(최소 10, 최대 1000)
        date: 조회 기준일 (KST) (cursor가 없는 경우 필수이며 cursor와 함께 사용 불가)
        cursor: 페이징 처리를 위한 cursor (date가 없는 경우 필수이며 date와 함께 사용 불가)

    Notes:
        - 데이터는 매일 오전 4시, 전일 데이터가 갱신됩니다.
        - 2024년 1월 25일 데이터부터 조회할 수 있습니다.
    """

    validate_count(result_count)

    if page_cursor is not None:
        date = None

    validate_date_and_cursor(date, page_cursor)

    if isinstance(date, datetime):
        dates.is_valid(date, QueryableDate.잠재능력)

    path = "/maplestory/v1/history/potential"
    query = {
        "count": result_count,
        "date": dates.to_string(date),
        "cursor": page_cursor,
    }
    response = fetch(path, query)

    return PotentialHistory.model_validate(response)
