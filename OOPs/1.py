class Student:
  def __init__(self, name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade
  
  
student1 = Student("Shubham", 19,"A+")
student2 = Student("Vashu", 20,"A+")
    
    
print(student1.name, student1.age,student1.grade)
print(student2.name, student2.age,student2.grade)


'''
1 - default constructor
2 - parameterized constructor
3 - constructor with default values(self,name="Unknown", age=0)
'''