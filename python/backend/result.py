

def check_row(row, nominal, lim_inf, lim_sup):
    return all([
        (row[f'Mesure{i}'] == 0) or (row[f'Mesure{i}'] < (nominal + lim_sup) and row[f'Mesure{i}'] > (nominal + lim_inf)) 
        for i in range(1, 6)
    ])

def filter_conformity(dc):
# Création d'une liste pour les indices des lignes à conserver
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
    return dfConf, dfNConf, conformes, nonConformes