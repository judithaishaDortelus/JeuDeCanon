import math
import tkinter as tk


class Projectile:
    """Classe pour gérer la fonctionnalité du projectile.

    Attributs:
        canvas (tk.Canvas): La toile où le projectile est dessiné.
        angle (float): L'angle initial du tir.
        puissance (float): La puissance initiale du tir.
        x (float): La position x du projectile.
        y (float): La position y du projectile.
        identifiant (int): L'identifiant du projectile dans la toile.
        vx (float): Vitesse horizontale du projectile.
        vy (float): Vitesse verticale du projectile.
    """

    def __init__(self, canvas, angle, puissance, x=70, y=570):
        """Initialise un objet Projectile avec la toile, l'angle et la puissance donnés.

        Args:
            canvas (tk.Canvas): La toile où le projectile sera dessiné.
            angle (float): L'angle initial du tir.
            puissance (float): La puissance initiale du tir.
            x (float): La position x initiale du projectile.
            y (float): La position y initiale du projectile.
        """
        self.canvas = canvas
        self.angle = angle
        self.puissance = puissance
        self.x = x
        self.y = y
        self.identifiant = None
        self.vx = 0
        self.vy = 0

        self.creer_projectile()
        self.initialiser_vitesses()
        self.animer()


    def creer_projectile(self):
        """Crée le projectile sur la toile."""
        self.identifiant = self.canvas.create_oval(
            self.x, self.y, self.x + 10, self.y + 10, fill="#1E90FF", outline=""
        )

    def initialiser_vitesses(self):
        """Initialise les vitesses initiales."""
        angle_en_radians = math.radians(self.angle)
        self.vx = self.puissance * math.cos(
            angle_en_radians
        )  # Calcul de la vitesse horizontale
        self.vy = -self.puissance * math.sin(
            angle_en_radians
        )  # Calcul de la vitesse verticale

    def animer(self):
        """Anime le projectile en mouvement.

        Returns:
            tuple: Les nouvelles coordonnées du projectile (x, y).
        """
        self.x += self.vx * 0.1
        self.y += self.vy * 0.1
        self.vy += 9.8 * 0.1  # gravité

        # Mise à jour des coordonnées du projectile
        self.canvas.coords(self.identifiant, self.x, self.y, self.x + 10, self.y + 10)

        return self.x, self.y  # Retourne les nouvelles coordonnées du projectile
