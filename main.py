import curses
from curses import wrapper
import material
import time
import random
import entity.char.player as player
import entity.char.enemy as enemy
import entity.item.item as item
import entity.item.healingpotion as healingpotion
import game_defs


# showman = Item("showman", thing_type=material.Things.MISC, rarity=material.Rarity.LEGENDARY)
showman = item.Item("showman", thing_type=material.Things.MISC, rarity=material.Rarity.EPIC)
tooth = item.Item("tooth", thing_type=material.Things.WEAPON, rarity=material.Rarity.COMMON)


# enemy = Enemy("enemy", level=2, basic_damage=12, item_give= showman, basic_defense= 3, hp=100, )



def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True) 
    key = stdscr.getch()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(1, int(w/2-9), "What's your name?")
    curses.echo()
    name = stdscr.getstr(2, int(w/2 - 5), 20).decode("utf-8")
    curses.noecho()
    you = player.Player(name, level=1, basic_damage=15, basic_defense=3, max_hp=120, hp = 120, exp = 0, gold = 100)
    opponent = enemy.Enemy("opponent", level=1, basic_damage=10, basic_defense=3, hp=100, inventory=[showman, healingpotion.HealingPotion1, tooth])

    game_defs.battle(stdscr, turn = True, player = you, enemy = opponent)

    time.sleep(0.1)

wrapper(main)