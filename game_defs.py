from entity.item.healingpotion import HealingPotion1
import material


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
