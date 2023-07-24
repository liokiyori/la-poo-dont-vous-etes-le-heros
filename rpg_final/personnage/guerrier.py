from personnage.personnage import Personnage

class Guerrier(Personnage) :
    
    def __init__(self):
        super().__init__("guerrier",100,10)