from personnage.personnage import Personnage
import sys
sys.path.append("..")
from connexion import Connexion



class Monstre(Personnage):
    def __init__(self, classe, hp, degats):
        super().__init__(classe, hp, degats)

    @classmethod
    def chercher_monstre(cls):
        cursor = Connexion.connecter()
        query = "SELECT * FROM monstres ORDER BY RAND()"
        cursor.execute(query)
        result = cursor.fetchone()
        Connexion.deconnecter()

        if result:
                classe, hp, degats = result
                return cls(classe, hp, degats) 
        else:
            return None

        