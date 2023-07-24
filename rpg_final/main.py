from personnage.personnage import Personnage
from personnage.guerrier import Guerrier
from personnage.archer import Archer
from personnage.assassin import Assassin
from personnage.monstres import Monstre
from donjon import Donjon
from coffre import Coffre
from hug import repondre

def main():
    print(repondre())

    print("Choisissez votre classe : [c]hasseur, [g]uerrier ou [a]ssassin")
    choix_classe = input().lower()
    
    if choix_classe == 'c':
        hero = Archer()
    elif choix_classe == 'g':
        hero = Guerrier()
    elif choix_classe == 'a':
        hero = Assassin()
    else:
        print("Classe invalide. Vous serez un Archer par défaut.")
        hero = Archer()

    print("Vous pénétrez dans un sombre donjon...\n")
    nombre = int(input("Choisissez votre nombre de salle : "))
    donjon = Donjon(nombre)
    donjon.generer_salles()
    donjon = donjon.salles_donjon

    for i, type in enumerate(donjon, start=1):
        print(f"\nVous entrez dans la salle {i}...")
        direction = input("Dans quelle direction souhaitez-vous aller ? (g/d): ").lower()
        if direction == "g":
            print("vous allez à gauche")
        elif direction == "d":
            print("vous allez à droite")
        
        salles(hero, type)

        if hero.get_hp() <= 0:
            print("Game over!")
            break

        if type == 3:  
            print("Et non, y'a pas de boss en fait, c'est fini, bien joué")
            break



def salles(hero, type):
    if type == 1:  # salle de monstre
        monstre = Monstre.chercher_monstre()
        print(f"Un {monstre.get_classe()} apparait! Preparez_vous au combat")
        hero.combat(monstre)
    elif type == 2:  # salle de coffre
        coffre = Coffre()
        coffre.ouvrir(hero)


        


    
    





def combat_room(personnage, room_type):
    if room_type == 1:  # Monster room
        monstre = Monstre.chercher_monstre()
        print(f"A wild {monstre.get_classe()} appeared! Prepare for combat!")
        personnage.combat(monstre)
    elif room_type == 2:  # Chest room
        coffre = Coffre()
        coffre.ouvrir(personnage)

if __name__ == '__main__':
    main()