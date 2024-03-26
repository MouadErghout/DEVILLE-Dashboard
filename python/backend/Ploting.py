import pandas as pd
from python.backend import select_file
from python.backend import clean_data
from python.backend import result
from python.backend import diagramme_camembert


def interface1(paths):
    ## Interface 1, on veut concat les differents file
    ## Garder N°cote Valeur Nominale, Limite Inf', limite sup, tool et emprinte pour le premier file et concat les mesures et index pour le reste

    ## paths = ["./fot10_copie.xlsx","./fot11_copie.xlsx","./fot12_copie.xlsx"]
    print(paths)

    liste_df = select_file.getDFs(paths)
    liste_dc = clean_data.clean_data(liste_df)
    colonnes_a_garder = ["Empreinte",	"Mesure1",	"Mesure2",	"Mesure3",	"Mesure4",	"Mesure5",	"Index"]
    liste_to_concat = []
    for i in range(len(liste_dc)): # pour chaque dataframe dans la liste
        if i == 0:
            liste_to_concat.append(liste_dc[i]) # on ajoute toute la premiere dataframe dans une liste
        else:
            df_selected = liste_dc[i][colonnes_a_garder] # on ajoute les dataframe sans les colonnes N° cote, valeur nominal etc pour pas répéter
            liste_to_concat.append(df_selected)


    df = pd.concat(liste_to_concat, axis=1)
    return df

def interface2(paths):
    ##paths = ["./fot10_copie.xlsx", "./fot11_copie.xlsx", "./fot12_copie.xlsx"]
    dict_nok = {}
    liste_df = select_file.getDFs(paths)
    liste_dc = clean_data.clean_data(liste_df)
    liste_ds = result.filter_conformity(liste_dc)

    for i in range(len(liste_ds)):
        print(liste_ds[i][3])
        dict_nok[paths[i]] = liste_ds[i][3]

    return dict_nok

def interface3(paths):
    liste_df = select_file.getDFs(paths)  # appel methode getDFs
    liste_dc = clean_data.clean_data(liste_df)
    liste_ds = result.filter_conformity(liste_dc)

    #print(f"Nombre de côtes conformes : {liste_ds[0][2]}")
    #print(f"Nombre de côtes non conformes : {liste_ds[0][3]}")
    return liste_ds
    # print(f"dataframe conforme : {liste_ds[0][0]}")
    # print(f"dataframe non conformes : {liste_ds[0][1]}")

def interface4(paths,case):
    ##paths = ["./fot10_copie.xlsx", "./fot12_copie.xlsx"]

    liste_df = select_file.getDFs(paths)
    liste_dc = clean_data.clean_data(liste_df)
    liste_ds = result.filter_conformity(liste_dc)

    liste_variables = result.compare_reports(liste_ds)
    diagramme_camembert.afficher_diagramme(liste_variables[0])

    df = result.compare_deep(liste_dc, liste_variables[
        case])  # liste_indices_cas[1] : cas 1. Cette valeur sera attribuée par le frontend
    return liste_ds