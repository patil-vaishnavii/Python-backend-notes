# Example of Employee Management system

class Employee:
  def __init__(self,emp_id,name,department):
    self.emp_id = emp_id
    self.name = name
    self.department = department

    print("Employee record is created")

  def display(self):
    print("Employee Details")
    print("ID: ",self.emp_id)
    print("Name: ",self.name)
    print("Department: ",self.department)

  def __del__(self):
    print(f"Employee record of {self.name} removed")

emp1 = Employee(101,"Vaishnavi","Backend Development")

emp1.display()

del emp1

