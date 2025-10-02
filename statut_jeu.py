import tkinter as tk


class StatutJeu:
    """Classe pour gérer le statut du jeu.

    Attributs:
        score (int): Le score actuel du joueur.
        niveau (int): Le niveau actuel du jeu.
        tentatives_restantes (int): Le nombre de tentatives restantes.
        statut_frame (tk.Frame): Le cadre contenant les informations de statut du jeu.
        score_label (tk.Label): L'étiquette pour afficher le score.
        niveau_label (tk.Label): L'étiquette pour afficher le niveau.
        tentatives_restantes_label (tk.Label): L'étiquette pour afficher les tentatives restantes.
    """

    def __init__(self, parent_frame, score, niveau, tentatives):
        """Initialise un objet StatutJeu avec les paramètres donnés.

        Args:
            parent_frame (tk.Frame): Le cadre parent pour le statut du jeu.
            score (int): Le score actuel du joueur.
            niveau (int): Le niveau actuel du jeu.
            tentatives (int): Le nombre de tentatives restantes.
        """
        self.score = score
        self.niveau = niveau
        self.tentatives_restantes = tentatives

        self.statut_frame = tk.Frame(parent_frame, bg="#4682B4")
        self.statut_frame.pack(
            side=tk.LEFT, padx=10, pady=5
        )  # Création du cadre pour le statut

        self.score_label = tk.Label(
            self.statut_frame,
            text=f"Score: {self.score}",
            font=("Helvetica", 12),
            bg="#4682B4",
            fg="white",
        )
        self.score_label.pack(side=tk.RIGHT, padx=10, pady=5)

        self.niveau_label = tk.Label(
            self.statut_frame,
            text=f"Niveau: {self.niveau}",
            font=("Helvetica", 12),
            bg="#4682B4",
            fg="white",
        )
        self.niveau_label.pack(side=tk.RIGHT, padx=10, pady=5)

        self.tentatives_restantes_label = tk.Label(
            self.statut_frame,
            text=f"Tentatives restantes: {self.tentatives_restantes}",
            font=("Helvetica", 12),
            bg="#4682B4",
            fg="white",
        )
        self.tentatives_restantes_label.pack(side=tk.RIGHT, padx=10, pady=5)

    def mettre_a_jour_score(self, score):
        """Met à jour l'étiquette du score.

        Args:
            score (int): Le nouveau score à afficher.
        """
        self.score = score
        self.score_label.config(text=f"Score: {self.score}")


    def mettre_a_jour_tentatives_restantes(self, tentatives):
        """Met à jour l'étiquette des tentatives restantes.

        Args:
            tentatives (int): Le nombre de tentatives restantes à afficher.
        """

        self.tentatives_restantes = tentatives
        self.tentatives_restantes_label.config(text=f"Tentatives restantes: {self.tentatives_restantes}")


    def mettre_a_jour_niveau(self, niveau):
        """Met à jour l'étiquette du niveau.

        Args:
            niveau (int): Le nouveau niveau à afficher.
        """
        self.niveau = niveau
        self.niveau_label.config(text=f"Niveau: {self.niveau}")
