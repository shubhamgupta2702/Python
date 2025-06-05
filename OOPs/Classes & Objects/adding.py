class Car:
  def setDetails(self, color, name):
    self.color = color
    self.name = name
  def showDetails(self):
    print(f'This car is a {self.color} {self.name}')
    
    
car1 = Car()
car1.setDetails('White', "Tesla")

car2 = Car()
car2.setDetails('Black', "Forge")

car1.showDetails()
car2.showDetails()