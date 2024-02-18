from enum import Enum, Flag, auto

from kst.datetime import timedelta

import maplestory.utils.kst as kst


class BaseEnum(Enum):
    @classmethod
    def members(cls):
        return list(cls.__members__)

    @classmethod
    def keys(cls):
        return list(cls.__members__)

    @classmethod
    def values(cls):
        return [c.value for c in cls]

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class WorldType(BaseEnum):
    일반 = 0  # normal
    리부트 = 1  # reboot
    Normal = 0
    Reboot = 1


class GuildRankType(BaseEnum):
    주간명성치 = 0  # Weekly Fame
    플레그레이스 = 1  # Flag Race
    지하수로 = 2  # Underground Waterway


class MinimumDateType(BaseEnum):
    랭킹 = kst.datetime(2023, 12, 22)
    유니온 = 1  # Union
    길드 = 2  # Guild


class Planet(Enum):
    MERCURY = (3.303e23, 2.4397e6)
    VENUS = (4.869e24, 6.0518e6)
    EARTH = (5.976e24, 6.37814e6)
    MARS = (6.421e23, 3.3972e6)
    JUPITER = (1.9e27, 7.1492e7)
    SATURN = (5.688e26, 6.0268e7)
    URANUS = (8.686e25, 2.5559e7)
    NEPTUNE = (1.024e26, 2.4746e7)

    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300e-11
        return G * self.mass / (self.radius * self.radius)


# >>> Planet.EARTH.value
# (5.976e+24, 6378140.0)
# >>> Planet.EARTH.surface_gravity
# 9.802652743337129


class Period(timedelta, Enum):
    "different lengths of time"
    _ignore_ = "Period i"
    Period = vars()
    for i in range(367):
        Period["day_%d" % i] = i


# >>> list(Period)[:2]
# [<Period.day_0: kst.datetime.timedelta(0)>, <Period.day_1: kst.datetime.timedelta(days=1)>]
# >>> list(Period)[-2:]
# [<Period.day_365: kst.datetime.timedelta(days=365)>, <Period.day_366: kst.datetime.timedelta(days=366)>]


class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


# >>> purple = Color.RED | Color.BLUE
# >>> white = Color.RED | Color.GREEN | Color.BLUE
# >>> Color.GREEN in purple
# False
# >>> Color.GREEN in white
# True
# >>> purple in white
# True
# >>> white in purple
# False


if __name__ == "__main__":
    from devtools import debug

    val = 1
    w = WorldType(val)
    debug(w)
    w = WorldType.일반
    debug(w)
    w = WorldType.Normal
    debug(w)
    query = {"world_type": w, "world_name": "테스트"}
    debug(query)

    debug(WorldType._member_names_)
    debug(WorldType._member_map_)
    debug(WorldType._value2member_map_)
    debug(WorldType.list())
    debug(WorldType.values())
    debug(WorldType.members())
    # debug(WorldType.__members__)
    # debug(list(WorldType.__members__))
