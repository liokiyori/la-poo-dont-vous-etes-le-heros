from connection_db_data.connexion import Connexion
from monsters.monster import Monster
from items.weapon import Weapon

class Data:
    def get_monster_id(self, id):
        cursor = Connexion.connecter()

        query = "SELECT classe, pv, attaque FROM monstres WHERE id = %s"
        cursor.execute(query, (id,))

        monstre_choisi = cursor.fetchone()

        if monstre_choisi is not None:
            quoi = Monster(monstre_choisi[0], monstre_choisi[1], monstre_choisi[2])

        Connexion.deconnecter()

        return quoi

    def get_arme_id(self, id) :
        cursor = Connexion.connecter()

        query = "SELECT nom, atk FROM arme_amelioree WHERE id = %s"
        cursor.execute(query,(id,))

        arme_choisi = cursor.fetchone()
        
        army = None

        if arme_choisi is not None :
            army = Weapon(arme_choisi[0], arme_choisi[1])

        Connexion.deconnecter()

        return army