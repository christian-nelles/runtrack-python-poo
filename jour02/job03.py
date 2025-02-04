class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté")
        else:
            print("Le livre est deja emprunté")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu")
        else:
            print("Le livre est deja rendu")

livre = Livre("C'est qui Pascal ?", "John Doe", 50)
livre.emprunter()
livre.emprunter()
livre.rendre()
livre.rendre()