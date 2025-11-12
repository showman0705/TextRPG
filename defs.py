"""Legacy helpers kept for backwards compatibility.

The project historically stored assorted gameplay utilities inside this
module.  The new layout organises them under :mod:`text_rpg`, but we keep
thin wrappers here so that older imports do not immediately break.
"""

from __future__ import annotations

from text_rpg.combat.battle import battle
from text_rpg.save.manager import SaveManager
from text_rpg.ui.dialog import play_scene as type_scene
from text_rpg.ui.dialog import typing_animation as typing_Ani
from text_rpg.ui.status import show_inventory as curses_show_inventory
from text_rpg.ui.status import show_level as curses_show_level
from text_rpg.ui.status import show_status as curses_show_status

__all__ = [
    "battle",
    "curses_show_inventory",
    "curses_show_level",
    "curses_show_status",
    "type_scene",
    "typing_Ani",
    "SaveManager",
]


def type(stdscr, scene):
    """Compatibility alias for :func:`text_rpg.ui.dialog.play_scene`."""

    type_scene(stdscr, scene)
