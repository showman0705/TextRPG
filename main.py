import curses
from curses import wrapper
import material
import Item
import Enemy
import time
import random

############### 캐릭터 ###############
class Character():
    '''initial_defense = 5, initial_mana = 30
    나중에 방어력, 마나 등 추가'''
    def __init__(self, name, level=1, basic_damage = 10, basic_defense = 3, hp = 100, ):
        self.name = name
        self.level = level
        self.basic_damage = basic_damage
        self.basic_defense = basic_defense
        self.hp = hp  

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
    def __init__(self, name, level = 1, basic_damage = 10, basic_defense = 3, max_hp = 100, hp = 100, inventory = None, sin_list = None, exp = 0, gold = 100):
        super().__init__(name, level, basic_damage, basic_defense, hp)
        self.exp = exp
        self.max_hp = max_hp
        self.gold = gold
        self.inventory = inventory if inventory is not None else []
        self.sin_list = sin_list if sin_list is not None else []

    def level_up(self): 
        self.level += 1
        self.basic_damage += 5
        self.max_hp += 20
        level_up_message = f"{self.name} 레벨업, 현재레벨: {self.level}"
        return level_up_message

    def get_item(self, item):
        self.inventory.append(item)

    def use_item(self, item): # TODO: 아이템 효과 추가
        if item in self.inventory:
            self.inventory.remove(item)

    def show_status(self): 
        status = super().show_status()
        status += f"HP: {self.hp}/{self.max_hp}\nEXP: {self.exp}\nGold: {self.gold}\n"
        # 죄악 추가
        return status
    
    def show_inventory(self): # TODO: 아이템 상세정보, 여러개면 갯수 나타내서 간략화, 아이템 사용 등 추가
        inventory_info = "inventory:\n"
        for item in self.inventory:
            inventory_info += f"- {item.name} ({item.thing_type.value}, {item.rarity.value})\n"
        return inventory_info
############## 플레이어 ###############

################ 적 #################
class Enemy(Character):
    '''defeat 메서드에서 drop_item, give_exp 호출 -> 플레이어에게 줌'''
    def __init__(self, name, level, basic_damage, basic_defense, hp):
        super().__init__(name, level, basic_damage, hp)
        self.basic_defense = basic_defense

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
############### 적 #################

############### 질투(가시 데미지) 구현 가능 확인 ################
class Invidia_3(Enemy):
    def __init__(self, name, level, basic_damage, basic_defense, hp, sin: material.Sin.Invidia):
        super().__init__(name, level, basic_damage, basic_defense, hp)
        self.sin = sin
    def give_sin_Invidia(self, target: Character):
        if target.attack(self):
            target.hp -= target.attack() *(10/100)
            print("질투")
############## 질투(가시 데미지) 구현 가능 확인 ################




################ 아이템 #################
class Item():
    def __init__(self, name, thing_type: material.Things, rarity: material.Rarity):
        self.name = name
        self.thing_type = thing_type
        self.rarity = rarity

    def show_info(self):
        info = f"Item Name: {self.name}\nType: {self.thing_type.value}\nRarity: {self.rarity.value}\n"

class Potion(Item):
    def __init__(self, name, thing_type: material.Things.POTION, rarity: material.Rarity):
        super().__init__(name, thing_type, rarity)
################## 아이템 #################


######## 회복 물약 #################
class HealingPotion(Potion):
    def __init__(self, name, heal_amount, thing_type: material.Things.POTION, potion_type: material.PotionType.HEALING, rarity: material.Rarity):
        super().__init__(name, thing_type, rarity)
        self.heal_amount = heal_amount

    def use(self, user: Player):
        user.hp += self.heal_amount
        user.use_item(self)
######## 회복 물약 #################

HealingPotion1 = HealingPotion("Small Healing Potion", heal_amount=30, thing_type=material.Things.POTION, potion_type=material.PotionType.HEALING, rarity=material.Rarity.COMMON)

# name = input("이름: ")
# player = Player(name, level=1,basic_damage=15, basic_defense = 3, max_hp = 100, hp=100)
# enemy = Invidia_3("질투의 제3권속", level=2, basic_damage=8, basic_defense= 3, hp=100, sin = material.Sin.Invidia)

# def battle(player, enemy):
#     print(f"플레이어 이름")

# while True:
#     print(f"\n플레이어 이름: {player.name}")
#     print(f"{enemy.name}을 만났댜")
#     print(f"플레이어 HP: {player.hp}")
#     print(f"{enemy.name} HP: {enemy.hp}")
#     action = input("행동을 선택하세요: [D] 데미지  [H] 회복  [Q] 종료  [S] 상태창 보기  [I] 인벤토리 보기 : ").lower()
#     player.get_item(HealingPotion1)  # 테스트용으로 매턴 회복물약 추가
#     if action == 's':
#         print(player.show_status())
#     elif action == 'd':
#         player.attack(enemy)
#         if enemy.hp<0:
#             enemy.hp = 0
#             print("질투의 제3권속을 물리쳤다!")
#             enemy.defeat(player)
#             enemy.hp = 100
#         enemy.attack(player)
#         if player.hp<0:
#             player.hp = 0
#             print("패배\n")
#             print(f"결과: \n{player.show_status()}\n{player.show_inventory()}")
#             break
#     elif action == 'h':
#         if HealingPotion1 in player.inventory:
#             HealingPotion1.use(player)
#             if player.hp > player.max_hp:
#                 player.hp = player.max_hp
#         else:
#             print("회복 물약이 없음")
#     elif action == 'i':
#         print(player.show_inventory())
#     elif action == 'q':
#         break

# def main(stdscr):
#     curses.curs_set(0)
#     stdscr.nodelay(True)

#     key = stdscr.getch()
#     h, w = stdscr.getmaxyx()

#     stdscr.clear()
#     stdscr.addstr(2, int(w/2 - len("Press any button to continue....")/2), "Press any button to continue....")
#     stdscr.getch()
#     stdscr.clear()
#     stdscr.addstr(1, int(w/2-9), "What's your name?")
#     curses.echo()
#     name = stdscr.getstr(2, int(w/2 - 5), 20).decode("utf-8")
#     curses.echo()
#     player = Player(name, level=1,basic_damage=15, basic_defense = 3, max_hp = 100, hp=100)
#     curses.noecho()
#     stdscr.refresh()

#     stdscr.addstr(player.show_status())






# wrapper(main)






def main(stdscr):

    curses.curs_set(0)
    stdscr.nodelay(True) 

    

    key = stdscr.getch()
    h, w = stdscr.getmaxyx()

    stdscr.addstr(1, int(w/2-9), "What's your name?")
    curses.echo()
    name = stdscr.getstr(2, int(w/2 - 5), 20).decode("utf-8")
    curses.noecho()

    player = Player(name, level=1, basic_damage=15, max_hp=120, hp = 120)
    enemy = Enemy("enemey", level=2, basic_damage=12, basic_defense= 3, hp=100)




    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"플레이어: {player.name}")
        stdscr.addstr(2,0, f"플레이어 체력: {player.hp}/{player.max_hp}")
        stdscr.addstr(1, 0, f"적 HP: {enemy.hp}")
        stdscr.addstr(3, 0, "[D] 데미지  [Q] 종료")
        stdscr.addstr(4, 0, "[S] 상태창 보기")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("s"):
            stdscr.nodelay(False)  
            stdscr.clear()
            stdscr.addstr(0, 0, "===== 상태창 =====")
            stdscr.addstr(1, 0, player.show_status())
            stdscr.addstr(4, 0, "\n아무 키나 누르면 돌아갑니다.")
            stdscr.refresh()
            stdscr.getch() 
            stdscr.nodelay(True)  
            continue
        elif key == ord("d"):
            player.attack(enemy)
            if enemy.hp < 0: 
                enemy.hp = 0
                enemy.defeat(player)
                stdscr.addstr(7,0, "enemy 해치움")
                stdscr.refresh()
            else:
                enemy.attack(player)
                if player.hp < 0:
                    player.hp = 0
                    stdscr.addstr("패배")
                
        elif key == ord("q"):
            break

    time.sleep(0.1)

curses.wrapper(main)  