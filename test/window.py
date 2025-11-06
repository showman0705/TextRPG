import curses
from pyfiglet import Figlet

def main(stdscr):


    curses.curs_set(0)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    f = Figlet(font = "doom")
    stdscr.border()
    text =  f.renderText('DANTE')


    status_win = curses.newwin(3, w-2, h-4, 1)
    status_win.border()
    status_win.addstr(1, 2, "HP: 120 | M  P: 30 | LV: 2")

    log_win = curses.newwin(h-6, w-2, 1, 1)
    for i, line in enumerate(text.splitlines()):
        try:
            log_win.addstr(int(h/2) - 3 + i, int(w/2) - 16, line)
        except curses.error:
            pass #TODO: 글씨 위치 바꾸면 맨위에 기준만 움직이는 거 고치기
    log_win.border()

    stdscr.refresh()
    status_win.refresh()
    log_win.refresh()
    stdscr.getch()

curses.wrapper(main)


