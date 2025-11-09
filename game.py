import curses
from curses import wrapper
from game_folder import start
import defs
import words

def game_play(stdscr):
    wrapper(start.start_game)

wrapper(game_play)