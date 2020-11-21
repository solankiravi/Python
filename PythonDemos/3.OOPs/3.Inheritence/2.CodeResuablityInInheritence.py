class Employee:
    raisePercentage = 1.05
    def __init__(self,firstName,lastName,package): 
        self.firstName = firstName
        self.lastName = lastName
        self.package = package
    def applyRaise(self):
        self.package = self.raisePercentage * self.package
class Developer(Employee):
    raisePercentage = 1.20
    pass
class Designer(Employee):
    raisePercentage = 1.10
    pass
#creating objects
emp1 = Employee("John", "Cena", 20000)
emp2 = Developer("Ravi","Solanki",50000) 
emp3 = Designer("Vikash","Solanki",30000)
emp1.applyRaise();emp2.applyRaise();emp3.applyRaise()
print(emp1.package);print(emp2.package);print(emp3.package)