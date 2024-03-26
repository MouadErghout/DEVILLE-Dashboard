from abc import ABC,abstractmethod
class IFetchData(ABC):
   @abstractmethod
   def selectFiles(self,files):
      pass

   def selectData(self, criteres):
       pass
   def cleanData(self,DataFrame):
      pass