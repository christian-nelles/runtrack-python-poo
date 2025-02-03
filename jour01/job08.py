import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self):
        self.rayon = 7

    def afficherInfos(self):
        print(f"""Rayon : {self.rayon}
Diametre : {cercle.diametre()}
Circonference : {cercle.circonference()}
Aire : {cercle.aire()}""")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle = Cercle(4)
cercle.afficherInfos()
cercle.changerRayon()
cercle.afficherInfos()