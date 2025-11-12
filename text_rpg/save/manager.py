"""Save file utilities."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from text_rpg.state import GameState


class SaveManager:
    """Handle serialization of :class:`~text_rpg.state.GameState` objects."""

    def __init__(self, base_dir: Path | str = Path("saves")) -> None:
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _path_for(self, slot: int) -> Path:
        return self.base_dir / f"slot_{slot}.json"

    def save(self, state: GameState, *, slot: int = 1) -> Path:
        payload = state.to_dict()
        payload["slot"] = slot
        payload["timestamp"] = datetime.utcnow().isoformat(timespec="seconds")
        payload["summary"] = state.summary()
        path = self._path_for(slot)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
        return path

    def load(self, slot: int = 1) -> GameState:
        path = self._path_for(slot)
        if not path.exists():
            raise FileNotFoundError(f"Save slot {slot} is empty")
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return GameState.from_dict(payload, item_loader=self._load_inventory_item)

    def available_slots(self) -> List[Dict[str, Any]]:
        slots: List[Dict[str, Any]] = []
        for path in sorted(self.base_dir.glob("slot_*.json")):
            try:
                slot = int(path.stem.split("_")[1])
            except (IndexError, ValueError):
                continue
            with path.open("r", encoding="utf-8") as handle:
                payload = json.load(handle)
            slots.append(
                {
                    "slot": slot,
                    "timestamp": payload.get("timestamp", ""),
                    "summary": payload.get("summary", ""),
                }
            )
        return slots

    def autosave(self, state: GameState) -> None:
        self.save(state, slot=state.progress.scene_index + 1)

    @staticmethod
    def _load_inventory_item(data: Dict[str, Any]) -> Dict[str, Any]:
        """Return a lightweight dictionary for inventory entries."""

        return dict(data)
