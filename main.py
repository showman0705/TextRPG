import curses
from curses import wrapper
import material
import time
import random




# class DamageCalculator():
#     ''', damage_type: DamageType, weapon_damage_bonus,  body_pard: Body, body_status: BodyStatus):'''
#     # 나중에 데미지 타입, 무기 데미지 보너스, 부위, 상태 등 추가
#     # 
#     def __init__(self, initial_damage, critical_chance, critical_multiplier):
#         self.initial_damage = initial_damage
#         self.critical_chance = critical_chance
#         self.critical_multiplier = critical_multiplier
    
#     def calculate_damage(self, target: 'Character'):
#         Total_damage = self.initial_damage
#         if random.randint(1, 100) <= self.critical_chance:
#             Total_damage *= self.critical_multiplier
#         return Total_damage
        
#         # 나중에 부위별 데미지, 상태별 데미지 보너스 등 추가
        

class Item():
    def __init__(self, name, thing_type: material.Things, raity: material.Rarity):
        self.name = name
        self.thing_type = thing_type
        self.raity = raity

    def show_info(self):
        info = f"Item Name: {self.name}\nType: {self.thing_type.value}\nRarity: {self.raity.value}\n"

# class Weapon(Item):
#     def __init__(self, name, thing_type)

class Character():
    '''initial_defense = 5, initial_mana = 30
    나중에 방어력, 마나 등 추가'''
    def __init__(self, name, level=1, basic_damage = 10, hp = 100):
        self.name = name
        self.level = level
        self.basic_damage = basic_damage
        self.hp = hp  

    def attack(self, target):
        '''캐릭터가 다른 캐릭터를 공격하는 메서드, 레벨이 높아질수록 데미지 증가, 나중에 크리티컬, 부위별 데미지, 상대 방어, 레벨 별 데미지로 추가
        #### 필요 변수: 피격받는 캐릭터 ####'''
        total_damage = self.basic_damage + (self.level - 1) * 2 # TODO: 나중에 데미지 계산식 개선
        target.hp -= total_damage
    
    def show_status(self):
        status = f"Name: {self.name}\nLevel: {self.level}\n"
        return status
    




class Player(Character): # TODO: 나중에 body클래스로 부위별 상태 추가
    '''level_up, get_item, use_item, show_inventory '''
    def __init__(self, name, level = 1, exp = 0, gold = 0, basic_damage = 10, hp = 100, inventory = None):
        super().__init__(name, level, basic_damage, hp)
        self.exp = exp
        self.gold = gold
        self.inventory = inventory if inventory is not None else []

    def level_up(self): 
        self.level += 1
        self.basic_damage += 5
        self.hp += 20
        print(f"{self.name} 레벨업, 현재레벨: {self.level}")
        self.hp = 100 + (self.level - 1) * 20

    def get_item(self, item):
        self.inventory.append(item)

    def use_item(self, item): # TODO: 아이템 효과 추가
        if item in self.inventory:
            self.inventory.remove(item)

    def show_status(self): 
        status = super().show_status()
        status += f"HP: {self.hp}\nEXP: {self.exp}\nGold: {self.gold}\n"
        return status
    
    def show_inventory(self): # TODO: 아이템 상세정보, 여러개면 갯수 나타내서 간략화, 아이템 사용 등 추가
        inventory_info = "inventory:\n"
        for item in self.inventory:
            inventory_info += f"- {item.name} ({item.thing_type.value}, {item.raity.value})\n"
        return inventory_info


class Enemy(Character):
    '''defeat 메서드에서 drop_item, give_exp 호출 -> 플레이어에게 줌'''
    def __init__(self, name, level = 1, basic_damage = 8, hp = 80):
        super().__init__(name, level, basic_damage, hp)

    def drop_item(self, player: Player): # TODO: 아이템 다양화 후에 몬스터에 따라서 다르게 설정 -> 클래스로
        item = Item("Goblin's tooth", material.Things.MISC, material.Rarity.COMMON)
        player.get_item(item)


    def give_exp(self, player: Player): # TODO: 나중에 경험치 개선 -> 몬스터 레벨, 플레이어 레벨 차이 등
        exp_gain = self.level * 10
        player.exp += exp_gain
        if player.exp >= player.level * 100:
            player.level_up()

    def defeat(self, player: Player):
        self.give_exp(player)
        self.drop_item(player)

    




name = input("이름: ")
player = Player(name, level=1, basic_damage=15, hp=120)
enemy = Enemy("enemy", level=2, basic_damage=12, hp=100)

while True:
    print(f"\n플레이어 이름: {player.name}")
    print(f"{enemy.name}을 만났댜")
    print(f"플레이어 HP: {player.hp}")
    print(f"{enemy.name} HP: {enemy.hp}")
    action = input("행동을 선택하세요: [D] 데미지  [Q] 종료  [S] 상태창 보기  [I] 인벤토리 보기 : ").lower()
    if action == 's':
        print(player.show_status())
    elif action == 'd':
        player.attack(enemy)
        if enemy.hp<0:
            enemy.hp = 0
            print("고블린을 물리쳤다!")
            enemy.defeat(player)
            enemy.hp = 100
        enemy.attack(player)
        if player.hp<0:
            player.hp = 0
            print("패배\n")
            print(f"결과: \n{player.show_status()}\n{player.show_inventory()}")

            break
    elif action == 'i':
        print(player.show_inventory())
    elif action == 'q':
        break































# def main(stdscr):

#     curses.curs_set(0)
#     stdscr.nodelay(True) 

    

#     key = stdscr.getch()
#     h, w = stdscr.getmaxyx()

#     stdscr.addstr(1, int(w/2-9), "What's your name?")
#     curses.echo()
#     name = stdscr.getstr(2, int(w/2 - 5), 20).decode("utf-8")
#     curses.noecho()

#     player = Player(name, level=1, basic_damage=15, basic_hp=120)
#     enemy = Character("enemey", level=2, basic_damage=12, basic_hp=100)




#     while True:
#         stdscr.clear()
#         stdscr.addstr(0, 0, f"플레이어: {player.name}")
#         stdscr.addstr(1, 0, f"HP: {enemy.hp}")
#         stdscr.addstr(3, 0, "[D] 데미지  [Q] 종료")
#         stdscr.addstr(5, 0, "[S] 상태창 보기")
#         stdscr.refresh()

#         key = stdscr.getch()
#         if key == ord("s"):
#             stdscr.addstr(5,0, player.show_status())
#         elif key == ord("d"):
#             player.attack(enemy)
#             if enemy.hp < 0: 
#                 enemy.hp = 0
#         elif key == ord("q"):
#             break

#     time.sleep(0.1)

# curses.wrapper(main)  