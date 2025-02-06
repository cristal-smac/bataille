# records actuels selon le nombre de valeurs de cartes (V) et 4 couleurs avec rangement naturel.

# Il existe des cycles alignés pour (C=4 V=4) et (C=4 V=6), ce qui permet de construire des cycles alignés pour C=4 et V pair à partir de 4 (V= 4, 6, 8, 10, ...)

from bataille import *

# Décommenter celui à tester

#------------------------------------------------------

# V=2  - MAXIMUM POSSIBLE - 38 parties
# Gagnant : (1, 0) - Nombre de plis : 4 - Nombre de cartes posees : 8
# cartes_joueur1 = [1, 1, 2, 2]
# cartes_joueur2 = [1, 2, 2, 1]
# Durée moyenne : 5,26

# Aucun cycle

#------------------------------------------------------

# V=3  - MAXIMUM POSSIBLE - 17.370 parties
# Gagnant : (1, 0) - Nombre de plis : 37 - Nombre de cartes posees : 54
#cartes_joueur1 =[2, 1, 3, 1, 3, 2]
#cartes_joueur2 = [2, 3, 3, 1, 1, 2]
# Durée moyenne : 13,43

# 360 cycles qui amènent à un seul cycle de taille 19, malheureusement non aligné :(((
#cartes_joueur1 = [3,2,1,1,2,1]
#cartes_joueur2 = [2,1,3,2,3,3] 

#------------------------------------------------------

# V=4  - MAXIMUM POSSIBLE - 31.532.760 parties (46mn)
# Gagnant : (1, 0) - Nombre de plis : 142 - Nombre de cartes posees : 192
#cartes_joueur1 = [2, 1, 3, 3, 4, 2, 3, 4]
#cartes_joueur2 = [4, 1, 3, 1, 4, 2, 2, 1]
# Durée moyenne : 28,61

# 8545 cycles qui amènent à 4 cycles différents, tous de taille 24 et tous alignés !
#[4, 2, 4, 1, 3, 1, 3, 3] [2, 1, 4, 4, 3, 2, 2, 1]
#[3, 1, 3, 3, 2, 1, 4, 4] [3, 2, 2, 1, 4, 2, 4, 1]
#[3, 1, 3, 3, 4, 1, 4, 4] [3, 2, 2, 1, 4, 2, 2, 1]
#[2, 1, 4, 4, 2, 1, 3, 3] [4, 2, 4, 1, 3, 2, 3, 1]

# Ex : Cycle aligné de taille 24
#cartes_joueur1 = [2, 1, 4, 4, 2, 1, 3, 3]
#cartes_joueur2 = [4, 2, 4, 1, 3, 2, 3, 1]

#------------------------------------------------------

# V=5 (il y  a 150 milliards de parties !!  (152.770.174.200 exactement))
# Gagnant : (1, 0) - Nombre de plis : 453 - Nombre de cartes posees : 562
#cartes_joueur1 = [1, 1, 1, 2, 1, 5, 3, 4, 4, 5]
#cartes_joueur2 = [2, 3, 5, 3, 4, 5, 2, 3, 4, 2]

# Aucun cycle encore trouvé aléatoirement : A mon avis, il n'y en n'a pas

#------------------------------------------------------

# V=6
#Gagnant : (1, 0) - Nombre de plis : 908 - Nombre de cartes posees : 1088
#cartes_joueur1 = [1, 2, 4, 4, 6, 6, 5, 2, 3, 1, 2, 3]
#cartes_joueur2 = [6, 5, 4, 1, 1, 5, 2, 3, 6, 4, 5, 3]
# Duree moyenne = 72.37

# Enormément de cycles alignés. Ici ex de taille 36
#cartes_joueur1 = [4, 2, 5, 5, 4, 2, 6, 6, 3, 2, 2, 1]
#cartes_joueur2 = [5, 4, 5, 1, 6, 4, 6, 1, 3, 1, 3, 3]

#------------------------------------------------------

# V=7
# Gagnant : (0, 1) - Nombre de plis : 1488 - Nombre de cartes posees : 1710
#cartes_joueur1 = [4, 1, 5, 4, 4, 6, 2, 4, 7, 3, 3, 7, 5, 7]
#cartes_joueur2 = [6, 7, 5, 5, 1, 6, 3, 1, 1, 6, 2, 2, 2, 3]

# Enormément de cycles 

#------------------------------------------------------

# V=8  (jeu de 32 cartes)
# NOUVEAU Gagnant : (0, 1) - Nombre de plis : 2216 - Nombre de cartes posees : 2546
# découvert par Marc Lapierre le 6/02/2025
#cartes_joueur1 = [8, 5, 1, 4, 4, 2, 4, 5, 7, 8, 6, 7, 3, 8, 7, 7]
#cartes_joueur2 = [3, 3, 1, 2, 1, 4, 5, 6, 6, 6, 5, 2, 2, 1, 8, 3]


# Cycle de taille 48
#cartes_joueur1 = [8, 5, 5, 1, 6, 2, 6, 6, 7, 2, 7, 7, 4, 2, 4, 4]
#cartes_joueur2 = [8, 1, 8, 8, 6, 5, 5, 1, 7, 3, 3, 1, 4, 3, 3, 2]

#------------------------------------------------------

# V=9
# NOUVEAU Gagnant : (1, 0) - Nombre de plis : 2612 - Nombre de cartes posees : 2926
# découvert par Marc Lapierre le 5/02/2025
#cartes_joueur1 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 9]
#cartes_joueur2 = [5, 9, 5, 5, 9, 8, 6, 8, 8, 7, 6, 9, 6, 6, 7, 8, 7, 7]


# Aucun cycle encore trouvé aléatoirement.

#------------------------------------------------------

# V=10
# NOUVEAU Gagnant : (0, 1) - Nombre de plis : 3245 - Nombre de cartes posees : 3606
#cartes_joueur1 = [10, 6, 7, 3, 10, 7, 4, 1, 9, 8, 2, 4, 4, 3, 4, 9, 1, 1, 10, 7]
#cartes_joueur2 = [9, 6, 3, 1, 2, 2, 7, 6, 8, 3, 6, 2, 10, 5, 9, 5, 5, 8, 5, 8]

# Aucun cycle encore trouvé aléatoirement


#------------------------------------------------------

# V=11
# NOUVEAU Gagnant : (1, 0) - Nombre de plis : 3860 - Nombre de cartes posees : 4224
#cartes_joueur1 = [4, 8, 4, 3, 9, 2, 11, 1, 2, 8, 4, 4, 8, 3, 6, 7, 7, 8, 6, 11, 2, 11]
#cartes_joueur2 = [1, 3, 6, 10, 1, 3, 6, 1, 7, 5, 11, 10, 9, 10, 7, 2, 9, 5, 9, 10, 5, 5] 

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=12
# NOUVEAU Gagnant : (0, 1) - Nombre de plis : 4453 - Nombre de cartes posees : 4860
#cartes_joueur1 = [9, 2, 4, 11, 3, 10, 6, 4, 1, 3, 10, 2, 10, 12, 7, 2, 5, 7, 3, 4, 11, 7, 4, 2]
#cartes_joueur2 = [9, 5, 1, 3, 8, 11, 11, 7, 1, 6, 1, 12, 8, 6, 10, 9, 6, 9, 8, 8, 12, 12, 5, 5]

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=13
# NOUVEAU Gagnant : (0, 1) - Nombre de plis : 5506 - Nombre de cartes posees : 5942
#cartes_joueur1 = [1, 7, 7, 8, 1, 1, 9, 13, 1, 7, 3, 6, 10, 10, 2, 11, 9, 8, 12, 2, 7, 12, 2, 4, 4, 5]
#cartes_joueur2 = [3, 6, 6, 8, 2, 10, 4, 9, 11, 13, 8, 3, 6, 3, 12, 13, 12, 5, 10, 13, 5, 4, 11, 5, 11, 9]

# Aucun cycle encore trouvé aléatoirement




nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="naturelle", rangement_j2="naturelle",limite_cartes_posees=8000, trace=True)
print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")

