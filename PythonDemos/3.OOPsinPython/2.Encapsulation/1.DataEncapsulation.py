class Employee:
    raisePercent = 1.05
    #name is public. grade is protected and package is private
    def __init__(self,name,grade,package): 
        self.name = name
        self._grade = grade
        self.__package = package
    def UpdatePackage(self):
        self.__package = self.__package * self.raisePercent
    def PrintPackage(self):
        print(self.__package)
class Developer(Employee):
    pass

class DevOps(Developer):  
    pass
#creating objects
emp1 = Developer("Ravi","B",50000) 
print(emp1.name)
print(emp1._grade)
print("======Update Grade==========")
print(emp1.name)
emp1._grade = "D"
print(emp1._grade)

#Devops object
devops1 = DevOps("Utkarsh","C",60000)
print(devops1.name)
print(devops1._grade)
print("======Update Grade==========")
print(devops1.name)
devops1._grade = "D"
print(devops1._grade)

print("======Print Package==========")
emp = Employee("Ravi","B",50000) 
emp.PrintPackage()
print("======Update Package==========")
emp.UpdatePackage()
emp.PrintPackage()