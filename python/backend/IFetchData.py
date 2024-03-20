from abc import ABC,abstractmethod
class IFetchData(ABC):
   @abstractmethod
   def getDFbySheet(self,files):
      pass

   @abstractmethod
   def replace_all(self,df):
     pass
   @abstractmethod
   def select_paired_lines(self,df):
     pass
   @abstractmethod
   def cleanData(self,DataFrames):
      pass

   @abstractmethod
   def check_row(self,row, nominal, lim_inf, lim_sup):
      pass

   @abstractmethod
   def filter_conformity(self,dc):
      pass