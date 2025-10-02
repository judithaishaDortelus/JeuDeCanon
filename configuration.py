"""Configuration des paramètres pour le jeu de canon.

Ce fichier contient les constantes utilisées pour définir les limites
des paramètres du jeu, telles que l'angle et la puissance du tir.

Constantes:
    ANGLE_MIN (int): L'angle minimum acceptable pour le tir.
    ANGLE_MAX (int): L'angle maximum acceptable pour le tir.
    PUISSANCE_MIN (int): La puissance minimum acceptable pour le tir.
    PUISSANCE_MAX (int): La puissance maximum acceptable pour le tir.
"""
"""
    -'pathlib': Nécessaire pour manipuler le chemin du fichier et répertoires de manière portable et efficace
"""
from pathlib import Path

# Angle de tir en degrés
ANGLE_MIN = -5  # L'angle minimum acceptable pour le tir.
ANGLE_MAX = 200  # L'angle maximum acceptable pour le tir.

# Puissance de tir
PUISSANCE_MIN = 0  # La puissance minimum acceptable pour le tir.
PUISSANCE_MAX = 350  # La puissance maximum acceptable pour le tir.

# Définit le dossier de base de l'application comme étant le dossier contenant ce fichier de configuration.
DOSSIER_BASE = Path(__file__).resolve().parent

# Chemin vers le fichier stockant les informations concernant les scores
FICHIER_CLASSEMENT = DOSSIER_BASE / "classement.txt"
