#Use of Super Keyword
class Employee:
    raisePercentage = 1.05
    def __init__(self,firstName,lastName,package): 
        self.firstName = firstName
        self.lastName = lastName
        self.package = package
class Developer(Employee):
    raisePercentage = 1.20
    def __init__(self,firstName,lastName,package,yearsOfExperience):
        super().__init__(firstName,lastName,package)
        self.yearsOfExperience = yearsOfExperience
    
#creating objects
emp1 = Employee("John", "Cena", 20000)
emp2 = Developer("Ravi","Solanki",50000,1.5) 
print(emp2.yearsOfExperience)
