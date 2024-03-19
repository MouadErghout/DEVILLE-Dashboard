from abc import ABC,abstractmethod
class IFetchData(ABC):
   @abstractmethod
   def selectFiles(self,files):
      pass
   @abstractmethod

   def selectData(self, DataFrames, criteres):
       pass
   @abstractmethod

   def cleanData(self,DataFrames):
      pass