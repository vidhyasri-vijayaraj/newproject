"""
#8/8/23
#Abstraction
from abc import ABC, abstractmethod
class Shapes(ABC):
    @abstractmethod
    def pent(self):
        pass
class Shape(Shapes):
    def pent(self):
        print("I have five sides")
    def pen(self):
         print("I five sides")
class Shap(Shapes):
    def pent(self):
        print("I too have five sides")
obj_1=Shape()
obj_1.pen()
obj_2=Shap()
obj_2.pent()
"""
from abc import ABC, abstractmethod
class Shapes(ABC):
    @abstractmethod
    def pent(self):
        print("First side")
   # @abstractmethod 
    def hex(self):
        print("six sides")
class Shape(Shapes):
    def pent(self):
        print("I have five sides")
class Shap(Shapes):
    def pent(self):
        print("I too have five sides")
obj_1=Shape()
obj_1.pent()
obj_2=Shap()
obj_2.pent()
obj_2.hex()
