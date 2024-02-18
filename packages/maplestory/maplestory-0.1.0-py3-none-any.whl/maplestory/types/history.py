from typing import Literal

from maplestory.types.common import Grade

CubePotenialGrade = Literal["레전드리", "유니크", "에픽", "레어", "노멀"]
PotentialGrade = Grade | None
PotentialOption = str | None
