"""Compatibility shim for older imports."""

from __future__ import annotations

from text_rpg.story.chapter0 import play  # re-export

__all__ = ["play"]
