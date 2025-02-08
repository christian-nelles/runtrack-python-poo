class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes = 0
        self.__jaunes = 0
        self.__rouges = 0

    def marquerUnBut(self):
        self.__buts += 1
        print(f"{self.__nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        self.__passes += 1
        print(f"{self.__nom} a effectué une passe décisive !")

    def recevoirUnCartonJaune(self):
        self.__jaunes += 1
        print(f"{self.__nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.__rouges += 1
        print(f"{self.__nom} a reçu un carton rouge !")

    def afficherStatistiques(self):
        print(f"{self.__nom} (#{self.__numero}, {self.__position}) - {self.__buts} buts, {self.__passes} passes, {self.__jaunes} jaunes, {self.__rouges} rouges.")

    def getNom(self):
        return self.__nom


class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)
        print(f"{joueur.getNom()} a rejoint l'équipe {self.__nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques de l'équipe {self.__nom} :")
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.__joueurs:
            if joueur.getNom() == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()

messi = Joueur("Lionel Messi", 10, "Attaquant")
mbappe = Joueur("Kylian Mbappé", 7, "Attaquant")
kante = Joueur("N'Golo Kanté", 6, "Milieu")
psg = Equipe("PSG")
psg.ajouterJoueur(messi)
psg.ajouterJoueur(mbappe)
psg.ajouterJoueur(kante)
psg.afficherStatistiquesJoueurs()
psg.mettreAJourStatistiquesJoueur("Lionel Messi", "but")
psg.mettreAJourStatistiquesJoueur("Kylian Mbappé", "passe")
psg.mettreAJourStatistiquesJoueur("N'Golo Kanté", "jaune")
psg.afficherStatistiquesJoueurs()