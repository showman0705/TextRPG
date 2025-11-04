from entity.char.character import Character

class Player(Character): # TODO: 나중에 body클래스로 부위별 상태 추가
    '''level_up, get_item, use_item, show_inventory '''
    def __init__(self, name, level, basic_damage, basic_defense, max_hp, hp, exp, gold, inventory = None, sin_list = None):
        super().__init__(name, level, basic_damage, basic_defense, hp, inventory)
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

    def get_item(self, item): 
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