"""Entry point used by :mod:`game` and :mod:`main`."""

from __future__ import annotations

import curses

from text_rpg.save.manager import SaveManager
from text_rpg.ui.menu import TitleScreen


def run(stdscr: "curses._CursesWindow") -> None:
    stdscr.clear()
    menu = TitleScreen(save_manager=SaveManager())
    menu.run(stdscr)
