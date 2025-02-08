class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = False

    def marquerCommeFinie(self):
        self.__statut = True

    def getTitre(self):
        return self.__titre

    def getStatut(self):
        return self.__statut

    def afficher(self):
        statut = "Terminé" if self.__statut else "À faire"
        return f"{self.__titre} - {self.__description} [{statut}]"

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache):
        self.__taches.append(tache)
        print(f"Tâche '{tache.getTitre()}' ajoutée.")

    def supprimerTache(self, titre):
        self.__taches = [t for t in self.__taches if t.getTitre() != titre]
        print(f"Tâche '{titre}' supprimée.")

    def marquerCommeFinie(self, titre):
        for t in self.__taches:
            if t.getTitre() == titre:
                t.marquerCommeFinie()
                print(f"Tâche '{titre}' marquée comme terminée.")

    def afficherListe(self):
        print("\nListe des tâches :")
        for t in self.__taches:
            print(t.afficher())

    def filterListe(self, statut):
        filtres = [t.afficher() for t in self.__taches if t.getStatut() == statut]
        print("\nTâches filtrées :")
        for t in filtres:
            print(t)

todo = ListeDeTaches()
tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
tache2 = Tache("Réviser Python", "Pratiquer la POO")
tache3 = Tache("Sport", "Aller courir 30 minutes")
todo.ajouterTache(tache1)
todo.ajouterTache(tache2)
todo.ajouterTache(tache3)
todo.afficherListe()
todo.marquerCommeFinie("Réviser Python")
todo.afficherListe()
todo.filterListe(False)
todo.supprimerTache("Sport")
todo.afficherListe()