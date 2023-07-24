import random

class Donjon:
    def __init__(self, nombre_salle):
        self.nombre_salle = nombre_salle
        self.salles_donjon = []
    
    @classmethod
    def generer_donjon(cls, nombre_salle):
        # Génère une liste de salles (1: monstre, 2: coffre, 3: boss)
        nombre_salle = int(nombre_salle)
        salles_donjon = [random.choice([1, 2]) for i in range(nombre_salle - 1)]
        random.shuffle(salles_donjon)
        salles_donjon.append(3)  # The last room is the boss room
        return salles_donjon

    def generer_salles(self):
        self.salles_donjon = self.generer_donjon(self.nombre_salle)


