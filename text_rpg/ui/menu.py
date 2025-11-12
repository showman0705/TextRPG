"""Title menu and input helpers."""

from __future__ import annotations

import curses
from dataclasses import dataclass
from typing import List, Optional

from pyfiglet import Figlet

from text_rpg.save.manager import SaveManager
from text_rpg.state import GameState
from text_rpg.story import run_chapter
from text_rpg.ui.dialog import show_message


@dataclass
class MenuEntry:
    label: str


class TitleScreen:
    def __init__(self, save_manager: Optional[SaveManager] = None) -> None:
        self.save_manager = save_manager or SaveManager()
        self.entries: List[MenuEntry] = [
            MenuEntry("새 게임"),
            MenuEntry("불러오기"),
            MenuEntry("옵션"),
            MenuEntry("종료"),
        ]

    def run(self, stdscr: "curses._CursesWindow") -> None:
        curses.curs_set(0)
        current_index = 0
        while True:
            self._draw_title(stdscr)
            current_index = self._draw_menu(stdscr, current_index)
            selection = self.entries[current_index].label
            if selection == "새 게임":
                self._start_new_game(stdscr)
            elif selection == "불러오기":
                self._load_game(stdscr)
            elif selection == "옵션":
                show_message(stdscr, ["옵션 메뉴는 아직 준비 중입니다."], pause=True)
            elif selection == "종료":
                break

    def _draw_title(self, stdscr: "curses._CursesWindow") -> None:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        f = Figlet(font="doom")
        text = f.renderText("DANTE")
        for i, line in enumerate(text.splitlines()):
            try:
                stdscr.addstr(max(0, height // 2 - 10 + i), max(0, width // 2 - len(line) // 2), line)
            except curses.error:
                pass
        stdscr.addstr(height // 2 - 2, max(0, width // 2 - 12), "Press any key to start....")
        stdscr.refresh()
        stdscr.getch()

    def _draw_menu(self, stdscr: "curses._CursesWindow", start_index: int) -> int:
        height, width = stdscr.getmaxyx()
        menu_height = 11
        menu_width = 30
        menu_start_y = max(0, height // 2)
        menu_start_x = max(0, width // 2 - menu_width // 2)
        index = start_index

        while True:
            menu_win = curses.newwin(menu_height, menu_width, menu_start_y, menu_start_x)
            menu_win.keypad(True)
            menu_win.box()
            for i, entry in enumerate(self.entries):
                x = max(1, (menu_width - len(entry.label)) // 2)
                y = 2 + i * 2
                label = entry.label
                if i == index:
                    label = f"< {label} >"
                    col = max(1, x - len(label) // 2)
                    menu_win.addstr(y, col, label, curses.A_BOLD)
                else:
                    col = max(1, x - len(label) // 2)
                    menu_win.addstr(y, col, label, curses.A_DIM)
            menu_win.refresh()
            key = menu_win.getch()
            if key == curses.KEY_UP:
                index = (index - 1) % len(self.entries)
            elif key == curses.KEY_DOWN:
                index = (index + 1) % len(self.entries)
            elif key in (curses.KEY_ENTER, ord("\n"), ord("\r")):
                menu_win.clear()
                stdscr.touchwin()
                stdscr.refresh()
                return index

    def _prompt_player_name(self, stdscr: "curses._CursesWindow") -> Optional[str]:
        stdscr.clear()
        curses.echo()
        height, width = stdscr.getmaxyx()
        prompt = "이름을 입력하세요: "
        stdscr.addstr(height // 2, max(0, width // 2 - len(prompt) // 2), prompt)
        stdscr.refresh()
        name_bytes = stdscr.getstr(height // 2 + 1, width // 2 - 10, 20)
        curses.noecho()
        name = name_bytes.decode("utf-8").strip()
        return name or None

    def _start_new_game(self, stdscr: "curses._CursesWindow") -> None:
        name = self._prompt_player_name(stdscr)
        if not name:
            show_message(stdscr, ["이름이 입력되지 않았습니다."], pause=True)
            return
        state = GameState.new_game(name)
        run_chapter(stdscr, state, autosave=self.save_manager.autosave)

    def _load_game(self, stdscr: "curses._CursesWindow") -> None:
        slots = self.save_manager.available_slots()
        if not slots:
            show_message(stdscr, ["저장된 데이터가 없습니다."], pause=True)
            return
        selection = self._select_slot(stdscr, slots)
        if selection is None:
            return
        try:
            state = self.save_manager.load(selection)
        except FileNotFoundError:
            show_message(stdscr, ["선택한 슬롯은 비어 있습니다."], pause=True)
            return
        run_chapter(stdscr, state, autosave=self.save_manager.autosave)

    def _select_slot(self, stdscr: "curses._CursesWindow", slots: List[dict]) -> Optional[int]:
        height, width = stdscr.getmaxyx()
        menu_height = max(5, len(slots) * 3 + 4)
        menu_width = 50
        menu_start_y = max(0, height // 2 - menu_height // 2)
        menu_start_x = max(0, width // 2 - menu_width // 2)
        index = 0

        while True:
            menu_win = curses.newwin(menu_height, menu_width, menu_start_y, menu_start_x)
            menu_win.keypad(True)
            menu_win.box()
            for i, slot in enumerate(slots):
                label = f"슬롯 {slot['slot']}: {slot['summary']} ({slot['timestamp']})"
                y = 2 + i * 2
                if i == index:
                    menu_win.addstr(y, 2, label[: menu_width - 4], curses.A_BOLD)
                else:
                    menu_win.addstr(y, 2, label[: menu_width - 4])
            menu_win.refresh()
            key = menu_win.getch()
            if key == curses.KEY_UP:
                index = (index - 1) % len(slots)
            elif key == curses.KEY_DOWN:
                index = (index + 1) % len(slots)
            elif key in (curses.KEY_ENTER, ord("\n"), ord("\r")):
                selected_slot = slots[index]["slot"]
                menu_win.clear()
                stdscr.touchwin()
                stdscr.refresh()
                return selected_slot
            elif key in (27, ord("q"), ord("Q")):
                menu_win.clear()
                stdscr.touchwin()
                stdscr.refresh()
                return None
