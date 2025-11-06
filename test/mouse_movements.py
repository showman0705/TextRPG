# import curses

# def main(stdscr):
#     curses.curs_set(0)
#     stdscr.keypad(True)

#     # 마우스 이벤트 활성화
#     curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

#     stdscr.addstr(0, 0, "마우스를 클릭하거나 이동해보세요. (q: 종료)")

#     while True:
#         key = stdscr.getch()
#         if key == ord('q'):
#             break
#         elif key == curses.KEY_MOUSE:
#             _, mx, my, _, bstate = curses.getmouse()
#             stdscr.addstr(2, 0, f"마우스 좌표: ({mx}, {my})  상태: {bstate}     ")
#             stdscr.refresh()

# curses.wrapper(main)


import curses

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    menu = ["Start", "Settings", "Exit"]
    h, w = stdscr.getmaxyx()

    while True:
        stdscr.clear()
        for i, item in enumerate(menu):
            x = w // 2 - len(item) // 2
            y = h // 2 - len(menu) // 2 + i
            stdscr.addstr(y, x, item)
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            for i, item in enumerate(menu):
                x = w // 2 - len(item) // 2
                y = h // 2 - len(menu) // 2 + i
                if y == my and x <= mx < x + len(item):
                    stdscr.addstr(h - 2, 0, f"{item} 선택됨!")
                    stdscr.refresh()
                    if item == "Exit":
                        return
        elif key == ord('q'):
            break

curses.wrapper(main)
