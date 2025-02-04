class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def afficher_longueur(self):
        return self.__longueur

    def afficher_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle = Rectangle(10, 5)
print("Longueur :", rectangle.afficher_longueur())
print("Largeur :", rectangle.afficher_largeur())
rectangle.set_longueur(20)
rectangle.set_largeur(10)
print("Nouvelle longueur :", rectangle.afficher_longueur())
print("Nouvelle largeur :", rectangle.afficher_largeur())