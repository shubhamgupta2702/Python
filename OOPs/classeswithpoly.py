# classes with polymorphism

class Bird:
  def sound(self):
    print('Birds make sound')
  
class Crow(Bird):
  def sound(self):
    print('Crow says Caw-Caw')
    
class Parrot(Bird):
  def sound(self):
    print("Parrot sounds,Squak")
    
bird1 = Crow()
bird2 = Parrot()
bird3 = Bird()

bird1.sound()
bird2.sound()
bird3.sound()