from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, model_validator

import maplestory.utils.kst as kst
from maplestory.models.history import Account, CubeHistory, StarforceHistory
from maplestory.utils.network import fetch


def get_account_id() -> str:
    """계정 식별자(ouid) 조회

    Returns:
        str: _description_
    """

    path = "/maplestory/v1/ouid"
    response = fetch(path)

    return Account.model_validate(response).ouid


def validate_date_and_cursor(
    date: Optional[datetime] = None, cursor: Optional[str] = None
) -> None:
    """
    date와 cursor의 유효성을 확인하는 함수입니다.

    Args:
        date (Optional[datetime]): 날짜 정보. 기본값은 None입니다.
        cursor (Optional[str]): 커서 정보. 기본값은 None입니다.

    Raises:
        ValueError: date와 cursor가 동시에 제공되는 경우 또는 둘 다 제공되지 않는 경우 발생합니다.
    """

    if date is not None and cursor is not None:
        raise ValueError("date and cursor cannot be used together")

    if date is None and cursor is None:
        raise ValueError("date or cursor must be provided")


class CubeHistory:
    # history: list[CubeHistory]

    def fetch(self, date: datetime = kst.yesterday()):
        all_history = []
        history = get_cube_usage_history(reference_data=date)
        all_history.extend(history.cube_history)
        while cursor := history.next_cursor:
            history = get_cube_usage_history(cursor=cursor)
            all_history.extend(history.cube_history)

        return all_history

    def fetch_from_date(self, from_date: datetime):
        all_history = []
        the_date = from_date
        while the_date < kst.kst_today():
            history = get_cube_usage_history(reference_data=the_date)
            all_history.extend(history.cube_history)
            the_date += datetime.timedelta(days=1)

        return all_history

    def fetch_from_to(self, from_date: datetime, to_date: datetime):
        all_history = []
        the_date = from_date
        while the_date <= to_date:
            history = get_cube_usage_history(reference_data=the_date)
            all_history.extend(history.cube_history)
            the_date += datetime.timedelta(days=1)

        return all_history


def get_cube_usage_history(
    result_count: int = 1000,
    date: datetime = kst.yesterday(),
    page_cursor: str | None = None,
) -> CubeHistory:
    """
    큐브 사용 결과를 조회합니다.
    Fetches the usage result of the cube.

    Args:
        result_count : 한번에 가져오려는 결과의 갯수. The number of results to fetch at once.
        date : 조회 기준일(KST). Reference date for the query (KST).
        page_cursor : 페이징 처리를 위한 cursor. Cursor for paging.

    Returns:
        CubeHistory: 큐브 사용 결과. The usage result of the cube.
    """

    validate_date_and_cursor(date, page_cursor)

    path = "/maplestory/v1/history/cube"
    query = {
        "count": result_count,
        "date": kst.validate(date),
        "cursor": page_cursor,
    }
    response = fetch(path, query)

    return CubeHistory.model_validate(response)


# TODO: date랑 page_cursor가 같이 들어오면 에러를 발생시키도록
class StarforceHistoryParameter(BaseModel):
    result_count: int = 1000
    date: datetime | None = None  # = date.kst_yesterday()
    page_cursor: str | None = None
    # 아니면 page_cursor가 None이 아니면 date를 None으로 변경하던가

    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: Any) -> Any:
        if data.get("date") and data.get("page_cursor"):
            raise ValueError("page_cursor cannot be used with date")
        return data


def get_starforce_history(
    result_count: int = 1000,
    date: datetime | None = kst.yesterday(),
    page_cursor: str | None = None,
) -> StarforceHistory:
    """
    스타포스 강화 결과를 조회합니다.
    Fetches the starforce enhancement results.

    Args:
        result_count (int): 한번에 가져오려는 결과의 갯수(최소 10, 최대 1000)
                            The number of results to fetch at once (minimum 10, maximum 1000)
        date (datetime, optional): 조회 기준일(KST) (cursor가 없는 경우 필수이며 cursor와 함께 사용 불가)
                                             Query base date (KST) (required if cursor is not present and cannot be used with cursor)
        page_cursor (str, optional): 페이징 처리를 위한 cursor (date가 없는 경우 필수이며 date와 함께 사용 불가)
                                     Cursor for pagination (required if date is not present and cannot be used with date)
    """

    if result_count < 10 or result_count > 1000:
        raise ValueError("result_count must be between 10 and 1000")

    validate_date_and_cursor(date, page_cursor)

    path = "/maplestory/v1/history/starforce"
    query = {
        "count": result_count,
        "date": kst.validate(date),
        "cursor": page_cursor,
    }
    response = fetch(path, query)
    return StarforceHistory.model_validate(response)
