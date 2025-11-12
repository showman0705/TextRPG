"""Narrative chapter registry and helpers."""

from __future__ import annotations

from typing import Callable, Dict, Optional

from text_rpg.state import GameState

from . import chapter0

ChapterHandler = Callable[["curses._CursesWindow", GameState, Optional[Callable[[GameState], None]]], None]


CHAPTER_REGISTRY: Dict[str, ChapterHandler] = {
    "chapter0": chapter0.play,
}


def run_chapter(
    stdscr: "curses._CursesWindow",
    state: GameState,
    *,
    autosave: Optional[Callable[[GameState], None]] = None,
) -> None:
    handler = CHAPTER_REGISTRY.get(state.progress.chapter_id)
    if handler is None:
        raise KeyError(f"Unknown chapter id: {state.progress.chapter_id}")
    handler(stdscr, state, autosave)


def register_chapter(identifier: str, handler: ChapterHandler) -> None:
    CHAPTER_REGISTRY[identifier] = handler
