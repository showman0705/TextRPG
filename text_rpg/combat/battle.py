"""Simple turn based combat loop used by the prototype."""

from __future__ import annotations

import curses
from typing import Tuple

from entity.char.enemy import Enemy
from entity.char.player import Player
from entity.item.healingpotion import HealingPotion1

from text_rpg.ui import status as status_ui


def _find_healing_potion(player: Player) -> Tuple[int, object] | Tuple[None, None]:
    for idx, item in enumerate(player.inventory):
        name = getattr(item, "name", None)
        if name is None and isinstance(item, dict):
            name = item.get("name")
        if name == HealingPotion1.name:
            return idx, item
    return None, None


def _apply_healing(player: Player, item: object) -> None:
    heal_amount = getattr(item, "heal_amount", 30)
    player.hp = min(player.max_hp, player.hp + heal_amount)


def battle(stdscr: "curses._CursesWindow", player: Player, enemy: Enemy) -> bool:
    """Execute a combat encounter and return ``True`` if the enemy falls."""

    stdscr.nodelay(False)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"플레이어: {player.name}")
        stdscr.addstr(1, 0, f"적 HP: {enemy.hp}")
        stdscr.addstr(2, 0, f"플레이어 체력: {player.hp}/{player.max_hp}")
        stdscr.addstr(4, 0, "[D] 공격  [H] 힐  [S] 상태창  [I] 인벤토리  [Q] 종료")
        stdscr.refresh()

        key = stdscr.getch()

        if key in (ord("s"), ord("S")):
            status_ui.show_status(stdscr, player)
            continue
        if key in (ord("i"), ord("I")):
            status_ui.show_inventory(stdscr, player)
            continue
        if key in (ord("q"), ord("Q")):
            return False

        if key in (ord("h"), ord("H")):
            idx, item = _find_healing_potion(player)
            if idx is None:
                stdscr.addstr(6, 0, "회복물약이 없습니다.")
                stdscr.refresh()
                stdscr.getch()
                continue
            if hasattr(item, "use"):
                item.use(player)
            else:
                _apply_healing(player, item)
                player.inventory.pop(idx)
            continue

        if key in (ord("d"), ord("D")):
            damage = player.attack(enemy)
            stdscr.addstr(6, 0, f"{player.name}의 공격! {damage} 데미지")
            stdscr.refresh()
            if enemy.hp <= 0:
                enemy.hp = 0
                enemy.defeat(player, enemy)
                stdscr.addstr(7, 0, "적을 물리쳤습니다!")
                stdscr.refresh()
                stdscr.getch()
                return True

            stdscr.addstr(7, 0, f"{enemy.name}의 반격!")
            stdscr.refresh()
            stdscr.getch()

            damage = enemy.attack(player)
            stdscr.addstr(8, 0, f"{enemy.name}의 공격! {damage} 데미지")
            if player.hp <= 0:
                player.hp = 0
                stdscr.addstr(9, 0, "패배했습니다...")
                stdscr.refresh()
                stdscr.getch()
                return False
            stdscr.refresh()
            stdscr.getch()
            continue
