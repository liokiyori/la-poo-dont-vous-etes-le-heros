class Personnage:

    def __init__(self, classe, hp, degats):
        self.__classe = classe
        self.__hp = hp
        self.__degats = degats

    def get_classe(self):
        return self.__classe
        
    def get_hp(self):
        return self.__hp
    
    def attaquer(self, cible):
        cible.subir_degats(self.__degats)

    def subir_degats(self, degats):
        self.__hp -= degats
        if self.__hp < 0:
            self.__hp = 0

    def ajouter_degats(self, bonus_degats):
        self.__degats += bonus_degats
    
    
    def combat(personnage, monstre):
        tour = 0
        while personnage.get_hp() > 0 and monstre.get_hp() > 0:
            tour += 1
            print(f"tour numéro {tour}")
            personnage.attaquer(monstre)
            if monstre.get_hp() > 0:
                monstre.attaquer(personnage)

            print(f"{type(personnage).__name__}: {personnage.get_hp()} HP, Monstre: {monstre.get_hp()} HP")

        if personnage.get_hp() > 0:
            print(f"{type(personnage).__name__} a gagné le combat !")
        else:
            print("Le monstre a gagné le combat !")

