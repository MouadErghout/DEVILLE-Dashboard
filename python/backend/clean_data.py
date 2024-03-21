import pandas as pd
import numpy

def replace_all(df):
        for column in df.columns:
                df[column] = pd.to_numeric(df[column], errors='coerce') # Dans toutes les colones on converti chaque valeur en float, si erreur remplacer nan

        df.fillna(0, inplace=True) # remplace nan par 0 partout
        return df

def select_paired_lines(df):
    dfcotes = df[df['N° Cote'] > 10] # ne conserve que les lignes ou la valeur de la colonne est supérieure à 10 pour éliminer tous les espaces 
    indices = dfcotes.index.tolist()
    indices_to_keep = list(indices)  # Utilisation d'un set pour éviter les doublons

                        # Ajout de l'indice de la ligne suivante pour chaque ligne conforme
    for index in indices:
            next_index = index + 1
            if next_index in df.index:  # Assurez-vous que l'indice suivant est dans le DataFrame original
                indices_to_keep.append(next_index)

                        # Création du nouveau DataFrame avec les lignes sélectionnées
    dcotes = df.loc[indices_to_keep]

                        # Tri du DataFrame selon l'ordre initial des indices
    dc = dcotes.sort_index()
    dc.reset_index(drop=True, inplace=True) 
                
    return dc

def clean_data(liste_df):
        new_list_df = []
        for df in liste_df:
                df = replace_all(df)
                dc = select_paired_lines(df)
                new_list_df.append(dc)
        return new_list_df