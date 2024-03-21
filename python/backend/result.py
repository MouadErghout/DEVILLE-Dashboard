import pandas as pd

def check_row(row, nominal, lim_inf, lim_sup):
    return all([
        (row[f'Mesure{i}'] == 0) or (row[f'Mesure{i}'] < (nominal + lim_sup) and row[f'Mesure{i}'] > (nominal + lim_inf)) 
        for i in range(1, 6)
    ])

def compare_reports(liste_df):

    dr = pd.concat([liste_df[0][1]["N° Cote"],liste_df[1][1]["N° Cote"]], axis=1) # 1er indice : liste des valeurs FOT 10. 2e indice : dataframe Non conforme

    cas1 = 0
    cas2 = 0
    cas3 = 0

    for index, row in dr.iterrows():
        if row[0] == row[1]:
            if pd.notna(row[0]):  # Vérifie que la valeur n'est pas NaN
                cas2 += 1
        elif pd.isna(row[1]):  # Premier cas : valeur dans la première colonne, NaN dans la seconde
            cas3 += 1
        elif pd.isna(row[0]):  # Deuxième cas : NaN dans la première colonne, valeur dans la seconde
            cas1 += 1
    return [cas1,cas2,cas3]

def filter_conformity(liste_dc):
# Création d'une liste pour les indices des lignes à conserver
    liste_valeurs = []
    for dc in liste_dc:
        liste_intermediaire = [] # pour stocker les valeurs dans une liste de liste
        indices_to_keep = []
        indice_to_move = []
        # Parcours du DataFrame en sautant une ligne à chaque fois (pour traiter les paires)
        for index in range(0, len(dc), 2):
            if index + 1 in dc.index:  # Vérifier que la paire existe
                row1 = dc.loc[index]
                row2 = dc.loc[index + 1]
                nominal, lim_inf, lim_sup = row1['Valeur nominale'], row1['Limite Inf'], row1['Limite Sup']

                # Conserver la paire si les deux lignes répondent aux critères
                if check_row(row1, nominal, lim_inf, lim_sup) and check_row(row2, nominal, lim_inf, lim_sup):
                    indices_to_keep.extend([index, index + 1])
                else:
                    indice_to_move.extend([index, index + 1])

        dfConf = dc.loc[indices_to_keep] # conformes
        dfNConf= dc.loc[indice_to_move] # non conformes
            # Affiche toutes les côtes conformes
        conformes = len(dfConf)/2
        nonConformes = len(dfNConf)/2
        liste_intermediaire.extend([dfConf, dfNConf, conformes, nonConformes])
        liste_valeurs.append(liste_intermediaire)

    return liste_valeurs