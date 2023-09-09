from characters.character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "Guerrier")
        self.damage = 25
        self.health =200
        self.healing_power = 40
