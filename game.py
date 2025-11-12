"""Top-level launcher for the TextRPG prototype."""

from __future__ import annotations

from curses import wrapper

from text_rpg.app import run


def main() -> None:
    wrapper(run)


if __name__ == "__main__":
    main()
