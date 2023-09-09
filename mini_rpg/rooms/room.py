from random import randint
from items.chest import Chest
from connection_db_data.data import Data
class Room:
    directions = ["north", "south", "east", "west"]

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.monster = None
        self.chest = None

    def generate_content(self):
        salle = randint(0,3)
        if salle in [0,1,3] :
            mob = Data()
            id_mob = randint(1,6)
            mono = mob.get_monster_id(id_mob)
            self.monster = mono
        if salle == 2 :
            arme = Data()
            id_arme = randint(1,8)
            arme_choi = arme.get_arme_id(id_arme)
            self.chest = Chest(arme_choi)
