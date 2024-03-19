from python.backend.IPlotData import IPlotData


class ConcretePlotData(IPlotData):
    def plotdata(self, DataFrame, critere):
        print("Tracé des données en fonction du critère :", critere)
        # Exemple de tracé des données à l'aide de DataFrame et du critère

    def compareData(self, criteres):
        print("Comparaison des données avec les critères :", criteres)
        # Exemple de comparaison des données avec les critères

    def nombreDimNOK(self, DataFrame):
        print("Calcul du nombre de dimensions non conformes dans le DataFrame")
        # Exemple de calcul du nombre de dimensions non conformes dans le DataFrame

    def Stat_OK_NOK(self, DataFrame):
        print("Calcul des statistiques OK/NOK dans le DataFrame")
        # Exemple de calcul des statistiques OK/NOK dans le DataFrame

    def Stat_N_VS_Nplus1(self, DataFrames, RedevenuOk):
        print("Comparaison des statistiques entre N et N+1 DataFrames, redévenu OK :", RedevenuOk)
        # Exemple de comparaison des statistiques entre N et N+1 DataFrames, redévenu OK


