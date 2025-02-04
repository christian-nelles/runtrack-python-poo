class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, nom, prix):
        if prix > 0:
            self.__plats[nom] = prix
        else:
            print("C'est jamais gratuit(surtout en France)")

    def annuler_commande(self):
        self.__statut = "annulée"
        print("Commande annulée.")

    def __calculer_total(self):
        return sum(self.__plats.values())

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut : {self.__statut}")
        for plat, prix in self.__plats.items():
            print(f"- {plat} : {prix}€")
        print(f"Total : {self.__calculer_total()}€")

    def calculer_TVA(self):
        return self.__calculer_total() * (20 / 100)

commande = Commande(101)
commande.ajouter_plat("Pizza", 12)
commande.ajouter_plat("Salade", 8)
commande.afficher_commande()
print("TVA :", commande.calculer_TVA(), "€")
commande.annuler_commande()
commande.afficher_commande()