import curses
from curses import wrapper
import material
import time
import random
from classes import Player, Enemy, Item, HealingPotion
import game_defs



HealingPotion1 = HealingPotion("Small Healing Potion",  heal_amount=30, thing_type=material.Things.POTION, potion_type=material.PotionType.HEALING, rarity=material.Rarity.COMMON)
# showman = Item("showman", thing_type=material.Things.MISC, rarity=material.Rarity.LEGENDARY)
showman = Item("showman", thing_type=material.Things.MISC, rarity=material.Rarity.EPIC)
tooth = Item("tooth", thing_type=material.Things.WEAPON, rarity=material.Rarity.COMMON)


# enemy = Enemy("enemy", level=2, basic_damage=12, item_give= showman, basic_defense= 3, hp=100, )

opponent = Enemy("opponent", level=1, basic_damage=10, basic_defense=3, hp=100, inventory=[showman, HealingPotion1, tooth])


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True) 
    key = stdscr.getch()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(1, int(w/2-9), "What's your name?")
    curses.echo()
    name = stdscr.getstr(2, int(w/2 - 5), 20).decode("utf-8")
    curses.noecho()
    player = Player(name, level=1, basic_damage=15, max_hp=120, hp = 120, exp = 0, gold = 100)
    
    game_defs.battle(stdscr, turn = True, player = player, enemy = opponent)

    time.sleep(0.1)

wrapper(main)