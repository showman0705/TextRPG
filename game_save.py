"""Compatibility layer that forwards to :class:`text_rpg.save.manager.SaveManager`."""

from __future__ import annotations

from text_rpg.save.manager import SaveManager
from text_rpg.state import GameState
from text_rpg.story import run_chapter

_DEFAULT_MANAGER = SaveManager()


def save_game_data(state: GameState, slot: int = 1) -> None:
    _DEFAULT_MANAGER.save(state, slot=slot)


def new_save(state: GameState, slot: int = 1) -> None:
    _DEFAULT_MANAGER.save(state, slot=slot)


def continue_game(stdscr: "curses._CursesWindow", slot: int = 1) -> None:
    state = _DEFAULT_MANAGER.load(slot)
    run_chapter(stdscr, state, autosave=_DEFAULT_MANAGER.autosave)
