class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def getNom(self):
        return self.__nom

    def getNombreHabitants(self):
        return self.__nombre_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville._Ville__nombre_habitants += 1

paris = Ville("Paris", 1_000_000)
marseille = Ville("Marseille", 861_635)
print(f"Population de la ville de {paris.getNom()} : {paris.getNombreHabitants()}")
print(f"Population de la ville de {marseille.getNom()} : {marseille.getNombreHabitants()}")
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
print(f"Mise à jour de la population de la ville de {paris.getNom()} : {paris.getNombreHabitants()}")
print(f"Mise à jour de la population de la ville de {marseille.getNom()} : {marseille.getNombreHabitants()}")