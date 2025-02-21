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

# Exploré complètement par Clément Courbet le 20/02/2025

# Aucun cycle encore trouvé aléatoirement : A mon avis, il n'y en n'a pas

#------------------------------------------------------

# V=6
# NOUVEAU Gagnant : (1, 0) - Nombre de plis : 994 - Nombre de cartes posees : 1190
# découvert par Marc Lapierre le 19/02/2025
#cartes_joueur1 = [3,4,5,4,1,1,6,2,1,1,2,3]
#cartes_joueur2 =  [5,4,4,5,6,6,2,2,6,3,5,3]
# Duree moyenne = 72.37

# Enormément de cycles alignés. Ici ex de taille 36
#cartes_joueur1 = [4, 2, 5, 5, 4, 2, 6, 6, 3, 2, 2, 1]
#cartes_joueur2 = [5, 4, 5, 1, 6, 4, 6, 1, 3, 1, 3, 3]


#------------------------------------------------------

# V=7
# NOUVEAU Gagnant : (1, 0) - Nombre de plis : 1611 - Nombre de cartes posees : 1880
# découvert par Marc Lapierre le 19/02/2025
#cartes_joueur1 = [1,1,1,1,2,2,2,2,3,6,6,3,6,7]
#cartes_joueur2 = [4,3,5,4,5,4,5,6,3,7,7,5,4,7]

# Enormément de cycles 



#------------------------------------------------------

# V=8  (jeu de 32 cartes)
# Gagnant : (0, 1) - Nombre de plis : 2308 - Nombre de cartes posees : 2602
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[5,5,1,4,6,1,8,3,6,5,3,7,8,2,2,8,]
#cartes_joueur2=[7,8,7,6,1,3,4,7,5,1,4,3,2,6,4,2,]

# Cycle de taille 48
#cartes_joueur1 = [8, 5, 5, 1, 6, 2, 6, 6, 7, 2, 7, 7, 4, 2, 4, 4]
#cartes_joueur2 = [8, 1, 8, 8, 6, 5, 5, 1, 7, 3, 3, 1, 4, 3, 3, 2]

#------------------------------------------------------

# V=9
# Gagnant : (1, 0) - Nombre de plis : 2708 - Nombre de cartes posees : 3024
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[3,3,1,3,7,9,1,2,6,3,4,4,6,7,2,2,9,5]
#cartes_joueur2=[5,8,7,4,8,5,1,5,8,1,7,2,4,9,8,6,6,9]

# Aucun cycle encore trouvé aléatoirement.

#------------------------------------------------------

# V=10
# Gagnant : (1, 0) - Nombre de plis : 3745 - Nombre de cartes posees : 4120
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[7,9,2,1,8,4,3,9,7,9,1,6,4,5,10,5,4,7,6,3]
#cartes_joueur2=[2,9,10,2,8,1,10,5,7,6,2,3,8,5,8,1,3,6,4,10]

# Aucun cycle encore trouvé aléatoirement


#------------------------------------------------------

# V=11
# Gagnant : (0, 1) - Nombre de plis : 4211 - Nombre de cartes posees : 4582
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[10,5,11,5,2,3,4,6,10,10,8,8,9,4,5,1,10,5,11,7,8,8]
#cartes_joueur2=[4,9,1,7,1,6,2,3,6,3,3,9,2,7,9,2,7,1,11,11,4,6]

# Cycle découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[1,3,4,9,4,9,6,5,10,7,6,10,5,7,10,11,11,2,8,7,9,5]
#cartes_joueur2=[8,1,4,1,4,8,2,11,6,3,7,2,8,3,9,1,2,3,10,5,6,11]


#------------------------------------------------------

# V=12
# Gagnant : (1, 0) - Nombre de plis : 4913 - Nombre de cartes posees : 5346
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[8,11,5,8,7,3,11,4,6,7,6,2,12,3,1,5,10,12,2,5,11,6,2,5]
#cartes_joueur2=[10,7,9,8,6,3,9,12,9,2,9,4,11,1,1,1,4,4,7,12,8,10,3,10]

# Aucun cycle encore trouvé aléatoirement

#------------------------------------------------------

# V=13
# Gagnant : (1, 0) - Nombre de plis : 5610 - Nombre de cartes posees : 6038
# découvert par Clément Courbet le 20/02/2025
#cartes_joueur1=[7,4,10,12,11,9,8,1,2,6,13,2,6,2,11,6,1,13,1,11,5,12,5,12,4,7]
#cartes_joueur2=[9,9,10,7,8,4,9,6,10,10,3,3,5,3,8,13,3,11,7,2,4,12,1,8,5,13]

# Aucun cycle encore trouvé aléatoirement




nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="naturelle", rangement_j2="naturelle",limite_cartes_posees=8000, trace=True)
print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")

