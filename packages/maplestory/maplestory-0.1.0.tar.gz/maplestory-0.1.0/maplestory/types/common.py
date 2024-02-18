from datetime import datetime
from typing import Annotated, Literal

from annotated_types import Ge, Le, Len

ExpireDate = datetime | None
Grade = Literal["레전드리", "유니크", "에픽", "레어"]
PageCursor = Annotated[str, Len(64, 64)]
PresetNumber = Annotated[int, Ge(1), Le(3)] | None
WorldName = Literal[
    "스카니아",
    "베라",
    "루나",
    "제니스",
    "크로아",
    "유니온",
    "엘리시움",
    "이노시스",
    "레드",
    "오로라",
    "아케인",
    "노바",
    "리부트",
    "리부트2",
    "버닝",
    "버닝2",
    "버닝3",
]
