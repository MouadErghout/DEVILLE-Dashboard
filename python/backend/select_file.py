import pandas as pd
import numpy

def select_file(path): # Devrait retourner une liste des path, pour pouvoir rendre l'affichage des graphiques et des interfaces dynamique.
        liste_df = []
        for p in path:
            df = pd.read_excel(p,usecols="B,F,I,J,P,Q,s:w,Y", sheet_name="Dimensional report").copy()[21:] # Ouvrir le fichier et ne regarder que les colonnes interessantes + a partir de ligne 21
            pd.set_option('display.max_rows', None)

            # Renommer les colonnes
            df.rename(columns={
                'Unnamed: 1': 'N° Cote',  # Remplacez 'NouveauNom1' par le nom que vous souhaitez
                'Unnamed: 5': 'Valeur nominale',  # Remplacez 'NouveauNom2' par le nom que vous souhaitez
                'Unnamed: 8': 'Limite Inf',  # etc.
                'Unnamed: 9': 'Limite Sup',
                'Unnamed: 15': 'Measure tool',
                'Unnamed: 16': 'Empreinte',
                'Unnamed: 18': 'Mesure1',
                'Unnamed: 19': 'Mesure2',
                'Unnamed: 20': 'Mesure3',
                'Unnamed: 21': 'Mesure4',
                'Unnamed: 22': 'Mesure5',
                'Unnamed: 24': 'Index'
            }, inplace=True)
            liste_df.append(df)
        return liste_df