import curses
from curses import wrapper
from pyfiglet import Figlet

def show_title_scr(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    f = Figlet(font="doom")
    text = f.renderText("DANTE")
    for i, line in enumerate(text.splitlines()):
        try:
            stdscr.addstr(int(h / 2) - 10 + i, int(w / 2) - len(line)//2, line)
        except curses.error:
            pass

    stdscr.refresh()
    stdscr.addstr(int(h / 2) - 2, int(w / 2) - 12, "Press any key to start....")
    stdscr.refresh()
    stdscr.getch()  # 게임 시작전에 Press어쩌구 그거
    stdscr.addstr(int(h / 2) - 2, int(w / 2) - 12, "                          ")
    stdscr.refresh()

    menu_height = 11
    menu_width = 30
    menu_start_y = int(h / 2)
    menu_start_x = int(w / 2 - menu_width / 2)
    menu_win = curses.newwin(menu_height, menu_width, menu_start_y, menu_start_x)
    menu_win.keypad(True)
    menu_win.box()

    titles = ["새 게임","불러오기", "옵션", "종료"]
    current_curs = 0

    while True:
        menu_win.clear()
        menu_win.box()

        for i, title in enumerate(titles):
            x = int((menu_width - len(title)) / 2)
            y = 2 + i * 2
            if i == current_curs:
                menu_win.addstr(y, x - len(title) + 1, "<" + title + ">")
            else:
                menu_win.addstr(y, x - len(title) + 1, title)

        menu_win.refresh()

        key = menu_win.getch()

        if key == curses.KEY_UP:
            current_curs = (current_curs - 1) % len(titles)
        elif key == curses.KEY_DOWN:
            current_curs = (current_curs + 1) % len(titles)
 
        elif titles[current_curs] == "종료":
            break
        else:
            menu_win.addstr(menu_height - 2, 2, f"{titles[current_curs]}")
            menu_win.refresh()
            menu_win.getch()
        
wrapper(show_title_scr)
