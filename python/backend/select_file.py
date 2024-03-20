import pandas as pd
import numpy

def select_file(path):
        df = pd.read_excel(path,usecols="B,F,I,J,Q,s:w", sheet_name="Dimensional report").copy()[21:] # Ouvrir le fichier et ne regarder que les colonnes interessantes + a partir de ligne 21
        pd.set_option('display.max_rows', None)

        # Renommer les colonnes
        df.rename(columns={
            'Unnamed: 1': 'N° Cote',  # Remplacez 'NouveauNom1' par le nom que vous souhaitez
            'Unnamed: 5': 'Valeur nominale',  # Remplacez 'NouveauNom2' par le nom que vous souhaitez
            'Unnamed: 8': 'Limite Inf',  # etc.
            'Unnamed: 9': 'Limite Sup',
            'Unnamed: 16': 'Empreinte',
            'Unnamed: 18': 'Mesure1',
            'Unnamed: 19': 'Mesure2',
            'Unnamed: 20': 'Mesure3',
            'Unnamed: 21': 'Mesure4',
            'Unnamed: 22': 'Mesure5'
        }, inplace=True)
        return df