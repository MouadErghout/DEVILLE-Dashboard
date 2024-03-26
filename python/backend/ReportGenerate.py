import os


def RepInterface1(df):
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
    reports_path = os.path.join(documents_path, 'reports')
    if not os.path.exists(reports_path):
        os.makedirs(reports_path)

    # Définir le nom du fichier Excel avec le chemin complet
    nom_fichier_excel = os.path.join(reports_path, 'donnees.xlsx')

    # Enregistrer le DataFrame dans un fichier Excel
    df.to_excel(nom_fichier_excel, index=False)