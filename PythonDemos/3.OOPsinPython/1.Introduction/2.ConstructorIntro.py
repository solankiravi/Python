class Employee:
    #Constructor is created using __init__ method
     #In the init method, self refers to the newly created object;
     # in other class methods, it refers to the instance whose method was called.
    def __init__(self,firstName,lastName): 
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName +"."+ lastName + "@abcd.com"
    #Every method should have at least one argument. First argument should be self
    #Because regular methods automatically takes instance as first argument
    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)  
    def printHello(self):
        print("Hello")   
#creating objects
emp1 = Employee("Ravi","Solanki");emp2 = Employee("Vikash","Solanki")
print(emp1.email);print(emp2.email)
#Calling class's Methods
print(emp1.fullName()); print(emp2.fullName())
print(Employee.fullName(emp1));print(Employee.fullName(emp2))