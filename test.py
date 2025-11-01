import curses
from curses import wrapper

import curses

def main(stdscr):
    curses.curs_set(0)           # 커서 숨기기
    stdscr.clear()
    stdscr.addstr(0, 0, "아무 키나 누르면 다음으로 진행합니다...")
    stdscr.refresh()

    stdscr.getch()               # 여기서 입력 대기
    stdscr.addstr(2, 0, "다음 단계로 진행 중입니다!")
    stdscr.refresh()
    stdscr.getch()               # 종료 전 잠깐 대기

curses.wrapper(main)
