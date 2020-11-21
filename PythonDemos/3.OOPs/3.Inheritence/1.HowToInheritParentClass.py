#Introduction of Inheritence - How to inherit parent class
class Employee:
    def __init__(self,firstName,lastName): 
        self.firstName = firstName
        self.lastName = lastName
    def FullName(self):
        return self.firstName + " " + self.lastName
class Developer(Employee):
    pass
class Designer(Employee):
    pass
#creating objects
emp1 = Developer("Ravi","Solanki"); print(type(emp1))
emp2 = Designer("Vikash","Solanki"); print(type(emp2))
print(emp1.FullName())
print(emp2.FullName())