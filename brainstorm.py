# 1. LES CLASSES

def partie_classes():
    class Personne:
        def __init__(self, nom):
            self.nom = nom  # attribut de l'objet

        def afficher_details(self):
            print(f"Nom: {self.nom}")

    # Création d'un objet (une instance de la classe Personne)
    p = Personne("Alice")
    p.afficher_details()  # Affiche "Nom: Alice"



# 2. L'ENCAPSULATION-ABSTRACTION

def partie_encapsulation_abstraction():
    class Personne:
        def __init__(self, nom, age):
            self.__nom = nom  # Encapsulation de l'attribut
            self.__age = age  # Encapsulation de l'attribut

        def afficher_details(self):  # Interface publique
            print(f"Nom: {self.__nom}, Âge: {self.__age}")

        def set_age(self, age):  # Setter pour contrôler l'accès à l'âge
            if age > 0:
                self.__age = age
            else:
                print("L'âge doit être positif.")

    p = Personne("Alice", 30)
    p.afficher_details()  # Affiche "Nom: Alice, Âge: 30"
    p.set_age(-5)  # Tentative d'accès indirect à un attribut privé (contrôlé)
    p.set_age(35)
    p.afficher_details()  # Affiche "Nom: Alice, Âge: 35"



# 3. LE PASSAGE PAR REFERENCE

def partie_passage_par_reference():
    class Personne:
        def __init__(self, nom):
            self.nom = nom

        def changer_nom(self, nouveau_nom):
            self.nom = nouveau_nom  # Modification de l'attribut de l'objet

    def changer_nom_personne(nouveau):
        nouveau.changer_nom("Bob")  # Modification de l'objet passé en argument

    p = Personne("Alice")
    print(p.nom)  # Affiche "Alice"
    changer_nom_personne(p)  # Passe p par référence et modifie l'objet
    print(p.nom)  # Affiche "Bob"



# 4. L'HERITAGE

def partie_heritage():
    class Personne:
        def __init__(self, nom):
            self.nom = nom
            
        def afficher_details(self):
            print(f"Nom: {self.nom}")

    class Employe(Personne):  # Employe hérite de Personne
        def __init__(self, nom, job):
            super().__init__(nom)  # Appel du constructeur de la classe parente
            self.job = job

        def afficher_profession(self):  # Surcharge de la méthode de la classe parente
            print(f"Job: {self.job}")

    # Création d'un objet Personne
    p = Personne("Marc")
    p.afficher_details()
    # p.afficher_profession() # Ne pourra pas l'initier
    # Création d'un objet Employe
    e = Employe("Alice", "Développeur")
    e.afficher_details() 
    e.afficher_profession() 




partie_classes()  # Exécute la partie sur les classes
print("-----")
partie_encapsulation_abstraction()  # Exécute la partie sur l'encapsulation-abstraction
print("-----")
partie_passage_par_reference()  # Exécute la partie sur le passage par référence
print("-----")
partie_heritage()  # Exécute la partie sur l'héritage