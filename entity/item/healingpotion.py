from entity.item.potion import Potion
import entity.material as material

class HealingPotion(Potion):
    def __init__(self, name, heal_amount, thing_type: material.Things.POTION, potion_type: material.PotionType.HEALING, rarity: material.Rarity):
        super().__init__(name, thing_type, rarity, potion_type)
        self.heal_amount = heal_amount

    def use(self, user):
        user.hp += self.heal_amount
        user.use_item(self)

HealingPotion1 = HealingPotion("Small Healing Potion",  heal_amount=30, thing_type=material.Things.POTION, potion_type=material.PotionType.HEALING, rarity=material.Rarity.COMMON)
