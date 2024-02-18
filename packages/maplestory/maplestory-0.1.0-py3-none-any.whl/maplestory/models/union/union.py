from datetime import datetime

from pydantic import BaseModel


class Union(BaseModel):
    """유니온 정보

    Attributes:
        date: 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        union_level: 유니온 레벨
        union_grade: 유니온 등급

    Examples:
        >>> Union(date="2024-01-04T00:00+09:00", union_level=9254, union_grade="그랜드 마스터 유니온 3")
        Union(date=datetime.datetime(2024, 1, 4, 0, 0, tzinfo=TzInfo(+09:00)),
              union_level=9254,
              union_grade='그랜드 마스터 유니온 3')
    """

    date: datetime
    union_level: int
    union_grade: str

    @property
    def date_string(self) -> str:
        return self.date.isoformat()
