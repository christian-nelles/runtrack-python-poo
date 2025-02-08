class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"""\nMarque = {self.marque}
Modèle = {self.modele}
Année = {self.annee}
Prix = {self.prix}""")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("La voiture démarre : Vroum Vroum !")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roue}")

    def demarrer(self):
        print("La moto démarre : Vrrroooom !")

voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
voiture.informationsVehicule()
voiture.demarrer()
moto.informationsVehicule()
moto.demarrer()