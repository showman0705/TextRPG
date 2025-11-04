
class Character():
    '''initial_defense = 5, initial_mana = 30
    나중에 방어력, 마나 등 추가'''
    def __init__(self, name, level, basic_damage, basic_defense, hp, inventory = None ):
        self.name = name
        self.level = level
        self.basic_damage = basic_damage
        self.basic_defense = basic_defense
        self.hp = hp  
        self.inventory = inventory if inventory is not None else []


    def attack(self, target):
        '''캐릭터가 다른 캐릭터를 공격하는 메서드, 레벨이 높아질수록 데미지 증가, 나중에 크리티컬, 부위별 데미지, 상대 방어, 레벨 별 데미지로 추가
        #### 필요 변수: 피격받는 캐릭터 ####'''
        # total_defense = target.basic_defense + (target.level -1) * 1 # TODO: 나중에 방어력 계산
        total_damage = self.basic_damage + (self.level - 1) 
        # * 2 - total_defense# TODO: 나중에 데미지 계산식 개선
        target.hp -= total_damage
        return total_damage
    
    def show_status(self):
        status = f"Name: {self.name}\nLevel: {self.level}\n"
        return status