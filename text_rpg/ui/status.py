"""Curses helpers for showing various player-centric overlays."""

from __future__ import annotations

import curses
from typing import Iterable

from entity.char.player import Player


def _draw_lines(window: "curses._CursesWindow", lines: Iterable[str]) -> None:
    for idx, line in enumerate(lines):
        window.addstr(idx, 0, line)


def show_status(stdscr: "curses._CursesWindow", player: Player) -> None:
    stdscr.nodelay(False)
    stdscr.clear()
    _draw_lines(
        stdscr,
        [
            "===== 상태창 =====",
            player.show_status(),
            "아무 키나 누르면 돌아갑니다.",
        ],
    )
    stdscr.refresh()
    stdscr.getch()
    stdscr.nodelay(True)


def show_level(stdscr: "curses._CursesWindow", player: Player) -> None:
    stdscr.nodelay(False)
    stdscr.clear()
    _draw_lines(
        stdscr,
        [
            "===== 스킬 레벨업 =====",
            "레벨업할 스킬들",
            "아무 키나 누르면 돌아갑니다.",
        ],
    )
    stdscr.refresh()
    stdscr.getch()
    stdscr.nodelay(True)


def show_inventory(stdscr: "curses._CursesWindow", player: Player) -> None:
    stdscr.nodelay(False)
    stdscr.clear()
    lines = ["===== 인벤토리 =====", player.show_inventory().rstrip(), "아무 키나 누르면 돌아갑니다."]
    for idx, line in enumerate(lines):
        stdscr.addstr(idx, 0, line)
    stdscr.refresh()
    stdscr.getch()
    stdscr.nodelay(True)
