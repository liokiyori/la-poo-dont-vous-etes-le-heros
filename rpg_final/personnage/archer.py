from personnage.personnage import Personnage

class Archer(Personnage) :
    
    def __init__(self):
        super().__init__("archer",90,15)