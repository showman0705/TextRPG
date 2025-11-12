"""Core package for the TextRPG project.

This namespace regroup the high level building blocks used by the
curses-based prototype.  Modules are structured by concerns (state
management, UI helpers, combat utilities, etc.) so that subsequent
iterations can extend the game without dealing with a monolithic
`defs.py` file.
"""

from . import app, state  # re-export for convenience

__all__ = ["app", "state"]
