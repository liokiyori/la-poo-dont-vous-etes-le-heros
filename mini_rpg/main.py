from characters.warrior import Warrior
from characters.assassin import Assassin
from characters.hunter import Hunter
from utils.menu import Menu
from rooms.dungeon import Dungeon
from utils.huggingchat import repondre

def main():
    print("Bienvenue dans le Mini RPG !")
    print(repondre())
    name = input("Entrez votre nom : ")

    class_type = Menu.choose_class()

    if class_type == "Guerrier":
        player = Warrior(name)
    elif class_type == "Assassin":
        player = Assassin(name)
    elif class_type == "Chasseur":
        player = Hunter(name)
    else:
        player = Warrior(name)

    print(f"Bienvenue, {player.name} le {player.class_type} !")

    difficulty = int(input("Choisissez la difficulté (nombre de salles min : 6) : "))
    if difficulty < 6 :
        difficulty = 25
        print("c'est pas beau de vouloir tricher, alors tu va avoir le droit a 25 salles")
    dungeon = Dungeon(difficulty)
    dungeon.generate_rooms()

    for i, room in enumerate(dungeon.rooms):
        print(f"Vous êtes dans la salle {i+1}.")

        if i == dungeon :
            print(f"Le {room.monster.name} apparaît !!!")

        if room.monster:
            print(f"Un {room.monster.name} apparaît !")
            while room.monster.health > 0 and player.health > 0:
                print(f"{player.name} (Santé: {player.health})")
                print(f"{room.monster.name} (Santé: {room.monster.health})")
        
                action = Menu.choose_action()

                if action == "Taper":
                    player.attack(room.monster)
                    print(f"Vous attaquez le {room.monster.name} !")
                    room.monster.attack(player)
                elif action == "Soigner":
                    player.heal()
                    print(f"Vous vous soignez de {player.healing_power} points de vie.")
                    room.monster.attack(player)

                if player.health <= 0:
                    print("Vous êtes mort. Game Over.")
                    break
                elif room.monster.health <= 0:
                    print(f"Vous avez vaincu le {room.monster.name} !")

        if room.chest:
            print("Vous avez trouvé un coffre dans cette salle.")
            choice = input("Voulez-vous ouvrir le coffre ? (Oui/Non) : ")
            if choice.lower() == "oui":
                room.chest.open_chest(player)

        if i < len(dungeon.rooms) - 1:
            direction = Menu.choose_direction()
            print(f"Vous choisissez de vous diriger vers le {direction}.")
            print("Vous entrez dans la salle suivante.\n")
main()