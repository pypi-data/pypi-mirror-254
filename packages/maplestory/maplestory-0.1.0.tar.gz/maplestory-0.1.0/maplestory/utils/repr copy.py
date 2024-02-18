from pydantic import BaseModel

# from pydantic.typing import ReprArgs


class HideNoneRepresentation:
    def __repr_args__(self: BaseModel):  # -> "ReprArgs":
        return [
            (key, value) for key, value in self.__dict__.items() if value is not None
        ]
        # for k, v in self.__dict__.items():
        #     if v is not None:
        #         yield k, v
