class Menu:
    @staticmethod
    def choose_class():
        print("Choisissez votre classe :")
        print("1. Guerrier")
        print("2. Assassin")
        print("3. Chasseur")

        choice = int(input("Entrez le numéro de votre classe : "))
        if choice == 1:
            return "Guerrier"
        elif choice == 2:
            return "Assassin"
        elif choice == 3:
            return "Chasseur"
        else:
            return "Guerrier"  # Default to Guerrier if an invalid choice is entered

    @staticmethod
    def choose_action():
        print("Choisissez une action :")
        print("1. Taper")
        print("2. Soigner")

        choice = int(input("Entrez le numéro de votre action : "))
        if choice == 1:
            return "Taper"
        elif choice == 2:
            return "Soigner"
        else:
            return "Taper"  # Default to Taper if an invalid choice is entered

    @staticmethod
    def choose_direction():
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Sud")
        print("3. Est")
        print("4. Ouest")

        choice = int(input("Entrez le numéro de votre direction : "))
        if choice == 1:
            return "Nord"
        elif choice == 2:
            return "Sud"
        elif choice == 3:
            return "Est"
        elif choice == 4:
            return "Ouest"
        else:
            return "Nord" 
