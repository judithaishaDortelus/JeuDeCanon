# Jeu De Canon
Interface graphique d'un jeu de canon développée en Python selon une architecture orientée objet.
Met en oeuvre la modélisation physique, la gestion des collision et une interface utilisateur interactive.
Projet réalisé dans le cadre d'un projet universitaire à l'Université Laval.

### Principales fonctionnalités:
- Ajustement de l'angle et de la puissance du tir
- Détection de cible
- Animation du projectile 
- Classement des meilleurs scores

### Technologies utilisées:
- Python
- TKinter
- Math
- Random

### Aperçu du jeu de canon:
#### Entrée
Le joueur peut ajuster l'angle et la puissance du tir. La trajectoire du projectile est calculée à l'aide de fonctions trigonométrique (module math) tandis que la prosition de la cible est générée aléatoirement (module random). Une animation affiche le mouvement du tir en temps réel.
<img width="1267" height="886" alt="01 0" src="https://github.com/user-attachments/assets/7a61fb85-c114-4176-bdb2-3723e8d8853c" />
<img width="1078" height="761" alt="01 1" src="https://github.com/user-attachments/assets/3ea55dd3-7686-4309-94f4-428c8d2684c4" />
<img width="1187" height="871" alt="01 2" src="https://github.com/user-attachments/assets/1a9974d1-ed05-45a5-8ff8-56b9d958aca6" />

#### Niveaux et essais
À chaque tir réussi, le joueur passe au niveau suivant et voit son score augmenter. Le nombre d'essais est alors réinitialisé.
<img width="1187" height="169" alt="02 0" src="https://github.com/user-attachments/assets/ecd5a80d-8b7f-475f-bbb4-f9d02cb41e50" />
<img width="1041" height="140" alt="02 1" src="https://github.com/user-attachments/assets/9b9c10a2-9679-4891-aa48-23f9ada21889" />
<img width="1063" height="194" alt="02 2" src="https://github.com/user-attachments/assets/78cc340e-9d9b-4ecf-b57c-d327df687ed5" />
<img width="1058" height="180" alt="03 0" src="https://github.com/user-attachments/assets/351af179-f3fc-449a-b457-1d569e68edb1" />

#### Fin de partie et classement
À la fin de la partie, le joueur peut enregistrer son nom et son score (savegardés dans un fichier .txt). Il est également possible de consulter à tout moment le tableau des 10 meilleurs joueurs.
<img width="1094" height="850" alt="03 1" src="https://github.com/user-attachments/assets/e4f4d179-4022-4fd0-995e-04f5b8541573" />
<img width="1097" height="851" alt="04" src="https://github.com/user-attachments/assets/197e58e5-2089-4c87-a3c0-3120b9cad474" />
