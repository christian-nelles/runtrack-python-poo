import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def points(self):
        if self.valeur in ["J", "Q", "K"]:
            return 10
        elif self.valeur == "A":
            return 11
        else:
            return int(self.valeur)

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    couleurs = ["coeur", "Carreau", "Trèfle", "Pique"]

    def __init__(self):
        self.paquet = [Carte(val, coul) for val in self.valeurs for coul in self.couleurs]
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop() if self.paquet else None

jeu = Jeu()
main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

print("Main du joueur:", ", ".join(str(carte) for carte in main_joueur))
print("Main du croupier:", str(main_croupier[0]), "et une carte cachée")

def calculer_score(main):
    score = sum(carte.points() for carte in main)
    as_count = sum(1 for carte in main if carte.valeur == "A")
    
    while score > 21 and as_count:
        score -= 10
        as_count -= 1
    
    return score

score_joueur = calculer_score(main_joueur)
print("Score du joueur :", score_joueur)