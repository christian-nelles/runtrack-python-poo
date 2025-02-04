class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    def afficher_titre(self):
        return self.__titre

    def afficher_auteur(self):
        return self.__auteur

    def afficher_nombre_pages(self):
        return self.__nombre_pages

    def modifier_titre(self, titre):
        self.__titre = titre

    def modifier_auteur(self, auteur):
        self.__auteur = auteur

    def modifier_nombre_pages(self, nombre_pages):
        if nombre_pages >= 0 and nombre_pages == int(nombre_pages):
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif")

livre = Livre("Cuisiner un python", "John Doe", 50)
print("Titre :", livre.afficher_titre())
print("Auteur :", livre.afficher_auteur())
print("Nombre de pages :", livre.afficher_nombre_pages())
livre.modifier_nombre_pages(-50)
livre.modifier_nombre_pages(50.5)
print("Nombre de pages après les mauvaises modification :", livre.afficher_nombre_pages())
livre.modifier_nombre_pages(500)
livre.modifier_titre("Dormir sur un cactus")
livre.modifier_auteur("CactusMan")
print("Nouveau titre :", livre.afficher_titre())
print("Nouvel auteur :", livre.afficher_auteur())
print("Nouveau nombre de pages :", livre.afficher_nombre_pages())