from python.backend.IFetchData import IFetchData
import pandas as pd


class ImpFetchData(IFetchData):
    def __init__(self):
        self.dfs = {}

    @property
    def dfs(self):
        return self._dfs

    # Setter pour l'attribut 'name'
    @dfs.setter
    def dfs(self, value):
        self._dfs = value


    def getDFbySheet(self, paths):
        for p in paths:
            df = pd.read_excel(p, usecols="B,F,I,J,Q,s:w", sheet_name="Dimensional report").copy()[
                 21:]  # Ouvrir le fichier et ne regarder que les colonnes interessantes + a partir de ligne 21
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
            self.dfs[p] = df



    def replace_all(self):
        dfs ={}
        for key, df in self.dfs.items():
            for column in df.columns:
                df[column] = pd.to_numeric(df[column],
                                           errors='coerce')  # Dans toutes les colones on converti chaque valeur en float, si erreur remplacer nan

            df.fillna(0, inplace=True)  # remplace nan par 0 partout
            dfs[key]=df
        self.dfs=dfs

    def select_paired_lines(self):
        dcs = {}
        for key, df in self.dfs.items():
            dfcotes = df[df[
                             'N° Cote'] > 10]  # ne conserve que les lignes ou la valeur de la colonne est supérieure à 10 pour éliminer tous les espaces
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
            dcs[key]=dc
        self.dfs=dcs

    def cleanData(self):
        self.replace_all(self.dfs)
        self.select_paired_lines(self.dfs)


    def check_row(self,row, nominal, lim_inf, lim_sup):
        return all([
            (row[f'Mesure{i}'] == 0) or (
                        row[f'Mesure{i}'] < (nominal + lim_sup) and row[f'Mesure{i}'] > (nominal + lim_inf))
            for i in range(1, 6)
        ])

    def filter_conformity(self):
        dcs = {}
        for key, dc in self.dfs.items():
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
                    if self.check_row(row1, nominal, lim_inf, lim_sup) and self.check_row(row2, nominal, lim_inf, lim_sup):
                        indices_to_keep.extend([index, index + 1])
                    else:
                        indice_to_move.extend([index, index + 1])

            dfConf = dc.loc[indices_to_keep]  # conformes
            dfNConf = dc.loc[indice_to_move]  # non conformes
            # Affiche toutes les côtes conformes
            conformes = len(dfConf) / 2
            nonConformes = len(dfNConf) / 2
        return dfConf, dfNConf, conformes, nonConformes






