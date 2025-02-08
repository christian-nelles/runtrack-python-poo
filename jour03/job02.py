class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__num_compte} - Titulaire : {self.__prenom} {self.__nom} - Solde : {self.__solde}€")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde}€")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}€ effectué. solde : {self.__solde}€")
        else:
            print("Erreur : le montant doit être positif")

    def retrait(self, montant):
        if montant > 0:
            if self.__solde - montant >= 0:
                self.__solde -= montant
                print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€")
            else:
                print("Fonds insuffisants")
        else:
            print("Erreur : le montant doit être positif")

    def agios(self):
        if self.__solde < 0:
            frais = self.__solde * 0.05
            self.__solde += frais
            print(f"Agios appliqués : {frais}€. Nouveau solde : {self.__solde}€")

    def virement(self, compte_dest, montant):
        if montant > 0 and (self.__solde - montant >= 0):
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant}€ vers le compte {compte_dest.__num_compte} réussi")
        else:
            print("Virement impossible : solde insuffisant")

compte1 = CompteBancaire("1", "Doe", "John", 500, False)
compte2 = CompteBancaire("2", "Dupont", "Alice", -100, True)
compte1.afficher()
compte1.versement(200)
compte1.retrait(100)
compte2.afficher()
compte2.agios()
compte1.virement(compte2, 300)
compte1.afficherSolde()
compte2.afficherSolde()
