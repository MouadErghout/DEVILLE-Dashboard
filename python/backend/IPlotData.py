from abc import ABC,abstractmethod
class IPlotData(ABC):
   @abstractmethod
   def compareData(self, DataFrames, criteres):
      pass
   @abstractmethod
   def plotdata(self,DataFrames,critere):
      pass

   @abstractmethod
   def Stat_OK_NOK(self, DataFrame):
      pass

   @abstractmethod
   def Stat_N_VS_Nplus1(self, DataFrames, RedevenuOk ):
      pass
