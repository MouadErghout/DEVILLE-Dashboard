from abc import ABC,abstractmethod
class IPlotData(ABC):
   @abstractmethod
   def plotdata(self,DataFrame,critere):
      pass

   @abstractmethod
   def compareData(self, criteres):
       pass

   @abstractmethod
   def nombreDimNOK(self,DataFrame):
      pass

   @abstractmethod
   def Stat_OK_NOK(self, DataFrame):
      pass

   @abstractmethod
   def Stat_N_VS_Nplus1(self, DataFrames, RedevenuOk ):
      pass
