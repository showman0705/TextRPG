from entity.item.item import Item
import material

class Potion(Item):
    def __init__(self, name, thing_type: material.Things.POTION, rarity: material.Rarity, potion_type: material.PotionType):
        super().__init__(name, thing_type, rarity)
        self.potion_type =potion_type