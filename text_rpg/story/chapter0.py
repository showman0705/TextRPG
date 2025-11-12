"""Implementation of the introductory chapter."""

from __future__ import annotations

from typing import Callable, List, Optional

import words

from text_rpg.state import GameState
from text_rpg.ui.dialog import play_scene, show_message

SceneHandler = Callable[["curses._CursesWindow", GameState], None]


SCENES: List[SceneHandler] = [
    lambda stdscr, state: play_scene(stdscr, words.chapter0_1),
    lambda stdscr, state: play_scene(stdscr, words.chapter0_2),
    lambda stdscr, state: play_scene(stdscr, words.chapter0_3),
]


def play(
    stdscr: "curses._CursesWindow",
    state: GameState,
    autosave: Optional[Callable[[GameState], None]] = None,
) -> None:
    while state.progress.scene_index < len(SCENES):
        scene_fn = SCENES[state.progress.scene_index]
        scene_fn(stdscr, state)
        state.advance_scene()
        if autosave is not None:
            autosave(state)

    show_message(
        stdscr,
        ["Chapter 0 종료", "다음 챕터는 아직 준비 중입니다."],
        pause=True,
    )
