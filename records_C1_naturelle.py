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
# Gagnant : (1, 0) - Nombre de plis : 246 - Nombre de cartes posees : 246
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[9,14,11,2,6,3,16,10]
#cartes_joueur2=[12,1,13,15,8,7,5,4]

# Durée moyenne des parties (en écartant les cycles) : 35.28

#------------------------------------------------------

# V=22 - 10^6

# Gagnant : (0, 1) - Nombre de plis : 1391 - Nombre de cartes posees : 1391
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[11,4,13,14,16,3,18,21,8,17,15,]
#cartes_joueur2=[19,10,6,20,12,2,9,5,7,22,1,]

# Durée moyenne des parties (en écartant les cycles) : 78.58

# Énormément de cycles de taille 264 très majoritairement, puis pas mal de 528 et quelques uns de plus de 1000 étapes
# mais aucun ne sera aligné (si V n'est pas un multiple de 2, pas d'alignement possible).

#------------------------------------------------------

# V=24 - 10^7 (55mn ; 10^6 en 5mn)
# Gagnant : (0, 1) - Nombre de plis : 886 - Nombre de cartes posees : 886
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[16,8,17,9,6,2,14,19,23,12,3,13,]
#cartes_joueur2=[22,24,1,21,11,18,4,10,5,15,7,20,]

# Durée moyenne des parties (en écartant les cycles) : 74.48

#------------------------------------------------------

# V=32 - 10^7 (124mn ; 10^6 en 12mn)
# Gagnant : (1, 0) - Nombre de plis : 1810 - Nombre de cartes posees : 1810
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[3,9,29,23,11,18,20,2,8,25,22,13,1,32,15,17]
#cartes_joueur2=[12,7,26,14,31,21,16,5,27,30,24,6,10,19,28,4]

# Durée moyenne des parties (en écartant les cycles) : 130.10

#------------------------------------------------------

# V=48 - 10^6 (45mn)
# Gagnant : (1, 0) - Nombre de plis : 4146 - Nombre de cartes posees : 4146
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[36,22,16,45,25,48,26,28,20,23,15,33,17,12,42,13,46,27,18,32,19,8,43,6]
#cartes_joueur2=[3,14,2,11,10,37,30,38,41,1,39,34,21,40,29,47,5,24,4,31,44,7,35,9]


#------------------------------------------------------

# V=64 - 10^6 (11h)
# Gagnant : (0, 1) - Nombre de plis : 7568 - Nombre de cartes posees : 7568
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[7,52,62,59,39,8,33,41,63,57,34,36,43,20,12,27,9,38,45,40,50,53,10,49,61,31,46,21,58,19,5,30,]
#cartes_joueur2=[22,29,4,54,32,23,35,44,48,60,14,47,25,55,24,42,26,11,18,13,15,1,6,2,56,64,37,51,17,16,3,28,]




nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="naturelle", rangement_j2="naturelle",limite_cartes_posees=8000, trace=True)
print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")

