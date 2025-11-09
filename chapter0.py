import defs
import words
import json
from curses import wrapper



def play_chapter0(stdscr):
    with open(, 'r') as f:
        save_data = json.load(f)
    current_save = save_data['save']
    wrapper(stdscr, current_save, 1, words.chapter0_1)
    wrapper(stdscr, current_save, 2, words.chapter0_2)

