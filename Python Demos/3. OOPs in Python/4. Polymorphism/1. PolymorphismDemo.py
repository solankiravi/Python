#Python Does not support method overloading Concept
class Employee:
    raisePercentage = 1.05
    def __init__(self,firstName,lastName,package): 
        self.firstName = firstName
        self.lastName = lastName
        self.package = package
    def applyRaise(self):
        self.package = self.raisePercentage * self.package
    '''    
    def applyRaise(self,promotionPercentage):
        self.package = self.promotionPercentage * self.package '''
class Developer(Employee):
    raisePercentage = 1.10
    def applyRaise(self):
        self.package = self.raisePercentage * self.package
        
#creating objects
emp1 = Employee("John", "Cena", 20000)
emp2 = Developer("Ravi","Solanki", 30000)
emp1.applyRaise()
emp2.applyRaise()
print(emp1.package); print(emp2.package)
