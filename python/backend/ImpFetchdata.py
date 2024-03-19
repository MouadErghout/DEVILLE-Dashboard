from python.backend.IFetchData import IFetchData


class ConcreteFetchData(IFetchData):
    def selectFiles(self, files):
        print("Sélection des fichiers :", files)

    def selectData(self, DataFrames, criteres):
        print("Sélection des données avec critères :", criteres)
        # Exemple de manipulation de DataFrames
        for df in DataFrames:
            print(df.head())  # Affichage des premières lignes de chaque DataFrame

    def cleanData(self, DataFrames):
        print("Nettoyage des données")
        # Exemple de nettoyage des DataFrames
        for df in DataFrames:
            # Opérations de nettoyage ici
            pass


