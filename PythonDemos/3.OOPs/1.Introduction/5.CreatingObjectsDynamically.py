class Employee:
    noOfEmo = 0
    def __init__(self,firstName,lastName): 
        self.firstName = firstName
        self.lastName = lastName
        Employee.noOfEmo += 1
    #Method that is bound to a class rather than its object.  
    # First Argument of class method is always class not instance 
    @classmethod    
    def newObjectFromStr(cls,empStr):
        firstName,lastName = empStr.split("-")
        return cls(firstName,lastName)
emp1Str = "Ravi-Solanki"
emp2Str = "Vikash-Solanki"
print(Employee.newObjectFromStr(emp1Str).firstName)
print(Employee.newObjectFromStr(emp2Str).firstName)
print(Employee.noOfEmo)