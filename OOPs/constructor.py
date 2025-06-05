'''
__init__()
'''

class School:
  def student_Details(self, name, rollNo):
    self.name = name
    self.rollNo = rollNo
    
student1 = School()
student1.student_Details("Shubham", 21)

print(student1.name)
print(student1.rollNo)