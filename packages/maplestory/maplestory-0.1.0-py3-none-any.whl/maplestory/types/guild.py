from typing import Annotated

from annotated_types import Ge, Le

GuildLevel = Annotated[int, Ge(1), Le(30)]
