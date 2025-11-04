# import curses
# from curses import wrapper

# import curses

# def main(stdscr):
#     curses.curs_set(0)           # 커서 숨기기
#     stdscr.clear()
#     stdscr.addstr(0, 0, "아무 키나 누르면 다음으로 진행합니다...")
#     stdscr.refresh()

#     stdscr.getch()               # 여기서 입력 대기
#     stdscr.addstr(2, 0, "다음 단계로 진행 중입니다!")
#     stdscr.refresh()
#     stdscr.getch()               # 종료 전 잠깐 대기

# curses.wrapper(main)
import curses
import random
import time

DANTE_ART = [
    "██████╗  █████╗ ███╗   ██╗████████╗███████╗",
    "██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝",
    "██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ",
    "██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ",
    "██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗",
    "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝"
]

# 색상 단계 (밝은색 → 어두운색 → 검정)
COLOR_PHASES = [
    [curses.COLOR_YELLOW, curses.COLOR_WHITE],  # 밝게 타오름
    [curses.COLOR_RED, curses.COLOR_YELLOW],    # 뜨겁게 탐
    [curses.COLOR_MAGENTA, curses.COLOR_RED],   # 그을림 시작
    [curses.COLOR_BLACK, curses.COLOR_BLACK],   # 완전히 탔음
]

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    # 색상쌍 등록
    for i, (fg, bg) in enumerate(COLOR_PHASES, start=1):
        curses.init_pair(i, fg, bg)

    h, w = stdscr.getmaxyx()
    art_height = len(DANTE_ART)
    art_width = len(DANTE_ART[0])
    base_y = h // 2 - art_height // 2
    base_x = w // 2 - art_width // 2
    stdscr.getch()
    stdscr.nodelay(True)

    
    burn_progress = 0  # 0 ~ 100 사이 진행도
    while burn_progress <= 100:
        stdscr.clear()

        # 진행도에 따라 색상 단계 선택
        phase = min(len(COLOR_PHASES) - 1, burn_progress // 25)

        for i, line in enumerate(DANTE_ART):
            for j, ch in enumerate(line):
                if ch == " ":
                    continue

                # 랜덤하게 일부 문자는 이미 탔거나 아직 밝게 남아 있음
                fade_chance = random.randint(0, 100)
                if fade_chance < burn_progress:  # 타서 사라짐
                    color = len(COLOR_PHASES)
                else:
                    color = random.randint(1, phase + 1)

                stdscr.addstr(base_y + i, base_x + j, ch, curses.color_pair(color))

        stdscr.refresh()
        time.sleep(0.08)
        burn_progress += 2

        # 키 입력 시 중단
        key = stdscr.getch()
        if key != -1:
            break

    # 다 타버린 후
    stdscr.clear()
    stdscr.addstr(h//2, w//2 - 7, "🔥 DANTE BURNT OUT 🔥", curses.A_BOLD)
    stdscr.refresh()
    time.sleep(0.65)
    stdscr.getch()

curses.wrapper(main)



# import curses
# import time

# DRAGON = [
#     "           __====-_  _-====__",
#     "     _--^^^#####//      \\\\#####^^^--_",
#     "  _-^##########// (    ) \\\\##########^-_",
#     " -############//  |\\^^/|  \\\\############-",
#     "_/############//   (@::@)   \\\\############\\_",
#     "/#############((     \\\\//     ))#############\\",
#     "-###############\\\\    (oo)    //###############-",
#     " -#################\\\\  /VV\\  //#################-",
#     "  --###################\\/##\\/###################--",
#     "    ^^--#################^^#################--^^",
#     "          ^^--##############--##############--^^",
#     "                 ^^--#########--#########--^^",
#     "                       ^^--###--###--^^",
#     "                           ^^--^^"
# ]

# def main(stdscr):
#     curses.curs_set(0)
#     stdscr.clear()
#     h, w = stdscr.getmaxyx()

#     start_y = h//2 - len(DRAGON)//2
#     start_x = w//2 - len(DRAGON[0])//2

#     for i, line in enumerate(DRAGON):
#         stdscr.addstr(start_y + i, start_x, line)
#         stdscr.refresh()
#         time.sleep(0.05)

#     stdscr.addstr(h - 2, w//2 - 10, "아무 키나 누르세요.")
#     stdscr.refresh()
#     stdscr.getch()

# curses.wrapper(main)
