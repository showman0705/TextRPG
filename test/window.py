import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.border()

    status_win = curses.newwin(3, w-2, h-4, 1)
    status_win.border()
    status_win.addstr(1, 2, "HP: 120 | MP: 30 | LV: 2")

    log_win = curses.newwin(h-6, w-2, 1, 1)
    log_win.addstr(1, 2, "적을 만났다")
    log_win.border()

    stdscr.refresh()
    status_win.refresh()
    log_win.refresh()
    stdscr.getch()

curses.wrapper(main)
