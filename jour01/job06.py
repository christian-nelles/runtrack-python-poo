class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self):
        self.prenom = input("Entrer un nom : ")

animal = Animal(0, "")
animal.nommer()
print(f"L'animal se nomme {animal.prenom}")
print(f"L'age de l'animal {animal.age} ans")
animal.vieillir()
print(f"L'age de l'animal {animal.age} ans")