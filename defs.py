from entity.item.healingpotion import HealingPotion1
import entity.material as material
from time import sleep
import curses


def curses_show_status(stdscr, player):
    '''curses에서 스텟보여주는 거 한번에 모아놓은 함수 간단하게 만들려고'''
    stdscr.nodelay(False)  
    stdscr.clear()  
    stdscr.addstr(0, 0, "===== 상태창 =====")
    stdscr.addstr(1, 0, player.show_status())
    stdscr.addstr(7 , 0, "아무 키나 누르면 돌아갑니다.")
    stdscr.refresh()
    stdscr.getch()
    stdscr.nodelay(True)

def curses_show_level(stdscr, player):
    stdscr.nodelay(False)
    stdscr.clear()
    stdscr.addstr(0,0, "===== 스킬 레벨업 =====")
    stdscr.addstr(3, 0, "레벨업할 스킬들")
    stdscr.addstr(5, 0, "아무 키나 누르면 돌아갑니다.")
    stdscr.refresh()
    stdscr.getch()
    stdscr.nodelay(True)

def curses_show_inventory(stdscr, player): # TODO: 인벤토리창의 길이가 너무 길어지면 오류가 생김 이거 해결
    key = stdscr.getch()
    stdscr.nodelay(False)
    stdscr.clear()
    stdscr.addstr(0,0, "===== 인벤토리 =====")
    stdscr.addstr(1,0, player.show_inventory())
    stdscr.addstr(3 + len(list(dict.fromkeys(player.inventory))), 0, "아무 키나 누르면 돌아갑니다.")
    stdscr.refresh()
    stdscr.getch()
    stdscr.nodelay(True)

def battle(stdscr, turn, player, enemy): # TODO: battle 함수는 전투를 완벽히 하나의 함수로 표현 -> 필요할때마다 호출
    turn = True

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"플레이어: {player.name}")
        stdscr.addstr(2,0, f"플레이어 체력: {player.hp}/{player.max_hp}")
        stdscr.addstr(1, 0, f"적 HP: {enemy.hp}")
        stdscr.addstr(3, 0, "[D] 데미지  [Q] 종료")
        stdscr.addstr(4, 0, "[H] 힐  [S] 상태창 보기  [I] 인벤토리 보기")
        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("s"):
            curses_show_status(stdscr, player)
            if key == ord("l"):
                curses_show_level(stdscr, player)
            continue    # 스테이터스 표시

        if key == ord("i"):
            curses_show_inventory(stdscr, player)
            continue    # 인벤토리 표시

        elif key == ord("d"):
            if turn:
                player.attack(enemy)
                turn = False
                if enemy.hp <= 0: 
                    enemy.hp = 0
                    enemy.defeat(player, enemy)
                    stdscr.addstr(7,0, "enemy 해치움")
                    stdscr.refresh()
                    enemy.hp = 100
                
            else:
                stdscr.getch()
                enemy.attack(player)
                turn = True
                if player.hp <= 0:
                    player.hp = 0
                    stdscr.clear()
                    stdscr.addstr(0,0,"패배")
                    stdscr.refresh()

        elif key == ord("q"):
            break

        elif key == ord("h"):
            if HealingPotion1 in player.inventory:
                HealingPotion1.use(player)
                if player.hp > player.max_hp:
                    player.hp = player.max_hp
            else:
                stdscr.addstr(10,0, "회복물약이 없습니다.")

# import curses
# from curses import wrapper
# import material
# import time
# import random
# import entity.char.player as player
# import entity.char.enemy as enemy
# import entity.item.item as item
# import entity.item.healingpotion as healingpotion
# import game_defs


# # showman = Item("showman", thing_type=material.Things.MISC, rarity=material.Rarity.LEGENDARY)
# showman = item.Item("showman", thing_type=material.Things.MISC, rarity=material.Rarity.EPIC)
# tooth = item.Item("tooth", thing_type=material.Things.WEAPON, rarity=material.Rarity.COMMON)


# # enemy = Enemy("enemy", level=2, basic_damage=12, item_give= showman, basic_defense= 3, hp=100, )



# def main(stdscr):
#     curses.curs_set(0)
#     stdscr.nodelay(True) 
#     key = stdscr.getch()
#     h, w = stdscr.getmaxyx()
#     stdscr.addstr(1, int(w/2-9), "What's your name?")
#     curses.echo()
#     name = stdscr.getstr(2, int(w/2 - 5), 20).decode("utf-8")
#     curses.noecho()
#     you = player.Player(name, level=1, basic_damage=15, basic_defense=3, max_hp=120, hp = 120, exp = 0, gold = 100)
#     opponent = enemy.Enemy("opponent", level=1, basic_damage=10, basic_defense=3, hp=100, inventory=[showman, healingpotion.HealingPotion1, tooth])

#     game_defs.battle(stdscr, turn = True, player = you, enemy = opponent)

#     time.sleep(0.1)

# wrapper(main)


#################################################################################################################################



import words
import locale
from curses import wrapper
from wcwidth import wcswidth
import json

locale.setlocale(locale.LC_ALL, '')

def typing_Ani(stdscr, text, y, x, speed):
    key = stdscr.getch()
    px = x
    for i, letter in enumerate(text):
        stdscr.addstr(y, px, letter)
        stdscr.refresh()
        sleep(speed)
        px += wcswidth(letter)



def type(stdscr, scene: list):
    key = stdscr.getch()
    y, x = stdscr.getmaxyx()
    curses.curs_set(0)  # 커서 숨기기
    stdscr.clear()
    for i in range(len(scene)):
        typing_Ani(stdscr, scene[i], int(y/2) , int(x/2) - int(wcswidth(scene[i])/2) - 1 , 0.1)
        stdscr.getch()
        stdscr.clear()
        stdscr.refresh()

def save_game_data():
    '''게임 데이터 저장 함수'''
    with open('C:\\Users\\showm\\TextRPG\\savefile.json', 'r') as f:
        save_data = json.load(f)
        save_data['save'] += 1
    with open('C:\\Users\\showm\\TextRPG\\savefile.json', 'w') as f:
        json.dump(save_data, f, indent= 4, ensure_ascii=False)

def new_save(i):
    '''새 게임'''
    save_json = {
    "save" : 1 
}
    with open('save' + i, 'w') as f:
        json.dump(save_json, f, indent = 4, ensure_ascii=False)
    

def continue_game(stdscr, save, current, chapter):
    '''불러오기'''
    if save == current:
        type(stdscr, chapter)
        wrapper(save_game_data)
        sleep(1)

