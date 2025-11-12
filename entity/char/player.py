"""Player entity definition."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

import entity.material as material
from entity.char.character import Character


class Player(Character):  # TODO: 나중에 body클래스로 부위별 상태 추가
    """Player controlled character with inventory and progression helpers."""

    def __init__(
        self,
        name: str,
        level: int,
        basic_damage: int,
        basic_defense: int,
        max_hp: int,
        hp: int,
        exp: int,
        gold: int,
        inventory: Optional[Iterable[Any]] = None,
        sin_list: Optional[Iterable[Any]] = None,
    ) -> None:
        super().__init__(name, level, basic_damage, basic_defense, hp, list(inventory or []))
        self.exp = exp
        self.max_hp = max_hp
        self.gold = gold
        self.sin_list = list(sin_list or [])

    def level_up(self) -> str:
        self.level += 1
        self.basic_damage += 5
        self.max_hp += 20
        return f"{self.name} 레벨업, 현재레벨: {self.level}"

    def get_item(self, item: Any) -> None:
        if isinstance(item, list):
            self.inventory.extend(item)
        else:
            self.inventory.append(item)

    def use_item(self, item: Any) -> None:  # TODO: 아이템 효과 추가
        if item in self.inventory:
            self.inventory.remove(item)

    def show_status(self) -> str:
        status = super().show_status()
        status += f"HP: {self.hp}/{self.max_hp}\nEXP: {self.exp}/{100 * self.level}\nGold: {self.gold}\n"
        return status

    def show_inventory(self) -> str:  # TODO: 아이템 상세정보, 여러개면 갯수 나타내서 간략화, 아이템 사용 등 추가
        inventory_info = "inventory:\n"
        counts: Dict[str, int] = {}
        descriptions: Dict[str, str] = {}
        for item in self.inventory:
            name, thing_type, rarity = self._describe_item(item)
            key = f"{name}|{thing_type}|{rarity}"
            counts[key] = counts.get(key, 0) + 1
            descriptions[key] = f"- {name} ({thing_type}, {rarity})"
        for key, base in descriptions.items():
            inventory_info += f"{base} x {counts[key]}\n"
        return inventory_info

    @staticmethod
    def _describe_item(item: Any) -> tuple[str, str, str]:
        if hasattr(item, "name"):
            name = item.name
            thing_type = getattr(getattr(item, "thing_type", ""), "value", str(getattr(item, "thing_type", "")))
            rarity = getattr(getattr(item, "rarity", ""), "value", str(getattr(item, "rarity", "")))
        elif isinstance(item, dict):
            name = str(item.get("name", "Unknown"))
            thing_type = str(item.get("thing_type", ""))
            rarity = str(item.get("rarity", ""))
        else:
            name = str(item)
            thing_type = ""
            rarity = ""
        return name, thing_type, rarity

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "level": self.level,
            "basic_damage": self.basic_damage,
            "basic_defense": self.basic_defense,
            "max_hp": self.max_hp,
            "hp": self.hp,
            "exp": self.exp,
            "gold": self.gold,
            "inventory": [self._item_to_dict(item) for item in self.inventory],
            "sin_list": [self._serialize_sin(sin) for sin in self.sin_list],
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
        *,
        item_loader: Optional[Any] = None,
    ) -> "Player":
        inventory_data = data.get("inventory", [])
        if item_loader is not None:
            inventory = [item_loader(entry) for entry in inventory_data]
        else:
            inventory = inventory_data
        sin_entries = [cls._deserialize_sin(entry) for entry in data.get("sin_list", [])]
        return cls(
            name=data["name"],
            level=int(data.get("level", 1)),
            basic_damage=int(data.get("basic_damage", 0)),
            basic_defense=int(data.get("basic_defense", 0)),
            max_hp=int(data.get("max_hp", 0)),
            hp=int(data.get("hp", 0)),
            exp=int(data.get("exp", 0)),
            gold=int(data.get("gold", 0)),
            inventory=inventory,
            sin_list=sin_entries,
        )

    @staticmethod
    def _item_to_dict(item: Any) -> Dict[str, Any]:
        if isinstance(item, dict):
            return dict(item)
        payload = {"name": getattr(item, "name", "Unknown")}
        thing_type = getattr(item, "thing_type", None)
        rarity = getattr(item, "rarity", None)
        if thing_type is not None:
            payload["thing_type"] = getattr(thing_type, "value", str(thing_type))
        if rarity is not None:
            payload["rarity"] = getattr(rarity, "value", str(rarity))
        heal_amount = getattr(item, "heal_amount", None)
        if heal_amount is not None:
            payload["heal_amount"] = heal_amount
        return payload

    @staticmethod
    def _serialize_sin(sin: Any) -> str:
        if isinstance(sin, material.Sin):
            return sin.name
        return str(sin)

    @staticmethod
    def _deserialize_sin(raw: Any) -> Any:
        if isinstance(raw, str):
            try:
                return material.Sin[raw]
            except KeyError:
                return raw
        return raw
