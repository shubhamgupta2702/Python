class LMS:
  def setDetails(self,name,marks):
    self.name = name
    self.marks = marks
  
Student1 = LMS()
Student1.setDetails('Aryan', 85)
print(Student1.name)   