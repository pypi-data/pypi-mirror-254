"""이 모듈은 Pydantic의 BaseModel을 상속받은 클래스에서 특정 조건을 만족하는 필드를 `__repr__` 메소드의 결과에서 제외하는 기능을 제공합니다. 

- `HideNoneRepresentation` 믹스인 클래스는 `None` 값을 가진 필드를 제외합니다.
- `HideZeroStatRepresentation` 믹스인 클래스는 "STR", "INT", "DEX", "LUK" 키에 대응하는 값이 0인 필드를 제외합니다.
"""

from pydantic import BaseModel


class HideNoneRepresentation:
    """`None` 값을 가진 필드를 `__repr__` 메서드의 결과에서 제외하는 믹스인 클래스입니다."""

    def __repr_args__(self: BaseModel):
        """BaseModel의 `__repr__` 메서드에서 사용하는 필드와 값의 리스트를 반환합니다.

        이 메서드는 `None` 값을 가진 필드를 제외합니다.

        Returns:
            list: 필드 이름과 값의 튜플을 원소로 가지는 리스트입니다. `None` 값을 가진 필드는 제외됩니다.
        """
        return [
            (key, value) for key, value in self.__dict__.items() if value is not None
        ]


class HideZeroStatRepresentation:
    """스탯 값이 0인 경우를 `__repr__` 메서드의 결과에서 제외하는 믹스인 클래스입니다."""

    STAT_KEYS = ["STR", "INT", "DEX", "LUK", "HP"]

    def __repr_args__(self: BaseModel):
        """BaseModel의 `__repr__` 메소드에서 사용하는 필드와 값의 리스트를 반환하는데, 스탯 값이 0인 필드를 제외합니다.

        Returns:
            list: 스탯 값이 0인 필드가 제외된 필드 이름과 값의 튜플을 원소로 가지는 리스트입니다.
        """

        return [
            (key, value)
            for key, value in self.__dict__.items()
            if key not in self.STAT_KEYS or value != 0
        ]
