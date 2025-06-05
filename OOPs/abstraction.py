from abc import ABC, abstractmethod

class Vehichle(ABC):
  @abstractmethod
  def start(self):
    pass #no implementation
  
class Car(Vehichle):
  def start(self):
    print('Car starts with key')
    
class Bike(Vehichle):
  def start(self):
    print("Bike starts with a button")
    
    
car = Car()
bike = Bike()

car.start()
bike.start()