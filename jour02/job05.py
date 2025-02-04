class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture marche")
        else:
            print("Plus de reservoir")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée")

    def __verifier_plein(self):
        return self.__reservoir

voiture = Voiture("Fiat", "Multipla", 1998, 300000)
voiture.demarrer()
voiture.arreter()