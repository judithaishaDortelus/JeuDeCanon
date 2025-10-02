class AngleInvalideException(Exception):
    def __init__(self, ANGLE_MIN, ANGLE_MAX):
        self.message = f"L'angle doit être compris entre {ANGLE_MIN} et {ANGLE_MAX} degrés."

    def __str__(self):
        return self.message

class PuissanceInvalideException(Exception):
    def __init__(self, PUISSANCE_MIN, PUISSANCE_MAX):
        self.message = f"La puissance doit être comprise entre {PUISSANCE_MIN} et {PUISSANCE_MAX}."

    def __str__(self):
        return self.message

class ValeursNumeriquesInvalides(Exception):
    def __init__(self, message="Veuillez entrer des valeurs numériques valides."):
        self.message = message

    def __str__(self):
        return self.message