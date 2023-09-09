from characters.character import Character

class Assassin(Character):
    def __init__(self, name):
        super().__init__(name, "Assassin")
        self.damage = 12
        self.healing_power = 15
