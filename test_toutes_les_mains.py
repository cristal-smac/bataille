from testPlusieurs import *

# Nb de distribs totales
# Coul Val Nb
# 2 2         6
# 2 3        90
# 2 4      2520
# 3 2        20
# 3 3      1680
# 3 4    369600
# 4 2        70
# 4 3     34650
# 4 4  63063000

# Vérifier les nombres de distrib
#for coul in range(2,5):
#    for val in range(2,5):
#       nb=0
#        for main1,main2 in enumerate(generer_toutes_distributions(coul,val)) :
#            nb+=1
#        print(f"coul {coul}  - val {val} -> nb distrib =\t {nb}")


# Analyse de toutes les distribs complètes de (2,2) à (4,4)
# ATTENTION (4,4) prend 1/2h
# (3,3) contient 594 cycles mais est écarté car les 2 paquets ne sont pas de tailles égales
for coul in range(2,5):
    for val in range(2,5):
        if ((coul*val)%2==0):
            print(f"\n--------- nb coul {coul}  - nb val {val}")
            simuler_toutes_distributions(nb_couleurs=coul, nb_valeurs=val, rangement_j1="naturelle", rangement_j2="naturelle",trace=False)
    
print()

