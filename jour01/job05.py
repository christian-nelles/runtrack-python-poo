class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"le point se trouve en {self.x}, {self.y}")

    def afficherX(self):
        print(f"le point a {self.x} en abscisse")

    def afficherY(self):
        print(f"le point a {self.y} en ordonnee ")

    def changerX(self, nouveauX):
        self.x = nouveauX

    def changerY(self, nouveauY):
        self.y = nouveauY

point = Point(1, 2)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(3)
point.changerY(4)
point.afficherLesPoints()
point.afficherX()
point.afficherY()