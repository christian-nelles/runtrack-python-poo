class Part:
    def __init__(self, name, material):
        """Initialise une pièce avec un nom et un matériau."""
        self.name = name
        self.material = material

    def change_material(self, new_material):
        """Change le matériau de la pièce."""
        self.material = new_material

    def __str__(self):
        """Retourne une description de la pièce."""
        return f"{self.name} en {self.material}"

class Ship:
    def __init__(self, name):
        """Initialise un bateau avec un nom et un dictionnaire de pièces."""
        self.name = name
        self.__parts = {
            "Mat": Part("Mat", "Bois"),
            "Coque": Part("Coque", "Acier"),
            "Voile": Part("Voile", "Coton")
        }
        self.history = []

    def display_state(self):
        """Affiche l'état actuel du bateau."""
        print(f"\nÉtat actuel du bateau {self.name}:")
        for part in self.__parts.values():
            print(f"  - {part}")

    def replace_part(self, part_name, new_part):
        """Remplace une pièce existante par une nouvelle."""
        if part_name in self.__parts:
            old_part = self.__parts[part_name]
            self.__parts[part_name] = new_part
            self.history.append(f"Remplacement de {old_part} par {new_part}")
            print(f"{part_name} remplacé par {new_part}")
        else:
            print(f"Erreur : la pièce '{part_name}' n'existe pas.")

    def change_part(self, part_name, new_material):
        """Modifie directement le matériau d'une pièce existante."""
        if part_name in self.__parts:
            part = self.__parts[part_name]
            old_material = part.material
            part.change_material(new_material)
            self.history.append(f"Modification de {part_name}: {old_material} → {new_material}")
            print(f"Matériau de {part_name} changé en {new_material}")
        else:
            print(f"Erreur : la pièce '{part_name}' n'existe pas.")

    def display_history(self):
        """Affiche l'historique des modifications."""
        print("\nHistorique des modifications:")
        for change in self.history:
            print(f"  - {change}")

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        """Initialise un bateau de course avec une vitesse maximale."""
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        """Affiche la vitesse maximale du bateau."""
        print(f"\nLa vitesse maximale du {self.name} est de {self.max_speed} nœuds.")

def interactive_menu():
    """Menu interactif pour gérer le bateau."""
    ship = Ship("Thésée")
    
    while True:
        print("\nCHOIX")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Changer le matériau d'une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == "1":
            ship.display_state()
        elif choice == "2":
            part_name = input("Nom de la pièce à remplacer: ").capitalize()
            new_material = input("Matériau de la nouvelle pièce: ").capitalize()
            new_part = Part(part_name, new_material)
            ship.replace_part(part_name, new_part)
        elif choice == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            ship.change_part(part_name, new_material)
        elif choice == "4":
            ship.display_history()
        elif choice == "5":
            print("Fermeture du programme.")
            break
        else:
            print("Option invalide, essayez encore.")

interactive_menu()