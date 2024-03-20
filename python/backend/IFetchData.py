from abc import ABC,abstractmethod
class IFetchData(ABC):
   @abstractmethod
   def getDFbySheet(self,paths):
      pass

   @abstractmethod
   def replace_all(self):
     pass
   @abstractmethod
   def select_paired_lines(self):
     pass
   @abstractmethod
   def cleanData(self):
      pass

   @abstractmethod
   def check_row(self,row, nominal, lim_inf, lim_sup):
      pass

   @abstractmethod
   def filter_conformity(self):
      pass