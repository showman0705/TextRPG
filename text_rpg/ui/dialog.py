"""Utilities responsible for rendering dialogue and narration."""

from __future__ import annotations

import curses
from time import sleep
from typing import Iterable, Sequence

from wcwidth import wcswidth


def typing_animation(stdscr: "curses._CursesWindow", text: str, y: int, x: int, speed: float = 0.05) -> None:
    """Print *text* character by character using a simple typewriter effect."""

    px = x
    for letter in text:
        stdscr.addstr(y, px, letter)
        stdscr.refresh()
        sleep(speed)
        px += max(1, wcswidth(letter))


def play_scene(
    stdscr: "curses._CursesWindow",
    scene: Sequence[str],
    *,
    typing_speed: float = 0.05,
) -> None:
    """Render a scene consisting of multiple lines with an optional typing effect."""

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.refresh()
    for line in scene:
        centered_y = height // 2
        centered_x = max(0, (width // 2) - (wcswidth(line) // 2) - 1)
        typing_animation(stdscr, line, centered_y, centered_x, typing_speed)
        stdscr.getch()
        stdscr.clear()
        stdscr.refresh()


def show_message(
    stdscr: "curses._CursesWindow",
    lines: Iterable[str],
    *,
    pause: bool = True,
) -> None:
    """Display a static message and optionally wait for user acknowledgement."""

    stdscr.clear()
    for idx, line in enumerate(lines):
        stdscr.addstr(idx, 0, line)
    stdscr.refresh()
    if pause:
        stdscr.getch()
