# records actuels selon le nombre de valeurs de cartes (V) avec 1 seule couleur (C=1) et rangement naturel.

# Conjecture "Spivey" : aucun cycle pour 2^V et 3*(2^V) donc aucun cycle pour 2,3,4,8,12,16,24,32,48

from bataille import *

# Décommenter celui à tester

#------------------------------------------------------

# V=2  - MAXIMUM POSSIBLE - 1 distrib
# Gagnant : (0, 1) - Nombre de plis : 1 - Nombre de cartes posees : 1
#cartes_joueur1 = [1]
#cartes_joueur2 = [2]

# aucun cycle

#------------------------------------------------------

# V=3  - MAXIMUM POSSIBLE - 3 distribs
# Gagnant : (0, 1) - Nombre de plis : 3 - Nombre de cartes posees : 3
#cartes_joueur1 = [2]
#cartes_joueur2 = [1, 3]

# aucun cycle

#------------------------------------------------------

# V=4  - MAXIMUM POSSIBLE - 12 distribs
# Gagnant : (0, 1) - Nombre de plis : 6 - Nombre de cartes posees : 6
#cartes_joueur1 = [1, 3]
#cartes_joueur2 = [4, 2]

# aucun cycle

#------------------------------------------------------

# V=5  - MAXIMUM POSSIBLE - 60 distribs
# Gagnant : (0, 1) - Nombre de plis : 8 - Nombre de cartes posees : 8
#cartes_joueur1 = [1, 4]
#cartes_joueur2 = [2, 3, 5]

#2 cycles différents tous de taille 6
#Nouveau Cycle de taille 6 False : (((4, 2), (3, 5, 1)), ((2, 4, 3), (5, 1)), ((4, 3), (1, 5, 2)), ((3, 4, 1), (5, 2)), ((4, 1), (2, 5, 3)), ((1, 4, 2), (5, 3)))
#Nouveau Cycle de taille 6 False : (((4, 3), (2, 5, 1)), ((3, 4, 2), (5, 1)), ((4, 2), (1, 5, 3)), ((2, 4, 1), (5, 3)), ((4, 1), (3, 5, 2)), ((1, 4, 3), (5, 2)))


#------------------------------------------------------

# V=6  - MAXIMUM POSSIBLE - 360 distribs
# Gagnant : (0, 1) - Nombre de plis : 15 - Nombre de cartes posees : 15
#cartes_joueur1 = [1, 3, 5]
#cartes_joueur2 = [4, 6, 2]

# Aucun cycle

#------------------------------------------------------

# V=7  - MAXIMUM POSSIBLE - 2520 distribs
# Gagnant : (0, 1) - Nombre de plis : 15 - Nombre de cartes posees : 15
#cartes_joueur1 = [3, 6, 2]
#cartes_joueur2 = [4, 5, 1, 7]

# 52 cycles différents tous de taille 8
#cartes_joueur1 = [2, 7, 3]
#cartes_joueur2 = [4, 1, 6, 5]

#------------------------------------------------------

# V=8  - MAXIMUM POSSIBLE - 20160 distribs
# Gagnant : (1, 0) - Nombre de plis : 26 - Nombre de cartes posees : 26
#cartes_joueur1 = [1, 4, 6, 8]
#cartes_joueur2 = [7, 2, 5, 3]
# Durée moyenne des parties (en écartant les cycles) : 10.53

# aucun cycle

#------------------------------------------------------

# V=9  - MAXIMUM POSSIBLE - 181.440 distribs
# Gagnant : (0, 1) - Nombre de plis : 28 - Nombre de cartes posees : 28
#cartes_joueur1 = [1, 2, 3, 8]
#cartes_joueur2 = [6, 5, 4, 7, 9]
# Durée moyenne des parties (en écartant les cycles) : 7.70

# Nouveau Cycle de taille 20 False : (((9, 4, 6, 5), (3, 8, 2, 7, 1)), ((4, 6, 5, 9, 3), (8, 2, 7, 1)), ((6, 5, 9, 3), (2, 7, 1, 8, 4)), ((5, 9, 3, 6, 2), (7, 1, 8, 4)), ((9, 3, 6, 2), (1, 8, 4, 7, 5)), ((3, 6, 2, 9, 1), (8, 4, 7, 5)), ((6, 2, 9, 1), (4, 7, 5, 8, 3)), ((2, 9, 1, 6, 4), (7, 5, 8, 3)), ((9, 1, 6, 4), (5, 8, 3, 7, 2)), ((1, 6, 4, 9, 5), (8, 3, 7, 2)), ((6, 4, 9, 5), (3, 7, 2, 8, 1)), ((4, 9, 5, 6, 3), (7, 2, 8, 1)), ((9, 5, 6, 3), (2, 8, 1, 7, 4)), ((5, 6, 3, 9, 2), (8, 1, 7, 4)), ((6, 3, 9, 2), (1, 7, 4, 8, 5)), ((3, 9, 2, 6, 1), (7, 4, 8, 5)), ((9, 2, 6, 1), (4, 8, 5, 7, 3)), ((2, 6, 1, 9, 4), (8, 5, 7, 3)), ((6, 1, 9, 4), (5, 7, 3, 8, 2)), ((1, 9, 4, 6, 5), (7, 3, 8, 2)))
# 336 Cycles différents de tailles 20 et 30


#------------------------------------------------------

# V=10 - MAXIMUM POSSIBLE - 1.814.400 distribs
# Gagnant : (0, 1) - Nombre de plis : 49 - Nombre de cartes posees : 49
#cartes_joueur1 = [1, 6, 2, 3, 9]
#cartes_joueur2 = [5, 8, 10, 7, 4]
# Durée moyenne des parties (en écartant les cycles) : 14.47

# 48 cycles différents tous de taille 60 , sur les 197970 cycles au total
# (3, 9, 7, 6, 2), (5, 8, 1, 10, 4)
# (7, 6, 2, 9, 4), (3, 10, 5, 8, 1)
# (5, 6, 2, 9, 4), (3, 10, 8, 7, 1)
# aucun n'est aligné (si V n'est pas un multiple de 2, pas d'alignement possible).

#------------------------------------------------------


# V=12 - MAXIMUM POSSIBLE - 239.500.800 distribs (212mn)
# Gagnant : (1, 0) - Nombre de plis : 74 - Nombre de cartes posees : 74
#cartes_joueur1 = [3, 1, 4, 9, 12, 10]
#cartes_joueur2 = [7, 6, 11, 5, 2, 8]
# Durée moyenne des parties (en écartant les cycles) : 20.86

# Aucun cycle

#------------------------------------------------------

# V=16 - 10^7 (52mn ;  10^6 en 1mn48)
# Gagnant : (1, 0) - Nombre de plis : 198 - Nombre de cartes posees : 198
#cartes_joueur1 =  [3, 8, 10, 7, 16, 9, 11, 2]
#cartes_joueur2 = [4, 12, 13, 5, 6, 1, 14, 15] 
# Durée moyenne des parties (en écartant les cycles) : 35.28

#------------------------------------------------------

# V=22 - 10^6

# Nouveau record : [2, 14, 22, 15, 10, 7, 11, 1, 12, 17, 5] [8, 21, 6, 4, 3, 16, 20, 19, 9, 18, 13]        Duree = 1103
# Durée moyenne des parties (en écartant les cycles) : 78.58

# Énormément de cycles de taille 264 très majoritairement, puis pas mal de 528 et quelques uns de plus de 1000 étapes
# mais aucun ne sera aligné (si V n'est pas un multiple de 2, pas d'alignement possible).

#------------------------------------------------------

# V=24 - 10^7 (55mn ; 10^6 en 5mn)
#Gagnant : (0, 1) - Nombre de plis : 670 - Nombre de cartes posees : 670
#cartes_joueur1 = [5, 2, 9, 22, 18, 23, 1, 12, 10, 7, 6, 17] 
#cartes_joueur2 = [13, 14, 21, 19, 20, 11, 24, 15, 8, 3, 4, 16]
# Durée moyenne des parties (en écartant les cycles) : 74.48

#------------------------------------------------------

# V=32 - 10^7 (124mn ; 10^6 en 12mn)
# Gagnant : (0, 1) - Nombre de plis : 1302 - Nombre de cartes posees : 1302
#cartes_joueur1 = [9, 27, 24, 29, 3, 21, 6, 8, 31, 19, 7, 5, 28, 13, 22, 26]
#cartes_joueur2 = [14, 10, 1, 11, 32, 30, 20, 25, 15, 16, 12, 18, 17, 23, 4, 2]
# Durée moyenne des parties (en écartant les cycles) : 130.10

#------------------------------------------------------

# V=48 - 10^6 (45mn)
# Gagnant : (1, 0) - Nombre de plis : 2790 - Nombre de cartes posees : 2790
#cartes_joueur1 = [20, 9, 45, 14, 30, 15, 36, 29, 40, 5, 39, 16, 13, 41, 27, 8, 1, 19, 48, 17, 18, 10, 3, 33]
#cartes_joueur2 = [28, 26, 24, 6, 42, 12, 43, 21, 37, 11, 22, 4, 47, 44, 7, 34, 31, 32, 25, 46, 23, 2, 35, 38]

#------------------------------------------------------

# V=64 - 10^6 (11h)
# Gagnant : (0, 1) - Nombre de plis : 4696 - Nombre de cartes posees : 4696
#cartes_joueur1 = [30, 31, 11, 5, 20, 61, 1, 17, 62, 28, 36, 59, 55, 23, 42, 9, 63, 58, 47, 54, 56, 38, 15, 10, 8, 3, 41, 2, 40, 51, 27, 6]
#cartes_joueur2 = [57, 50, 24, 37, 12, 48, 32, 46, 26, 29, 19, 35, 16, 22, 60, 52, 14, 53, 18, 64, 25, 45, 13, 43, 21, 34, 7, 49, 4, 33, 44, 39]



nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="naturelle", rangement_j2="naturelle",limite_cartes_posees=8000, trace=True)
print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")

