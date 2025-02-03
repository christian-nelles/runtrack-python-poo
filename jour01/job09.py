class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        return f"""Produit : {self.nom}
PrixHT : {self.prixHT}
TVA : {self.TVA}
PrixTTC : {self.CalculerPrixTTC()}
"""
        
    def ModifierLeNom(self):
        self.nom = input(f"Entrez nouveau nom pour {self.nom} : ")
        
    def ModifierLePrix(self):
        self.prixHT = float(input(f"Entrez nouveau prix pour {self.nom} : "))
        self.TVA = self.prixHT * 0.2
    
produit1 = Produit("Ordinateur", 1000, 1000 * 0.2)
produit2 = Produit("Téléphone", 500, 500 * 0.2)
produit1.CalculerPrixTTC()
produit2.CalculerPrixTTC
print(produit1.afficher())
print(produit2.afficher())
produit1.ModifierLeNom()
produit2.ModifierLePrix()
produit2.CalculerPrixTTC()
print(produit1.afficher())
print(produit2.afficher())
