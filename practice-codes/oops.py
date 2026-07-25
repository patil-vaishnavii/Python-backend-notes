#example of student management system
class Student:
  def __init__(self,name,roll,marks):
    self.name = name
    self.roll = roll
    self.marks = marks

  def display(self):
    print("Name: ",self.name)
    print("Roll No.: ",self.roll)
    print("Marks Obtained: ",self.marks)

  def is_pass(self):
    if self.marks >= 35:
      print("Result : Pass")
    else:
      print("Result : Fail")

student1 = Student("Vaishnavi",101,82)
student2 = Student("Nayan",104,34)

