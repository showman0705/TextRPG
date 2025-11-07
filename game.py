import curses
from curses import wrapper
from game_folder import start
import game_defs
import words

def game_play(stdscr):
    wrapper(start.start_game)
    wrapper(game_defs.type(stdscr, words.chapter1_1))

wrapper(game_play)