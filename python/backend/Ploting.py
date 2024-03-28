import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from python.backend import select_file
from python.backend import clean_data
from python.backend import result
from python.backend import diagramme_camembert
from python.backend.ReportGenerate import RepInterface1


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
    RepInterface1(df)

def interface2(paths,master):
    ##paths = ["./fot10_copie.xlsx", "./fot11_copie.xlsx", "./fot12_copie.xlsx"]
    dict_nok = {}
    liste_df = select_file.getDFs(paths)
    liste_dc = clean_data.clean_data(liste_df)
    liste_ds = result.filter_conformity(liste_dc)

    for i in range(len(liste_ds)):
        print(liste_ds[i][3])
        dict_nok[i] = liste_ds[i][3]


    # Extract keys (file paths) and values (number of dimensions NOK)
    file_paths = list(dict_nok.keys())
    dimensions_nok = list(dict_nok.values())

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the histogram
    ax.bar(file_paths, dimensions_nok, color='skyblue')
    ax.set_xlabel('Fichier Excel')
    ax.set_ylabel('Nombre de dimensions NOK')
    ax.set_title('Nombre de dimensions NOK par rapport sélectionné')
    ax.tick_params(axis='x', rotation=45, labelsize=8)
    plt.tight_layout()

    # Embed the plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def interface3(paths,master):
    liste_df = select_file.getDFs(paths)  # appel methode getDFs
    liste_dc = clean_data.clean_data(liste_df)
    liste_ds = result.filter_conformity(liste_dc)

    #print(f"Nombre de côtes conformes : {liste_ds[0][2]}")
    #print(f"Nombre de côtes non conformes : {liste_ds[0][3]}")
    labels = 'Conformes', 'Non conformes'
    sizes = [liste_ds[0][2], liste_ds[0][3]]
    colors = ['gold', 'lightskyblue']
    explode = (0.1, 0)  # explode 1st slice (i.e. 'Conformes')

    # Plot
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Répartition des conformes et des non conformes')

    # Embed the plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig1, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
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