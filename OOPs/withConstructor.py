class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
  
car1 = Car('Tesla', 'Red')

print(car1.color,car1.brand)
    
'''
syntax --
  class className:
  def __init__(self, parameter1, parameter2,..):
  self.parameter1 = parameter1
  self.parameter2 = parameter2
  
  
__init__()   -->  constructor
self.property  --> stores values inside object
'''