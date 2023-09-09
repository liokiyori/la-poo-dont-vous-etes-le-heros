from characters.character import Character

class Hunter(Character):
    def __init__(self, name):
        super().__init__(name, "Chasseur")
        self.damage = 13