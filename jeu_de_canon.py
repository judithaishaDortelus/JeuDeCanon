import tkinter as tk
from tkinter import messagebox
from canon import Canon
from cible import Cible
from commandes_jeu import CommandesJeu
from configuration import ANGLE_MIN, ANGLE_MAX, PUISSANCE_MIN, PUISSANCE_MAX, FICHIER_CLASSEMENT
from classement import Classement
from projectile import Projectile
from statut_jeu import StatutJeu
from exceptions import AngleInvalideException, PuissanceInvalideException, ValeursNumeriquesInvalides


class JeuDeCanon:
    """Classe pour gérer la fonctionnalité du jeu de canon.

    Attributs:
        fenetre_racine (tk.Tk): La fenêtre principale de l'application.
        classement (Classement): L'objet Classement pour gérer les scores.
        canvas (tk.Canvas): La toile où le jeu est dessiné.
        angle (float): L'angle du canon.
        puissance (float): La puissance du tir.
        score (int): Le score actuel du joueur.
        niveau (int): Le niveau actuel du jeu.
        tentatives_restantes (int): Le nombre de tentatives restantes dans le niveau actuel.
        max_tentatives (int): Le nombre maximum de tentatives par niveau.
        message_touche (int): L'identifiant du message affiché lorsque la cible est touchée.
        commandes (CommandesJeu): L'objet CommandesJeu pour gérer les contrôles du jeu.
        statut (StatutJeu): L'objet StatutJeu pour gérer le statut du jeu.
        canon (Canon): L'objet Canon représentant le canon du jeu.
        cible (Cible): L'objet Cible représentant la cible du jeu.
        projectile (Projectile): L'objet Projectile représentant le projectile tiré.
    """

    def __init__(self, fenetre_racine):
        """Initialise un objet JeuDeCanon avec une fenêtre principale donnée.

        Args:
            fenetre_racine (tk.Tk): La fenêtre principale de l'application.
        """
        self.fenetre_racine = fenetre_racine
        self.fenetre_racine.title("Jeu de Canon")
        self.fenetre_racine.config(bg="#87CEEB")
        self.fenetre_racine.resizable(False, False)

        self.classement = Classement()

        self.canvas = tk.Canvas(fenetre_racine, width=800, height=600, bg="#87CEEB")
        self.canvas.pack(pady=10)

        self.angle = 45
        self.puissance = 50
        self.score = 0
        self.niveau = 1
        self.tentatives_restantes = 3
        self.max_tentatives = 3  # Nombre maximum de tentatives par niveau

        self.message_touche = (
            None  # Initialisation du message affiché lorsqu'une cible est touchée
        )

        self.commandes_statut_frame = tk.Frame(self.fenetre_racine, bg="#4682B4")
        self.commandes_statut_frame.pack(
            side=tk.TOP, fill=tk.X
        )  # Création du cadre pour les commandes et le statut

        self.commandes = CommandesJeu(
            self.commandes_statut_frame, self, self.angle, self.puissance
        )
        self.statut = StatutJeu(
            self.commandes_statut_frame,
            self.score,
            self.niveau,
            self.tentatives_restantes,
        )
        self.commandes_statut_frame.pack(
            side=tk.TOP, fill=tk.X
        )  # Création du cadre contenant les commandes et le statut du jeu
        self.canon = Canon(self.canvas, self.angle)
        self.cible = Cible(self.canvas)

        self.projectile = None

    def tirer(self):
        """Gère l'action de tir et l'animation du projectile.

        Cette méthode effectue les opérations suivantes :
        1. Récupère et valide les valeurs de l'angle et de la puissance depuis les entrées utilisateur.
        2. Met à jour l'angle du canon.
        3. Crée et anime le projectile en fonction des valeurs saisies.
        4. Gère les collisions et les sorties de l'écran du projectile.
        5. Met à jour les tentatives restantes et le score, et affiche des messages appropriés.

        Exceptions :
        - Affiche un message d'erreur si les valeurs de l'angle ou de la puissance sont invalides.
        - Désactive le bouton "Tirer" pendant l'animation du projectile.

        Si le projectile touche la cible :
        - Met à jour le score et supprime la cible.
        - Affiche un message de succès et un bouton pour passer au niveau suivant.
        - Désactive le bouton "Tirer".

        Si le projectile sort de l'écran sans toucher la cible :
        - Réduit le nombre de tentatives restantes.
        - Met à jour l'affichage des tentatives restantes.
        - Termine le jeu si toutes les tentatives sont utilisées.

        Conditions de validation :
        - L'angle doit être compris entre ANGLE_MIN et ANGLE_MAX.
        - La puissance doit être comprise entre PUISSANCE_MIN et PUISSANCE_MAX.

        Affiche des messages d'erreur appropriés en cas de valeurs invalides.
        """
        try:
            self.angle = float(self.commandes.angle_entry.get())
            self.puissance = float(self.commandes.puissance_entry.get())

            if not (ANGLE_MIN <= self.angle <= ANGLE_MAX):
                raise AngleInvalideException(ANGLE_MIN, ANGLE_MAX)

            if not (PUISSANCE_MIN <= self.puissance <= PUISSANCE_MAX):
                raise PuissanceInvalideException(PUISSANCE_MIN, PUISSANCE_MAX)

        except ValueError:
            try:
                raise ValeursNumeriquesInvalides("Veuillez entrer des valeurs numériques valides.")
            except ValeursNumeriquesInvalides as e:
                messagebox.showerror("Erreur de validation", str(e))

        except AngleInvalideException as e:
            messagebox.showerror("Erreur de validation", str(e))

        except PuissanceInvalideException as e:
            messagebox.showerror("Erreur de validation", str(e))


        self.canon.mettre_a_jour(self.angle)

        if self.projectile:
            self.canvas.delete(
                self.projectile.identifiant
            )  # Suppression du projectile précédent s'il existe

        self.projectile = Projectile(self.canvas, self.angle, self.puissance)

        self.commandes.tirer_button.config(
            state=tk.DISABLED
        )  # Désactivation du bouton tirer pendant l'animation

        continuer_animation = True  # Indicateur pour contrôler la boucle

        # Boucle pour animer le mouvement du projectile
        while continuer_animation:
            x, y = self.projectile.animer()

            self.fenetre_racine.update()  # Mettre à jour l'interface graphique pour chaque étape de l'animation

            # Si la cible est manquée
            if x > 800 or y > 600 or x < 0 or y < 0:
                self.canvas.delete(
                    self.projectile.identifiant
                )  # Retirer le projectile de la toile
                self.projectile = None
                self.tentatives_restantes -= 1
                self.statut.mettre_a_jour_tentatives_restantes(
                    self.tentatives_restantes
                )
                if self.tentatives_restantes == 0:
                    self.terminer("Fin du Jeu")
                else:
                    self.commandes.tirer_button.config(
                        state=tk.NORMAL
                    )  # Réactivation du bouton tirer

                continuer_animation = False  # Arrêter la boucle

            elif self.cible.est_touchee(self.projectile):
                self.score += 10  # Augmenter le score
                self.statut.mettre_a_jour_score(self.score)
                self.canvas.delete(
                    self.cible.identifiant
                )  # Suppression de la cible touchée de la toile
                self.canvas.delete(
                    self.projectile.identifiant
                )  # Suppression du projectile de la toile
                self.projectile = None
                self.afficher_message_touche()
                self.commandes.niveau_suivant_button.pack(
                    side=tk.BOTTOM, pady=10
                )  # Affichage du bouton pour passer au niveau suivant
                self.commandes.tirer_button.config(
                    state=tk.DISABLED
                )  # Désactivation du bouton tirer

                continuer_animation = False  # Arrêter la boucle
            else:
                self.canvas.after(10)


    def afficher_message_touche(self):
        """Affiche le message lorsque la cible est touchée."""

        if self.afficher_message_touche is not None:
            self.message_touche = self.canvas.create_text(400, 300, text="TOUCHÉ!", fill="green", font=("Arial", 26))

    def effacer_message_touche(self):
        """Efface le message touché s'il existe."""
        if self.message_touche:
            self.canvas.delete(self.message_touche)
            self.message_touche = None

    def passer_au_niveau_suivant(self):
        """Passe au niveau suivant du jeu."""
        self.niveau += 1
        self.statut.mettre_a_jour_niveau(self.niveau)
        self.tentatives_restantes = (
            self.max_tentatives
        )  # Réinitialisation des tentatives restantes
        self.statut.mettre_a_jour_tentatives_restantes(self.tentatives_restantes)
        self.cible.creer_nouvelle_cible()
        self.effacer_message_touche()
        self.commandes.niveau_suivant_button.pack_forget()  # Masquage du bouton niveau suivant
        self.commandes.tirer_button.config(
            state=tk.NORMAL
        )  # Réactivation du bouton tirer

    def terminer(self, message):
        """Termine le jeu et affiche un message.

        Args:
            message (str): Le message à afficher à la fin du jeu.
        """
        self.canvas.create_text(
            400, 300, text=message, font=("Helvetica", 30), fill="red"
        )
        self.commandes.tirer_button.config(
            state=tk.DISABLED
        )  # Désactivation du bouton tirer
        self.commandes.niveau_suivant_button.pack_forget()  # Masquage du bouton niveau suivant
        self.commandes.nouveau_jeu_button.pack(
            side=tk.BOTTOM, pady=10
        )  # Affichage du bouton nouveau jeu
        self.afficher_fenetre_soumission_score()

    def afficher_fenetre_soumission_score(self):
        """Demande le nom du joueur pour enregistrer le score."""
        fenetre_soumission_score = tk.Toplevel()  # Création d'une nouvelle fenêtre
        fenetre_soumission_score.geometry("300x300")
        fenetre_soumission_score.title("Soumission de Score")
        tk.Label(
            fenetre_soumission_score, text="Entrez votre nom:", font=("Helvetica", 12)
        ).pack(pady=10)
        nom_entry = tk.Entry(fenetre_soumission_score, font=("Helvetica", 12))
        nom_entry.pack(pady=10)
        tk.Button(
            fenetre_soumission_score,
            text="Soumettre",
            font=("Helvetica", 12),
            command=lambda: self.soumettre_score(
                nom_entry.get(), fenetre_soumission_score
            ),
        ).pack(pady=10)

    def soumettre_score(self, nom, fenetre_parente):
        """Soumet le score du joueur au classement.

        Cette méthode enregistre le score actuel du joueur sous le nom fourni
        dans le classement, puis ferme la fenêtre de soumission.

        Note: Un message d'erreur devra être affiché si le nom fourni est vide.

        Args:
            nom (str): Le nom du joueur. Ce nom sera utilisé pour enregistrer le score.
            fenetre_parente (tk.Toplevel): La fenêtre parente contenant le formulaire de soumission.
                                           Cette fenêtre sera fermée après la soumission du score.

        Exemple:
            Si le score actuel du joueur est 100 et que le nom fourni est 'Alice',
            le score sera ajouté au classement avec le format ('Alice', 1500).
            La fenêtre de soumission sera ensuite fermée.
        """
        if not nom.strip():
            tk.messagebox.showerror(message="Le nom ne peut pas être vide.")
            return

        score = self.score
        self.classement.enregistrer_score(nom, score)
        fenetre_parente.destroy()

        # ** Done **

    def demarrer_nouveau_jeu(self):
        """Démarre un nouveau jeu."""
        self.score = 0  # Réinitialisation du score
        self.niveau = 1  # Réinitialisation du niveau
        self.tentatives_restantes = (
            self.max_tentatives
        )  # Réinitialisation des tentatives restantes

        self.statut.mettre_a_jour_score(self.score)
        self.statut.mettre_a_jour_niveau(self.niveau)
        self.statut.mettre_a_jour_tentatives_restantes(self.tentatives_restantes)

        self.canvas.delete("all")  # Suppression de tous les éléments de la toile
        self.canon.creer()
        self.cible.creer_nouvelle_cible()
        self.effacer_message_touche()

        self.commandes.tirer_button.config(
            state=tk.NORMAL
        )  # Réactivation du bouton tirer
        self.commandes.niveau_suivant_button.pack_forget()  # Masquage du bouton niveau suivant
        self.commandes.nouveau_jeu_button.pack_forget()  # Masquage du bouton nouveau jeu
