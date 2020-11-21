class Employee:
    favSong = "Song 1"
    numOfEmp = 0
    def __init__(self,firstName,lastName): 
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName +"."+ lastName + "@abcd.com"
        Employee.numOfEmp += 1
    def FavSong(self):
        return self.favSong
#creating objects
emp1 = Employee("Ravi","Solanki");emp2 = Employee("Vikash","Solanki")
#Calling class's Methods
emp1.favSong = "Song 2"
print(emp2.favSong);print(emp1.favSong)
print(Employee.numOfEmp)