class Coffre:
    def __init__(self):
        pass

    def ouvrir(self, personnage):
        personnage.ajouter_degats(5)
        print(f"{type(personnage).__name__} a ouvert le coffre et gagne +5 dégats!")