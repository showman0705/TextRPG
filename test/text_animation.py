import curses
from time import sleep

def typing_Ani(stdscr, text, y, x, speed):
    for i, letter in enumerate(text):
        stdscr.addstr(y, x + i, letter)
        stdscr.refresh()
        sleep(speed)

def type(stdscr):
    curses.curs_set(0)  # 커서 숨기기
    stdscr.clear()
    
    typing_Ani(stdscr, "hello world asdhjfkfeaekjfja", 5, 10, 0.1)
    
    stdscr.getch()

curses.wrapper(type)