"""Game state abstractions used by the TextRPG prototype."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional

from entity.char.player import Player


@dataclass
class Progress:
    """Represents the player's position inside the narrative flow."""

    chapter_id: str = "chapter0"
    scene_index: int = 0
    flags: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chapter_id": self.chapter_id,
            "scene_index": self.scene_index,
            "flags": self.flags,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Progress":
        return cls(
            chapter_id=data.get("chapter_id", "chapter0"),
            scene_index=int(data.get("scene_index", 0)),
            flags=dict(data.get("flags", {})),
        )


@dataclass
class GameState:
    """Container holding the mutable game data for the current session."""

    player: Player
    progress: Progress = field(default_factory=Progress)
    created_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def new_game(cls, player_name: str) -> "GameState":
        """Factory that provisions a default player profile for a fresh run."""

        player = Player(
            name=player_name,
            level=1,
            basic_damage=15,
            basic_defense=3,
            max_hp=120,
            hp=120,
            exp=0,
            gold=0,
            inventory=[],
            sin_list=[],
        )
        return cls(player=player)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "player": self.player.to_dict(),
            "progress": self.progress.to_dict(),
            "created_at": self.created_at.isoformat(timespec="seconds"),
        }

    @classmethod
    def from_dict(
        cls, data: Dict[str, Any], *, item_loader: Optional[Any] = None
    ) -> "GameState":
        player = Player.from_dict(data["player"], item_loader=item_loader)
        progress = Progress.from_dict(data.get("progress", {}))
        created_raw = data.get("created_at")
        if created_raw:
            try:
                created_at = datetime.fromisoformat(created_raw)
            except ValueError:
                created_at = datetime.utcnow()
        else:
            created_at = datetime.utcnow()
        return cls(player=player, progress=progress, created_at=created_at)

    def advance_scene(self) -> None:
        self.progress.scene_index += 1

    def summary(self) -> str:
        """Return a short summary string for menus or save slots."""

        return f"Lv.{self.player.level} {self.player.name} - {self.progress.chapter_id}#{self.progress.scene_index}"
