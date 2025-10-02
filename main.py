import tkinter as tk
from jeu_de_canon import JeuDeCanon


# Point d'entrée principal de l'application
if __name__ == "__main__":
    # Création de la fenêtre principale de l'application
    fenetre_racine = tk.Tk()

    # Initialisation du jeu de canon avec la fenêtre principale
    jeu = JeuDeCanon(fenetre_racine)

    # Lancement de la boucle principale de l'application
    fenetre_racine.mainloop()
