from testPlusieurs import *
import pandas as pd

# Tableau du nombre de victoires sur 10000
# On laisse des 0 sur la diagonale

methodes_rangement = ["naturelle", "aleatoire", "optimisee"]
nb_parties=100000

# Créer un DataFrame vide avec les méthodes de rangement comme index et colonnes
resultats_df = pd.DataFrame(0,index=methodes_rangement, columns=methodes_rangement)

# Remplir le DataFrame avec le nombre de victoires sans symétriques
for i, rang_j1 in enumerate(methodes_rangement):
    for j, rang_j2 in enumerate(methodes_rangement):
        if i < j:  # Exclure les symétriques
            _,vj1,vj2 = simuler_plusieurs(nb_couleurs=4, nb_valeurs=13, nb_parties=nb_parties, rangement_j1=rang_j1, rangement_j2=rang_j2, trace=False)
            resultats_df.loc[rang_j1, rang_j2] += vj1
            resultats_df.loc[rang_j2, rang_j1] += vj2

df_percent = (resultats_df / nb_parties) * 100
# Afficher le tableau des résultats avec pandas
print("Tableau des pourcentages de victoires (sans symétriques) :\n")
#print(resultats_df)
print(df_percent)