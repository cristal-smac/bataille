# Idéalement on ferait une classe Carte(valeur, couleur) et une classe joueur(main)
# Mais à la bataille, la couleur ne sert qu'à indiquer combien de fois une valeur apparait.
# Je supprime donc la classe Carte, et finalement aussi la classe joueur.
# Un jeu de cartes n'est plus qu'un tableau d'entiers de 1 à n valeurs apparaissant 1 à n Couleurs fois.
# Par exemple avec C=4 et V=3 , les C*V cartes : [1,2,3,1,2,3,1,2,3,1,2,3]
# Une partie est donc définie par 2 "mains" qui sont des tableaux d'entiers. 

import random


def ranger_cartes(main, pile_manche, mode_rangement):
    """ Range la pile de batailles dans la main gagnante selon le rangement choisi """
    if mode_rangement == "naturelle":
        main.extend(reversed(pile_manche))
    elif mode_rangement == "aleatoire":
        random.shuffle(pile_manche)
        main.extend(pile_manche)
    elif mode_rangement == "optimisee":
        main.extend(sorted(pile_manche, reverse=True))
    else :
        raise Exception("Methode de rangement inconnue ! " + mode_rangement)


def jouer_manche(main1, main2, rangement_j1, rangement_j2, trace=False):
    """ Joue une manche, une serie de cartes qui amène à un gagnant """
    pile_manche = []
    nombre_cartes_posees = 0
    while main1 and main2:
        if trace:
            print(f"Joueur 1 : {main1} - Joueur 2 : {main2}")

        carte_j1 = main1.pop(0)
        carte_j2 = main2.pop(0)
        nombre_cartes_posees+= 1
        if carte_j1 > carte_j2:
            pile_manche.extend([carte_j2, carte_j1])  # Plus forte en dernier
        else:
            pile_manche.extend([carte_j1, carte_j2])  # Plus forte en dernier
        
        if trace:
            print(f"Joueur 1 joue {carte_j1} - Joueur 2 joue {carte_j2} \t pile : {pile_manche}" )
                
        if carte_j1 > carte_j2:
            if trace:
                print("Joueur 1 gagne ce pli!",main1,main2)
            ranger_cartes(main1, pile_manche, rangement_j1)
            return nombre_cartes_posees
        elif carte_j2 > carte_j1:
            if trace:
                print("Joueur 2 gagne ce pli!")
            ranger_cartes(main2, pile_manche, rangement_j2)
            return nombre_cartes_posees

        if trace:
            print("Égalité, c'est la bataille!")
        
    return nombre_cartes_posees

def detecter_cycle(mains_vues, etat_courant):
    try: 
        index = mains_vues.index(etat_courant)
        return mains_vues[index:]
    except ValueError:
        return []


def jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1, rangement_j2, limite_cartes_posees=100, trace=False):
    """Joue une partie avec les cartes spécifiées pour chaque joueur, en détectant les cycles."""
    main1 = cartes_joueur1[:]
    main2 = cartes_joueur2[:]
    
    nombre_plis = 0
    nombre_cartes_posees = 0
    
    mains_vues = []  # Conserve les configurations de mains vues (utilisé pour la détection de cycle)
    
    if trace:
        print("Distribution initiale des cartes :")
        print(f"Joueur 1 : {main1} - {rangement_j1}")
        print(f"Joueur 2 : {main2} - {rangement_j2}")

    while main1 and main2 and nombre_cartes_posees < limite_cartes_posees :
        # On passe à des tuples car les listes sont "mutables" et donc "unhashable"
        etat_courant = (tuple(main1), tuple(main2))
        # Vérification du cycle
        cycle = detecter_cycle(mains_vues, etat_courant)
        if cycle :
            if trace:
                print(f"Cycle de taille {len(cycle)} détecté après {nombre_plis} tours. Partie arrêtée.")
                print(f"cycle : {cycle}")
            return 0, 0, tuple(cycle)  # Cycle détecté, on arrête la partie en renvoyant 0, 0 et le cycle

        mains_vues.append(etat_courant)

        nombre_plis += 1
        if trace:
            print(f"Plis {nombre_plis}")
        
        nombre_cartes_posees += jouer_manche(main1, main2, rangement_j1, rangement_j2, trace)
    
    if nombre_cartes_posees >= limite_cartes_posees:
        #if trace:
        print(f"Limite de {limite_cartes_posees} cartes posees atteinte, arrêt de la partie.")
        exit()
    
    # Les vainqueurs
    if main1 == [] and main2 == [] :
        victoires = (0,0)
    elif main1 == [] :
        victoires = (0,1)
    else :
        victoires =( 1,0)

    return nombre_plis, nombre_cartes_posees, victoires



# Tester la simulation pour plusieurs distributions aléatoires
if __name__ == "__main__":
    # Plus longue partie sans cycle avec 4 couleurs, 3 valeurs en "naturelle": 37 plis, 54 carte posees
    #cartes_joueur1 = [3, 1, 1, 2, 3, 2]
    #cartes_joueur2 = [3, 1, 3, 2, 1, 2]
    #nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="naturelle", rangement_j2="naturelle",limite_cartes_posees=5000, trace=True)
    #print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")

    # Exemple de partie cyclique
    cartes_joueur1 = [3, 2, 1, 1, 2, 1]
    cartes_joueur2 = [2, 1, 3, 2, 3, 3]
    nombre_plis, nombre_cartes_posees, victoires = jouer_partie(cartes_joueur1, cartes_joueur2, rangement_j1="naturelle", rangement_j2="naturelle",limite_cartes_posees=5000, trace=True)
    #print(f"Gagnant : {victoires} - Nombre de plis : {nombre_plis} - Nombre de cartes posees : {nombre_cartes_posees}")

    
