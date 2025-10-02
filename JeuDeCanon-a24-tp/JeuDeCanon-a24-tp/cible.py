import random
from projectile import Projectile

class Cible:
    """Classe permettant de représenter une cible.

    Attributs:
        canvas (tk.Canvas): La toile où la cible est dessinée.
        x (int): La position x de la cible.
        y (int): La position y de la cible.
        identifiant (int): L'identifiant de la cible dans la toile.
    """

    def __init__(self, canvas):
        """Initialise un objet Cible avec une toile donnée.

        Args:
            canvas (tk.Canvas): La toile où la cible sera dessinée.
        """
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.identifiant = None

        self.creer_nouvelle_cible()

    def creer_nouvelle_cible(self):
        """Crée une nouvelle cible à une position aléatoire sur la toile."""
        self.x = random.randint(400, 750)
        self.y = random.randint(50, 550)
        self.identifiant = self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill="#ff000d", outline="")


    def est_touchee(self, projectile):
        """Vérifie si la cible est touchée par un projectile aux coordonnées données.

        Cette méthode détermine si le projectile, aux coordonnées spécifiées,
        se trouve dans une zone de 10 unités autour de la cible.

        Args:
            projectile (Projectile): L'objet Projectile dont les coordonnées
            doivent être vérifiées.

        Returns:
            bool: True si le projectile touche la cible, False sinon.
        """
        x0_c, y0_c, x1_c, y1_c = self.canvas.coords(self.identifiant)
        x0_c -= 10
        y0_c -= 10
        x1_c += 10
        y1_c += 10

        projectile = projectile.animer()
        x, y = projectile

        if (x < x1_c) and (x > x0_c) and (y < y1_c) and (y > y0_c):
            return True

        return False
