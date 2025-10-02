import tkinter as tk
from configuration import FICHIER_CLASSEMENT

class CommandesJeu:
    """Classe pour gérer les commandes du jeu.

    Attributs:
        jeu (JeuDeCanon): L'objet représentant le jeu de canon.
        angle (float): L'angle initial du canon.
        puissance (float): La puissance initiale du tir.
        commandes_frame (tk.Frame): Le cadre contenant les commandes du jeu.
        angle_label (tk.Label): L'étiquette pour l'angle.
        angle_entry (tk.Entry): Le champ de saisie pour l'angle.
        puissance_label (tk.Label): L'étiquette pour la puissance.
        puissance_entry (tk.Entry): Le champ de saisie pour la puissance.
        tirer_button (tk.Button): Le bouton pour tirer.
        afficher_classement_button (tk.Button): Le bouton pour afficher le classement.
        niveau_suivant_button (tk.Button): Le bouton pour passer au niveau suivant.
        nouveau_jeu_button (tk.Button): Le bouton pour démarrer un nouveau jeu.
    """

    def __init__(self, parent_frame, jeu, angle, puissance):
        """Initialise un objet CommandesJeu avec les paramètres donnés.

        Args:
            parent_frame (tk.Frame): Le cadre parent pour les commandes du jeu.
            jeu (JeuDeCanon): L'objet représentant le jeu de canon.
            angle (float): L'angle initial du canon.
            puissance (float): La puissance initiale du tir.
        """
        self.jeu = jeu
        self.angle = angle
        self.puissance = puissance

        self.commandes_frame = tk.Frame(parent_frame, bg="#4682B4")
        self.commandes_frame.pack(
            side=tk.LEFT, padx=10, pady=5
        )  # Création du cadre pour les commandes

        self.angle_label = tk.Label(
            self.commandes_frame,
            text="Angle:",
            font=("Helvetica", 12),
            bg="#4682B4",
            fg="white",
        )
        self.angle_label.pack(side=tk.LEFT, padx=10, pady=5)

        self.angle_entry = tk.Entry(
            self.commandes_frame, font=("Helvetica", 12), width=5
        )
        self.angle_entry.insert(
            tk.END, str(self.angle)
        )  # Insertion de l'angle initial dans le champ de saisie
        self.angle_entry.pack(side=tk.LEFT, padx=10, pady=5)

        self.puissance_label = tk.Label(
            self.commandes_frame,
            text="Puissance:",
            font=("Helvetica", 12),
            bg="#4682B4",
            fg="white",
        )
        self.puissance_label.pack(side=tk.LEFT, padx=10, pady=5)

        self.puissance_entry = tk.Entry(
            self.commandes_frame, font=("Helvetica", 12), width=5
        )
        self.puissance_entry.insert(
            tk.END, str(self.puissance)
        )  # Insertion de la puissance initiale dans le champ de saisie
        self.puissance_entry.pack(side=tk.LEFT, padx=10, pady=5)

        self.tirer_button = tk.Button(
            self.commandes_frame,
            text="Tirer",
            font=("Helvetica", 12),
            command=self.jeu.tirer,
            fg="#1F2937",
        )
        self.tirer_button.pack(
            side=tk.LEFT, padx=10, pady=5
        )  # Création du bouton pour tirer

        self.afficher_classement_button = tk.Button(
            self.commandes_frame,
            text="Afficher Classement",
            font=("Helvetica", 12),
            command = self.jeu.classement.afficher,
            fg = "#1F2937",
        )
        self.afficher_classement_button.pack(
            side=tk.LEFT, padx=15, pady=5
        )

        self.niveau_suivant_button = tk.Button(
            self.jeu.fenetre_racine,
            text="Niveau Suivant",
            font=("Helvetica", 12),
            command=self.jeu.passer_au_niveau_suivant,
            fg="#1E40AF",
        )
        self.niveau_suivant_button.pack(side=tk.BOTTOM, pady=10)
        self.niveau_suivant_button.pack_forget()  # Cacher initialement le bouton permettant de passer au niveau suivant

        self.nouveau_jeu_button = tk.Button(
            self.jeu.fenetre_racine,
            text="Nouveau Jeu",
            font=("Helvetica", 12),
            command=self.jeu.demarrer_nouveau_jeu,
            fg="#166534",
        )
        self.nouveau_jeu_button.pack(side=tk.BOTTOM, pady=10)
        self.nouveau_jeu_button.pack_forget()  # Cacher initialement le bouton permettant de démarrer un nouveau jeu
