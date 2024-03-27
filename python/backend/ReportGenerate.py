import os
from doctest import master
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def RepInterface1(df):
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
    print(documents_path)
    reports_path = os.path.join(os.path.expanduser('~'), 'Documents', 'reports')
    if not os.path.exists(reports_path):
        os.makedirs(reports_path)

    nom_fichier_excel = os.path.join(reports_path, '11donnees.xlsx')

    # Enregistrer le DataFrame dans un fichier Excel
    df.to_excel(nom_fichier_excel, index=False)

