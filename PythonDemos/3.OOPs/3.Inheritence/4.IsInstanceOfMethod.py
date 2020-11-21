class Employee:
    raisePercentage = 1.05
    def __init__(self,firstName,lastName,package): 
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = "{} {}".format(self.firstName, self.lastName)
        self.package = package
class Developer(Employee):
    raisePercentage = 1.20
    def __init__(self,firstName,lastName,package,yearsOfExperience):
        super().__init__(firstName,lastName,package)
        self.yearsOfExperience = yearsOfExperience
class Manager(Employee):    
    def __init__(self,firstName,lastName,package,employees = None): 
         super().__init__(firstName,lastName,package)
         if(employees is None):
             self.employees= []
         else:
            self.employees = employees
    def addEmployee(self,emp):
         if(emp not in self.employees):
            self.employees.append(emp)
    def RemoveEmployee(self,emp):
         if(emp  in self.employees):
            self.employees.remove(emp)    
    def PrintAllEmployee(self):
        for emp in self.employees:
            print(emp.fullName)
     
#Employees
emp1 = Employee("John", "Cena", 20000)
#Developers
dev1 = Developer("Ravi","Solanki",50000,1.5) 
dev2 = Developer("Yuvraj","Singh",80000,5.5) 
dev3 = Developer("Virat","Kohli",100000,2.5) 
#Managers
Mgr1 = Manager("Ravi","Shastri",150000)
Mgr1.addEmployee(dev1)
Mgr1.addEmployee(dev2)
Mgr1.addEmployee(dev3)
Mgr1.RemoveEmployee(dev2)
print(Mgr1.PrintAllEmployee())
#Instance Check
print("============================================")
print(isinstance(Mgr1,Manager))
print(isinstance(Mgr1,Employee))
print(isinstance(Mgr1,Developer))