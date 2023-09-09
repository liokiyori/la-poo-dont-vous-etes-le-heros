
class Chest:
    def __init__(self, content):
        self.content = content  # L'objet dans le coffre (arme ou armure)

    def open_chest(self, player):
        # Afficher le contenu du coffre
        print(f"Vous avez trouvé un {self.content.name} dans le coffre!")

        # Demander au joueur s'il veut équiper l'objet
        choice = input("Voulez-vous équiper l'objet ? (Oui/Non) : ")
        if choice.lower() == "oui":
            player.equip_weapon(self.content)
            print(f"Vous avez équipé le {self.content.name}. Votre attaque augmente !")
            print(f"Votre attaque est désormais de : {player.damage}")
