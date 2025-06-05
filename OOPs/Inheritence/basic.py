class Animal:
  def sound(self):
    print("Animal make sound")
    
class Dog(Animal):  #inherit the property of animal class
  def bark(self):
    print('Dog bark')
    
dog = Dog()
dog.sound()
dog.bark()