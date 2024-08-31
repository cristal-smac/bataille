import time
import itertools
import random
import matplotlib.pyplot as plt
import numpy as np
from bataille import *



# Solution 1 : claire, facile mais terriblement inefficace !
#def generer_toutes(coul,val):
#    base_tableau = [i for i in range(1, val + 1) for _ in range(coul)]
#    unique_permutations = set(itertools.permutations(base_tableau))
#    
#    for tableau in unique_permutations:
#        yield tableau


# Solution 2
# Fonction generer_toutes :
# Cette fonction initialise le tableau à remplir ainsi qu'un tableau de compte (counts) pour suivre 
# le nombre de fois que chaque nombre (de 1 à n) a été utilisé.
# 
# Fonction récursive generer :
#    - Elle essaie de placer chaque nombre de 1 à n dans le tableau à la position actuelle (pos).
#    - Si un nombre a été placé moins de Coul fois (vérifié avec counts), il est placé à la position courante.
#    - On incrémente le compteur correspondant au nombre placé et on continue la génération pour la position suivante (pos + 1).
#    - Une fois le tableau rempli, on le coupe en 2 pour avoir 2 mains, et elles sont renvoyées avec yield.
#    - Avant de renvoyer les mains, selon que l'on souhaite ou non les mains symétriques, il faut laisser ou enlever le If
#       (le if est à enlever si les 2 joueurs n'ont pas la même stratégie par exemple)

# ATTENTION renvoie (A,B) puis (B,A)
def generer_toutes_distributions(coul,val):
    # Ne pas dépasser 4, 4
    def generer(tableau, counts, pos, val):
        if pos == len(tableau):
            milieu = len(tableau) // 2
            if tableau[:milieu] <= tableau[milieu:] :  # evite (main1,main2) puis (main2,main1)
                yield tableau[:milieu], tableau[milieu:]
            return
        
        for i in range(1, val + 1):
            if counts[i - 1] < coul:
                tableau[pos] = i
                counts[i - 1] += 1
                yield from generer(tableau, counts, pos + 1, val)
                counts[i - 1] -= 1

    tableau = [0] * (coul * val)
    counts = [0] * val  # Comptage des occurrences de chaque chiffre (1, 2, ..., n)
    
    yield from generer(tableau, counts, 0, val)



def generer_mains_aleatoires(nb_couleurs, nb_valeurs, nb_parties):
    """Génère un itérateur sur nb_parties mains aléatoires dans un paquet de 'couleurs' * 'valeurs'."""
    paquet = list(range(1, nb_valeurs + 1)) * nb_couleurs
    taille_main = len(paquet) // 2

    for _ in range(nb_parties):
        random.shuffle(paquet)
        yield paquet[:taille_main], paquet[taille_main:]


# Cycle aligné si il existe dedans une distrib avec 2 mains de même taille
def isAligne(cycle):
    for (main1,main2) in cycle :
        if (len(main1)==len(main2)):
            return True
    return False

# Cycle nouveau si
def isNouveau(cycle,liste):
    for c in liste:
        if (cycle[0] in c) or (cycle[0][::-1] in c) :
            return False
    return True


def simuler_distributions(distributions, rangement_j1, rangement_j2 , trace, limite_cartes_posees=10000):
    partie_max_duree = 0
    partie_max_distribution = None
    nombre_de_cycles = 0
    all_cycles=[]
    nombre_victoires_j1 = 0
    nombre_victoires_j2 = 0
    nb=0

    liste_durees = []
    for i, (main1, main2) in enumerate(distributions):
        nombre_plis, nombre_cartes_posees, victoires = jouer_partie(list(main1), list(main2), rangement_j1, rangement_j2, limite_cartes_posees, False)
        nb+=1

        if nombre_cartes_posees > 0 :
            # il n'y a donc pas de cycle et j'ai les victoires
            liste_durees.append(nombre_cartes_posees)
            nombre_victoires_j1 += victoires[0]
            nombre_victoires_j2 += victoires[1]
            if trace :
                print(f"Partie {i + 1}: {main1} {main2} \t Victoires : {victoires} Duree = {nombre_cartes_posees}, Nb plis = {nombre_plis}")
            if nombre_cartes_posees > partie_max_duree:
                # si c'est un record
                partie_max_duree = nombre_cartes_posees
                partie_max_distribution = (main1, main2)
                print(f"Nouveau record : {main1} {main2} \t Duree = {nombre_cartes_posees}") #, Nb plis = {nombre_plis}")
        else :
            # Dans ce cas victoire contient le cycle
            nombre_de_cycles += 1
            if isNouveau(victoires,all_cycles):
                all_cycles.append(victoires)
                #if trace :
                #print(f"Nouveau Cycle de taille {len(victoires)} {isAligne(victoires)} : {victoires}" )

    print(f"Nombre de distributions testées : {nb}")

    # Filtrer les valeurs égales à zéro
    liste_durees_sans_zero = [x for x in liste_durees if x > 0]
    # Calculer la moyenne des plis
    moyenne_durees = np.mean(liste_durees_sans_zero)
    print(f"Durée moyenne des parties (en écartant les cycles) : {moyenne_durees:.2f}")
    
    print("\nDistribution qui a nécessité la plus longue partie :")
    print(f"Joueur 1 : {partie_max_distribution[0]}")
    print(f"Joueur 2 : {partie_max_distribution[1]}")
    print(f"Duree pour cette partie : {partie_max_duree}")
    
    print(f"\nNombre victoires_j1 : {nombre_victoires_j1} - Nombre victoires_j2 : {nombre_victoires_j2}")
    print(f"Nombre de cycles détectés : {nombre_de_cycles}")
    print(f"Nombre de cycles différents : {len(all_cycles)}")
    #if (len(all_cycles) > 1) :
    #    print(all_cycles)


    # Générer l'histogramme
    #plt.hist(liste_durees, bins=range(min(liste_durees), max(liste_durees) + 2), edgecolor='black')
    #plt.title('Histogramme des durées (0 représente un cycle)')
    #plt.xlabel('Durees')
    #plt.ylabel('Nombre de parties')
    #plt.show()

    return moyenne_durees, nombre_victoires_j1, nombre_victoires_j2

def simuler_plusieurs(nb_couleurs, nb_valeurs, nb_parties,rangement_j1,rangement_j2,trace):
    print(f"nbCoul={nb_couleurs}, nbVal={nb_valeurs}, rangement_j1={rangement_j2}, rangement_j2={rangement_j2}")
    distributions = generer_mains_aleatoires(nb_couleurs, nb_valeurs, nb_parties)
    return simuler_distributions(distributions,rangement_j1,rangement_j2,trace)

def simuler_toutes_distributions(nb_couleurs, nb_valeurs,rangement_j1,rangement_j2,trace):
    # Ne pas dépasser 4, 4
    print(f"nbCoul={nb_couleurs}, nbVal={nb_valeurs}, rangement_j1={rangement_j2}, rangement_j2={rangement_j2}")
    distributions = generer_toutes_distributions(nb_couleurs, nb_valeurs)
    return simuler_distributions(distributions,rangement_j1,rangement_j2,trace)


# Tester la simulation pour plusieurs distributions aléatoires
if __name__ == "__main__":
    start_time = time.time()
    #simuler_plusieurs(nb_couleurs=4, nb_valeurs=5, nb_parties=1000000, rangement_j1="naturelle", rangement_j2="naturelle", trace=False)
    simuler_toutes_distributions(nb_couleurs=4, nb_valeurs=5, rangement_j1="naturelle", rangement_j2="naturelle",trace=False)
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)  # Convert to minutes and seconds
    print(f"\nTemps d'exécution: {int(minutes)} min {int(seconds)} sec")

