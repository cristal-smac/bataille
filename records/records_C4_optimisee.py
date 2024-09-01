# records actuels selon le nombre de valeurs de cartes (V) et 4 couleurs avec rangement optimisé.

# Pour l'instant cycles trouvés pour V=5 et V=7 et V=11, mais aucun aligné

from bataille import *

# Décommenter celui à tester

#------------------------------------------------------

# V=2 - MAXIMUM POSSIBLE - 38 parties
# Gagnant : (0, 0) - Nombre de plis : 5 - Nombre de cartes posees : 8
#cartes_joueur1 = [2, 2, 1, 1]
#cartes_joueur2 = [1, 1, 2, 2]
# Durée moyenne : 5,26

# Aucun cycle

#------------------------------------------------------

# V=3 - MAXIMUM POSSIBLE - 17.370
# Gagnant : (0, 1) - Nombre de plis : 34 - Nombre de cartes posees : 48
#cartes_joueur1 = [3, 2, 2, 2, 3, 3]
#cartes_joueur2 = [1, 1, 2, 3, 1, 1]
# Durée moyenne : 12.07

# Aucun cycle

#------------------------------------------------------

# V=4 - MAXIMUM POSSIBLE - 31.532.760 (32mn)
# Gagnant : (0, 1) - Nombre de plis : 100 - Nombre de cartes posees : 138
#cartes_joueur1 = [2, 4, 2, 2, 1, 1, 4, 1]
#cartes_joueur2 = [2, 3, 4, 3, 1, 3, 3, 4]
# Durée moyenne : 24,03

# Aucun cycle

#------------------------------------------------------

# V=5 (10^9 testées) (il y en a 150 milliards !!  (152.770.174.200 exactement))
#Gagnant : (1, 0) - Nombre de plis : 311 - Nombre de cartes posees : 382
#cartes_joueur1 = [2, 3, 5, 3, 1, 4, 4, 2, 4, 5]
#cartes_joueur2 = [5, 3, 1, 1, 2, 4, 2, 3, 5, 1]
# Duree moyenne :41.77

# 1 Cycle de taille 28
# cartes_joueur1 = [3, 1, 5, 4, 3, 2, 4, 3, 3, 2]
# cartes_joueur2 = [1, 1, 5, 4, 2, 2, 5, 4, 5, 1]

#------------------------------------------------------

# V=6
# Gagnant : (1, 0) - Nombre de plis : 620 - Nombre de cartes posees : 736
#cartes_joueur1 = [5, 3, 2, 2, 6, 2, 4, 5, 3, 6, 6, 3]
#cartes_joueur2 = [5, 6, 4, 4, 3, 1, 5, 2, 1, 1, 1, 4]
# Duree moyenne : 62.16

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=7
# Gagnant : (0, 1) - Nombre de plis : 2427 - Nombre de cartes posees : 2690
#cartes_joueur1 = [1, 2, 2, 2, 6, 5, 3, 1, 1, 3, 1, 4, 7, 7]
#cartes_joueur2 = [7, 4, 5, 5, 4, 4, 3, 5, 6, 2, 7, 6, 6, 3]

# Nombreux cycles, en général très longs (min 224) ! Ne pas les afficher !!
# cartes_joueur1 = [3, 5, 1, 7, 6, 6, 2, 4, 2, 3, 1, 7, 7, 6, 4, 5, 2, 3, 1]
# cartes_joueur2 = [5, 5, 4, 4, 3, 2, 1, 7, 6))

#------------------------------------------------------

# V=8
# Gagnant : (0, 1) - Nombre de plis : 1645 - Nombre de cartes posees : 1858
#cartes_joueur1 = [5, 3, 8, 6, 8, 6, 1, 3, 2, 1, 8, 7, 7, 1, 2, 1]
#cartes_joueur2 = [3, 5, 2, 7, 6, 4, 6, 3, 4, 8, 5, 7, 4, 4, 5, 2]

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# N9
# Gagnant : (0, 1) - Nombre de plis : 1936 - Nombre de cartes posees : 2154
#cartes_joueur1 = [1, 8, 6, 5, 6, 8, 2, 9, 2, 4, 7, 7, 7, 2, 5, 1, 1, 5]
#cartes_joueur2 = [9, 8, 6, 6, 4, 3, 3, 5, 2, 7, 8, 3, 9, 3, 9, 4, 4, 1]

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=10
#Gagnant : (0, 1) - Nombre de plis : 2628 - Nombre de cartes posees : 2896
#cartes_joueur1 = [8, 9, 3, 9, 7, 2, 4, 10, 8, 8, 7, 6, 5, 3, 3, 4, 2, 10, 5, 3]
#cartes_joueur2 = [6, 6, 6, 4, 1, 7, 10, 4, 8, 2, 1, 9, 9, 1, 10, 5, 2, 5, 1, 7]

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=11
# Gagnant : (0, 1) - Nombre de plis : 15136 - Nombre de cartes posees : 15642
#cartes_joueur1 = [3, 8, 3, 10, 4, 3, 9, 4, 10, 1, 1, 3, 4, 2, 7, 7, 8, 11, 6, 7, 9, 6]
#cartes_joueur2 = [5, 11, 8, 10, 5, 9, 2, 5, 7, 6, 2, 10, 11, 1, 8, 5, 11, 9, 6, 4, 1, 2]

# Cycle de taille 1125 
# cartes_joueur1 = [11, 6, 6, 2, 8, 3, 4, 1, 11, 10, 9, 5, 9, 7, 3, 1, 10, 10, 8, 4, 8, 6, 5, 2]
# cartes_joueur1 = [10, 4, 6, 1, 11, 8, 7, 5, 9, 2, 5, 1, 11, 7, 7, 3, 9, 4, 3, 2]

#------------------------------------------------------

# V=12
#Gagnant : (1, 0) - Nombre de plis : 3206 - Nombre de cartes posees : 3472
#cartes_joueur1 = [2, 1, 11, 7, 5, 9, 6, 4, 6, 9, 10, 1, 3, 12, 3, 4, 1, 3, 4, 10, 2, 12, 11, 1]
#cartes_joueur2 = [3, 8, 8, 11, 7, 5, 9, 8, 7, 4, 10, 9, 8, 7, 5, 2, 12, 5, 2, 12, 6, 10, 11, 6]

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=13
#Gagnant : (0, 1) - Nombre de plis : 4060 - Nombre de cartes posees : 4402
#cartes_joueur1 = [13, 8, 13, 2, 10, 13, 12, 2, 3, 10, 5, 6, 1, 1, 6, 6, 2, 11, 2, 5, 12, 8, 7, 9, 5, 8]
#cartes_joueur2 = [12, 5, 4, 1, 9, 11, 7, 6, 1, 10, 3, 9, 7, 4, 11, 10, 3, 8, 4, 7, 12, 11, 13, 3, 9, 4]

# Aucun cycle encore trouvé aléatoirement



nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="optimisee", rangement_j2="optimisee",limite_cartes_posees=20000, trace=True)
print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")






