from personnage.personnage import Personnage

class Boss(Personnage) :
    
    def __init__(self):
        super().__init__("boss",70,10)