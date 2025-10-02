import tkinter as tk
from configuration import FICHIER_CLASSEMENT

class Classement:
    """Classe pour gérer la fonctionnalité de classement.

    Attributs:
        nom_fichier (str): Le nom du fichier où les scores sont sauvegardés.
        scores (list): Une liste de tuples contenant les noms et scores.
        fenetre_classement (tk.Toplevel): La fenêtre de classement.
    """

    def __init__(self, nom_fichier="classement.txt"):
        """Initialise un objet Classement avec un nom de fichier donné.

        Args:
            nom_fichier (str): Le nom du fichier où les scores sont sauvegardés. Par défaut "classement.txt".
        """
        self.nom_fichier = nom_fichier
        self.scores = self.charger_scores()
        self.fenetre_classement = None

    def charger_scores(self):
        """Charge les scores à partir du fichier de classement.

        Cette méthode lit le fichier de classement spécifié par l'attribut
        `nom_fichier`, et extrait les scores sous forme de tuples (nom, score).
        Les scores sont triés par ordre décroissant et seules les dix meilleures
        entrées sont conservées.

        Returns:
            list: Une liste triée de tuples contenant les noms et scores. Si le
            fichier de classement n'existe pas, une liste vide est retournée.

        Exemple de contenu du fichier de classement:
            Le fichier `classement.txt` doit avoir le format suivant, avec chaque ligne
            contenant un nom et un score séparés par une virgule:

            John,100
            Alice,30
            Bob,50
            Eve,0
            Charlie,10

        Exemple de sortie:
            Si le fichier `classement.txt` contient les lignes ci-dessus, la méthode
            retournera:

            [('John', 100), ('Bob', 50), ('Alice', 30), ('Charlie', 10), ('Eve', 0)]
        """
        self.scores = []

        if not FICHIER_CLASSEMENT:
            return self.scores

        with open(self.nom_fichier, 'r') as fichier:
            txt = fichier.readlines()
        for ligne in txt:
            if "," in ligne:
                nom, score = ligne.strip().split(",")
                self.scores.append((nom.strip(), int(score.strip())))

        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)
        return self.scores[:10]


    def enregistrer_score(self, nom, score):
        """Enregistre un nouveau score dans le classement.

        Args:
            nom (str): Le nom du joueur.
            score (int): Le score du joueur.
        """
        self.scores.append((nom, score))
        # Tri des scores par ordre décroissant et on conserve que les 10 meilleurs scores
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:10]
        with open(self.nom_fichier, "a") as f:
            f.write(f"{nom},{score}\n")

    def afficher(self):
        """Affiche la fenêtre du classement avec les 10 meilleurs scores."""
        # Vérifie si la fenêtre de classement existe et est ouverte
        if (
            self.fenetre_classement is not None
            and self.fenetre_classement.winfo_exists()
        ):
            self.fenetre_classement.lift()  # Ramener la fenêtre au premier plan
            return

        self.fenetre_classement = tk.Toplevel()  # Création d'une nouvelle fenêtre
        self.fenetre_classement.geometry("300x300")
        self.fenetre_classement.title("Classement")
        tk.Label(
            self.fenetre_classement,
            text="Les 10 meilleurs scores",
            font=("Helvetica", 16),
        ).pack(anchor=tk.W, padx=10, pady=10)

        if self.scores:
            i = 1
            for nom, score in self.scores:
                txt_scores = f"{i}. {nom}: {score}"
                tk.Label(
                    self.fenetre_classement,
                    text=txt_scores,
                    font=("Helvetica", 11),
                ).pack(anchor=tk.W, padx=10, pady=1)
                i += 1
        else:
            tk.Label(
                self.fenetre_classement,
                text="-- Aucun score enregistré pour l'instant --",
                font=("Helvetica", 11),
            ).pack(anchor=tk.W, padx=10, pady=12)
