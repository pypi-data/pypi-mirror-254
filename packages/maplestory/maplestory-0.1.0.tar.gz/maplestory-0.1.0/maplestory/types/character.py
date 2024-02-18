from typing import Annotated, Literal

from annotated_types import Ge, Le

AbilityNumber = Annotated[int, Ge(1), Le(3)]
CharacterLevel = Annotated[int, Ge(1), Le(300)]
CharacterClassLevel = Literal["0", "1", "2", "3", "4", "5", "6"]
CharacterGender = Literal["남", "여"]
AndroidGender = CharacterGender | None
ItemGender = CharacterGender | None
ItemOptionValue = Annotated[int, Ge(-100)]  # 혼돈의 주문서로 음수 가능
ItemSlotName = Literal[
    "귀고리",
    "기계 심장",
    "눈장식",
    "망토",
    "모자",
    "무기",
    "반지1",
    "반지2",
    "반지3",
    "반지4",
    "뱃지",
    "벨트",
    "보조무기",
    "상의",
    "신발",
    "어깨장식",
    "얼굴장식",
    "엠블렘",
    "장갑",
    "펜던트",
    "펜던트2",
    "포켓 아이템",
    "하의",
    "훈장",
]
LabelName = Literal["스페셜라벨", "레드라벨", "블랙라벨", "마스터라벨"] | None
LinkSkillLevel = Annotated[int, Ge(1), Le(10)]
PetSkill = Literal[
    "버프 스킬 자동 사용",
    "아이템 줍기",
    "이동반경 확대",
    "자동 줍기",
    "펫 자이언트 스킬",
    "펫 훈련 스킬",
    "HP 물약충전",
    "MP 물약충전",
]
HyperStatLevel = Annotated[int, Ge(0), Le(15)]
HyperStatType = Literal[
    "STR",
    "DEX",
    "INT",
    "LUK",
    "HP",
    "MP",
    "DF/TF/PP",
    "크리티컬 확률",
    "크리티컬 데미지",
    "방어율 무시",
    "데미지",
    "보스 몬스터 공격 시 데미지 증가",
    "상태 이상 내성",
    "공격력/마력",
    "획득 경험치",
    "아케인포스",
    "일반 몬스터 공격 시 데미지 증가",
]
VCoreType = Literal["강화코어", "스킬코어", "특수코어"] | None
VCoreLevel = Annotated[int, Ge(1), Le(30)]