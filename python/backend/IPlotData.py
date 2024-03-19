from abc import ABC,abstractmethod
class IPlotData(ABC):
   @abstractmethod
   def Plotdata(self,DataFrame,critere):
      pass

   def compareData(self, criteres):
       pass
   def NombreDimNoK(self,DataFrame):
      pass