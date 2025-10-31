import enum
###################### 상태 등 이름 #############################
class Body(enum.Enum):
    '''부위별 데미지, 상태 
    #### 몸부위'''
    HEAD = "머리"
    BODY = "몸"
    LEFT_ARM = "왼팔"
    RIGHT_ARM = "오른팔"
    LEFT_LEG = "왼다리"
    RIGHT_LEG = "오른다리"

class BodyStatus(enum.Enum):
    '''#### 부위별 상태'''
    NORMAL = "정상" # 체력 특정 수준 이상
    INJURED = "부상" # 체력 특정 수준 이하
    BLEEDING = "출혈" # 칼날에 지속피해 -> 붕대로 치료
    DISABLED = "불구" # 체력 0, 기능 상실 ex) 다리: 회피 감소, 팔: 무기를 드는 손에 따라서 다름
    POiSONED = "중독" # 독 -> 해독제

class Things(enum.Enum):
    '''#### 아이템 종류'''
    WEAPON = "무기"
    ARMOR = "방어구"
    POTION = "물약"
    MISC = "잡동사니"

class PotionType(enum.Enum):
    '''#### 물약 종류'''
    HEALING = "회복약"
    MANA = "마나약"
    ANTIDOTE = "해독제"

class WeaponType(enum.Enum):
    '''#### 무기 종류'''
    SWORD = "검"
    BOW = "활"
    HAMMER = "망치"

class ArmorType(enum.Enum):
    '''#### 방어구 종류'''
    HELM = "투구"
    CHESTPLATE = "흉갑"
    LEGGINGS = "다리보호구"
    BOOTS = "장화"

class Rarity(enum.Enum):
    '''#### 아이템 희귀도'''
    COMMON = "일반"
    UNCOMMON = "비범"
    RARE = "희귀"
    EPIC = "영웅"
    LEGENDARY = "전설"

class DamageType(enum.Enum): # TODO: 데미지 타입 추가
    '''#### 데미지 타입'''
    SLASHING = "베기"
    PIERCING = "찌르기"
    BLUDGEONING = "타격"
###################### 상태 등 이름 #############################