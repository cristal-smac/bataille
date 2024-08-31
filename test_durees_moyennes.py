from testPlusieurs import *
import time
import pandas as pd

# Tableau des durées moyennes
# On laisse des NA sur la partie symétrique

methodes_rangement = ["naturelle", "aleatoire", "optimisee"]

start_time = time.time()

# Créer un DataFrame vide avec les méthodes de rangement comme index et colonnes
#resultats_df = pd.DataFrame(index=methodes_rangement, columns=methodes_rangement)

# Remplir le DataFrame avec les moyennes des durées sans symétriques
#for i, rang_j1 in enumerate(methodes_rangement):
#    for j, rang_j2 in enumerate(methodes_rangement):
#        if i <= j:  # Exclure les symétriques
#            moyenne_duree,_,_ = simuler_plusieurs(nb_couleurs=4, nb_valeurs=8, nb_parties=1000, rangement_j1=rang_j1, rangement_j2=rang_j2, trace=False)
#            resultats_df.loc[rang_j1, rang_j2] = moyenne_duree
            # resultats_df.loc[rang_j2, rang_j1] = moyenne_duree  # Copier la valeur de la symétrique

# Afficher le tableau des résultats avec pandas
#print("Tableau des moyennes des durées (sans symétriques) :\n")
#print(resultats_df)





# Tableau des moyennes de durées pour C=1
#resultats_df = pd.DataFrame(index=methodes_rangement, columns=[2,3,4,5,10,32,52])
#for i, rangmt in enumerate(methodes_rangement):
#    for j, v in enumerate([2,3,4,5,10,32,52]) :
#        moyenne_duree,_,_ = simuler_plusieurs(nb_couleurs=1, nb_valeurs=v, nb_parties=100000, rangement_j1=rangmt, rangement_j2=rangmt, trace=False)
#        resultats_df.loc[rangmt, v] = moyenne_duree
#print(resultats_df)


# Tableau des moyennes de durées pour C=4
resultats_df = pd.DataFrame(index=methodes_rangement, columns=[2,3,4,5,8,10,13])
for i, rangmt in enumerate(methodes_rangement):
    for j, v in enumerate([2,3,4,5,8,10,13]) :
        moyenne_duree,_,_ = simuler_plusieurs(nb_couleurs=4, nb_valeurs=v, nb_parties=100000, rangement_j1=rangmt, rangement_j2=rangmt, trace=False)
        resultats_df.loc[rangmt, v] = moyenne_duree
print(resultats_df)


end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)  # Convert to minutes and seconds
print(f"\nTemps d'exécution: {int(minutes)} min {int(seconds)} sec")