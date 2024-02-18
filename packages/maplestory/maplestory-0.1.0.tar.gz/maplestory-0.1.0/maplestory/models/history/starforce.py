from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, field_validator

from maplestory.models.types import PageCursor


# FIXME: plus_value가 현재 str인데, int/float으로 변경하기. 현재 'null'밖에 보지 못함.
# TODO: success_rate, event_range가 리스트인 경우 별도로 분리하기
class StarforceHistoryEvent(BaseModel):
    """진행 중인 스타포스 강화 이벤트 정보

    Attributes:
        success_rate: 이벤트 성공 확률
        cost_discount_rate: 이벤트 비용 할인율
        plus_value: 이벤트 강화 수치 가중값
        starforce_event_range: 이벤트 적용 강화 시도 가능한 n성 범위

    Examples:
        {
            "success_rate": "null",             -> None
            "cost_discount_rate": "30",         -> 0.3
            "plus_value": "null",               -> None
            "starforce_event_range": "0~24"
        },
        {
            "success_rate": "100,100,100",
            "cost_discount_rate": "null",       -> None
            "plus_value": "null",               -> None
            "starforce_event_range": "5,10,15"
        }
    """

    success_rate: str | None
    cost_discount_rate: float | None
    plus_value: str | None
    starforce_event_range: str

    @field_validator("success_rate", mode="before")
    @classmethod
    def change_success_rate(cls, v: Any) -> str | None:
        return None if v == "null" else v

    @field_validator("cost_discount_rate", mode="before")
    @classmethod
    def change_cost_discount_rate(cls, v: Any) -> float | None:
        return None if v == "null" else int(v) / 100

    @field_validator("plus_value", mode="before")
    @classmethod
    def change_plus_value(cls, v: Any) -> Any:
        return None if v == "null" else v


class StarforceHistoryInfo(BaseModel):
    """스타포스 히스토리 정보

    Attributes:
        id: 스타포스 히스토리 식별자
        item_upgrade_result: 강화 시도 결과
        before_starforce_count: 강화 시도 전 스타포스 수치
        after_starforce_count: 강화 시도 후 스타포스 수치
        starcatch_result: 스타 캐치
        superior_item_flag: 슈페리얼 장비
        destroy_defense: 파괴 방지
        chance_time: 찬스 타임
        event_field_flag: 파괴 방지 필드 이벤트
        upgrade_item: 사용 주문서 명
        protect_shield: 프로텍트 실드
        bonus_stat_upgrade: 보너스 스탯 부여 아이템 여부
        character_name: 캐릭터 명
        world_name: 월드 명
        target_item: 대상 장비 아이템 명
        date_create: 강화 일시 (KST) example: 2023-12-27T17:28+09:00
        starforce_event_list: 진행 중인 스타포스 강화 이벤트 정보
    """

    id: str  # Len(96, 96)
    item_upgrade_result: str
    before_starforce_count: int
    after_starforce_count: int
    starcatch_result: str
    superior_item_flag: str
    destroy_defense: str = Field(alias="destroy_defence")
    chance_time: str
    event_field_flag: str
    upgrade_item: str
    protect_shield: str
    bonus_stat_upgrade: str
    character_name: str
    world_name: str
    target_item: str
    date_create: datetime
    starforce_event_list: list[StarforceHistoryEvent]


class StarforceHistory(BaseModel):
    """스타포스 히스토리

    Attributes:
        count: 결과 건 수
        next_cursor: 페이징 처리를 위한 cursor
        starforce_history: 스타포스 히스토리
    """

    count: int
    next_cursor: PageCursor | None
    starforce_history: list[StarforceHistoryInfo]
