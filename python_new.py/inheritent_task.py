class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def method1(self):
        print(self.make,self.model)
class Car(Vehicle):
    pass
obj=Vehicle('maruthi',2024)
obj.method1()

#Employee Hierarchy: Create a base class Employee with attributes like name and salary.
# Derive classes Manager and Engineer from Employee, adding specific methods like assign_task
# for Manager and calculate_bonus for Engineer (based on performance)
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def method(self):
        print(self.name,self.salary)

class Manager(Employee):
