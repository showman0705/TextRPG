import entity.material as material

class Item():  
    def __init__(self, name: str, thing_type: material.Things, rarity: material.Rarity):
        self.name = name
        self.thing_type = thing_type
        self.rarity = rarity