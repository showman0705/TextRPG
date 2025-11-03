import material

################ 아이템 #################
class Item():  
    def __init__(self, name: str, thing_type: material.Things, rarity: material.Rarity):
        self.name = name
        self.thing_type = thing_type
        self.rarity = rarity


############### 캐릭터 ###############
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
############### 캐릭터 ###############


############### 플레이어 ###############
class Player(Character): # TODO: 나중에 body클래스로 부위별 상태 추가
    '''level_up, get_item, use_item, show_inventory '''
    def __init__(self, name, level = 1, basic_damage = 10, basic_defense = 3, max_hp = 100, hp = 100, inventory = None, sin_list:list = None, exp = 0, gold = 100):
        super().__init__(name, level, basic_damage, basic_defense, hp, inventory=None)
        self.exp = exp
        self.max_hp = max_hp
        self.gold = gold
        self.sin_list = sin_list if sin_list is not None else []

    def level_up(self): 
        self.level += 1
        self.basic_damage += 5
        self.max_hp += 20
        level_up_message = f"{self.name} 레벨업, 현재레벨: {self.level}"
        return level_up_message

    def get_item(self, item: Item): 
            self.inventory.extend(item) # 아이템은 리스트로 표현 -> 여러가지 아이템을 한번에 얻는 것도 가능


    def use_item(self, item): # TODO: 아이템 효과 추가
        if item in self.inventory:
            self.inventory.remove(item)

    def show_status(self): 
        status = super().show_status()
        status += f"HP: {self.hp}/{self.max_hp}\nEXP: {self.exp}/{100 * self.level}\nGold: {self.gold}\n"
        # 죄악 추가
        return status
    
    def show_inventory(self): # TODO: 아이템 상세정보, 여러개면 갯수 나타내서 간략화, 아이템 사용 등 추가
        inventory_info = "inventory:\n"
        for item in list(dict.fromkeys(self.inventory)):
            inventory_info += f"- {item.name} ({item.thing_type.value}, {item.rarity.value}) x {self.inventory.count(item)}\n"
        return inventory_info 
############## 플레이어 ###############

################ 적 #################
class Enemy(Character): # TODO: 인벤토리로 아이템을 여러가지 가지고 있는 적도 생성 가능하게 만들기
    '''defeat 메서드에서 drop_item, give_exp 호출 -> 플레이어에게 줌'''
    def __init__(self, name, level, basic_damage, basic_defense, hp, inventory = None):
        super().__init__(name, level, basic_damage, basic_defense, hp, inventory)

    def drop_item(self, player: Player, enemy): # TODO: 아이템 다양화 후에 몬스터에 따라서 다르게 설정 -> 클래스로
        item = self.inventory
        player.get_item(item)


    def give_exp(self, player: Player): # TODO: 나중에 경험치 개선 -> 몬스터 레벨, 플레이어 레벨 차이 등
        exp_gain = self.level * 10
        player.exp += exp_gain
        if player.exp >= player.level * 100:
            player.level_up()

    def defeat(self, player: Player, enemy):
        self.give_exp(player)
        self.drop_item(player, enemy)    
############### 적 #################

# ############### 질투(가시 데미지) 구현 가능 확인 ################
# class Invidia_3(Enemy):
#     def __init__(self, name, level, basic_damage, basic_defense, hp, sin: material.Sin.Invidia):
#         super().__init__(name, level, basic_damage, basic_defense, hp)
#         self.sin = sin
#     def give_sin_Invidia(self, target: Character):
#         if target.attack(self):
#             target.hp -= target.attack() *(10/100)
#             print("질투")
# ############## 질투(가시 데미지) 구현 가능 확인 ################





    # def show_info(self):
    #     info = f"Item Name: {self.name}\nType: {self.thing_type.value}\nRarity: {self.rarity.value}\n"


class Potion(Item):
    def __init__(self, name, thing_type: material.Things.POTION, rarity: material.Rarity, potion_type: material.PotionType):
        super().__init__(name, thing_type, rarity)
        self.potion_type =potion_type
################## 아이템 #################


######## 회복 물약 #################
class HealingPotion(Potion):
    def __init__(self, name, heal_amount, thing_type: material.Things.POTION, potion_type: material.PotionType.HEALING, rarity: material.Rarity):
        super().__init__(name, thing_type, rarity, potion_type)
        self.heal_amount = heal_amount

    def use(self, user: Player):
        user.hp += self.heal_amount
        user.use_item(self)
######## 회복 물약 #################